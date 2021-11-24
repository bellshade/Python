import re


def parse_path(url: str) -> str:
    """
    Fungsi yang menerima input berupa string url dan mengembalikan
    string yang berisi path dari url.

    Contoh:
    >>> parse_path("github.com")
    '/'
    >>> parse_path("www.github.com/about#footer")
    '/about/'
    >>> parse_path("http://github.com/contact-us")
    '/contact-us/'
    >>> parse_path("https://www.github.com/sebuah-slug-yang-panjang-sekali")
    '/sebuah-slug-yang-panjang-sekali/'
    """
    path_pattern = re.compile(r"""
        (?:https?://)?          # filter skema http:// atau https://
        (?:[^/]+)               # filter lokasi domain
        ([^\.\?#]+)?\??         # masukkan path kedalam capture group 1
    """, re.VERBOSE)

    # mengambil path dari url
    path = path_pattern.search(url).group(1) or ''

    return f"{path}/"


def generate_anchor_tag(url: str, description: str) -> str:
    """
    Fungsi yang menerima input berupa string url dan string description
    dan mengembalikan string yang berisi tag anchor dengan isi url dan
    description yang sama dengan input.

    Fungsi ini akan mengembalikan tag anchor dengan url yang berisi "/"
    dan description yang berisi "HOME"

    Contoh:
    >>> generate_anchor_tag("", "")
    '<a href="/">HOME</a>'
    >>> generate_anchor_tag("/about", "ABOUT")
    '<a href="/about">ABOUT</a>'
    >>> generate_anchor_tag("/contact-us", "CONTACT US")
    '<a href="/contact-us">CONTACT US</a>'
    >>> generate_anchor_tag("/sebuah-slug-yang-panjang-sekali", "SSYPS")
    '<a href="/sebuah-slug-yang-panjang-sekali">SSYPS</a>'
    """
    if url == "":
        url = "/"
        description = "HOME"

    return f'<a href="{url}">{description}</a>'


def generate_span_tag(description: str) -> str:
    """
    Fungsi yang menerima input berupa string dan kemudian
    mengembalikan string yang berisi tag span dengan class
    'active' dan isi yang sama dengan input.

    Contoh:
    >>> generate_span_tag("")
    '<span class="active">HOME</span>'
    >>> generate_span_tag("ABOUT")
    '<span class="active">ABOUT</span>'
    >>> generate_span_tag("CONTACT US")
    '<span class="active">CONTACT US</span>'
    >>> generate_span_tag("SSYPS")
    '<span class="active">SSYPS</span>'
    """
    if description == "":
        description = "HOME"

    return f'<span class="active">{description}</span>'


def generate_description(slug: str) -> str:
    """
    Fungsi yang menerima input berupa string dengan kebab-case
    dan mengubahnya menjadi string UPPERCASE.
    Fungsi ini juga akan mengakronim input yang terlalu panjang
    (lebih dari 30 karakter).

    Contoh:
    >>> generate_description("home")
    'HOME'
    >>> generate_description("about")
    'ABOUT'
    >>> generate_description("contact-us")
    'CONTACT US'
    >>> generate_description("sebuah-slug-yang-panjang-sekali")
    'SSYPS'
    """
    if len(slug) > 30:
        # return akronim dari slug yang telah
        # dipisahkan ke dalam sebuah list
        return "".join([d[0] for d in slug.split("-")]).upper()
    else:
        return slug.replace("-", " ").upper()


def generate_breadcrumb(url, separator):
    """
    Fungsi yang menerima input berupa string url dan separator
    dan mengembalikan string yang berisi navigasi breadcrumb.

    Halaman Wikipedia tentang navigasi breadcrumb:
    https://en.wikipedia.org/wiki/Breadcrumb_navigation

    Contoh:
    >>> generate_breadcrumb("youtube.com", " > ")
    '<span class="active">HOME</span>'
    >>> generate_breadcrumb("https://github.com/harmonify/index.html", " > ")
    '<a href="/">HOME</a> > <span class="active">HARMONIFY</span>'
    >>> generate_breadcrumb("facebook.com/sebuah-slug-yang-panjang-sekali", " / ")
    '<a href="/">HOME</a> / <span class="active">SSYPS</span>'
    """
    # inisialisasi variabel untuk menampung hasil
    result = []

    # ambil path dari url
    path = parse_path(url)

    # filter akhiran index.* dari path
    path = re.sub(r"index\.?.*$", '', path).split('/')
    if path[-1] == '':
        path.pop()

    # generate tag anchor dari awal sampai dengan
    # elemen kedua terakhir dari path
    for i in range(len(path[:-1])):
        url = '/'.join(path[:i + 1])
        desc = generate_description(path[i])
        anchor = generate_anchor_tag(url, desc)

        result.append(anchor)

    # generate tag span dengan elemen terakhir dari path
    span = generate_span_tag(generate_description(path[-1]))
    result.append(span)

    # return hasil join tag anchor dengan separator
    return separator.join(result)


def main(args=None):
    import doctest

    doctest.testmod()

    # basic tests
    print(generate_breadcrumb("youtube.com", " > ") ==
          '<span class="active">HOME</span>')

    print(generate_breadcrumb("https://github.com/harmonify/index.html", " > ") ==
          '<a href="/">HOME</a> > <span class="active">HARMONIFY</span>')

    print(generate_breadcrumb("facebook.com/sebuah-slug-yang-panjang-sekali", " / ") ==
          '<a href="/">HOME</a> / <span class="active">SSYPS</span>')

    # custom tests
    print(generate_breadcrumb("websiteku.com/services/api/basic", " | ") ==
          '<a href="/">HOME</a> | <a href="/services">SERVICES</a> | ' +
          '<a href="/services/api">API</a> | <span class="active">BASIC</span>')


if __name__ == '__main__':
    main()
