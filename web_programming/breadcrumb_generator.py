import re


def parse_path(url: str) -> str:
    path_pattern = re.compile(r"""
        (?:https?://)?          # filter skema http:// atau https://
        (?:[^/]+)               # filter lokasi domain
        ([^\.\?#]+)?\??         # masukkan path kedalam capture group 1
    """, re.VERBOSE)

    # mengambil path dari url
    path = path_pattern.search(url).group(1) or ''

    return f"{path}/"


def generate_anchor_tag(url: str, description: str) -> str:
    if url == "":
        url = "/"
        description = "HOME"

    return f'<a href="{url}">{description}</a>'


def generate_span_tag(description: str) -> str:
    if description == "":
        description = "HOME"

    return f'<span class="active">{description}</span>'


def generate_description(slug: str) -> str:
    if len(slug) > 30:
        # return akronim dari slug yang telah
        # dipisahkan ke dalam sebuah list
        return "".join([d[0] for d in slug.split("-")]).upper()
    else:
        return slug.replace("-", " ").upper()


def generate_breadcrumb(url, separator):
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
    print(generate_breadcrumb("youtube.com", " > ") ==
          '<span class="active">HOME</span>')

    print(generate_breadcrumb("https://github.com/harmonify/index.html", " > ") ==
          '<a href="/">HOME</a> > <span class="active">HARMONIFY</span>')

    print(generate_breadcrumb("facebook.com/sebuah-slug-yang-panjang-sekali", " / ") ==
          '<a href="/">HOME</a> / <span class="active">SSYPS</span>')

    print(generate_breadcrumb("websiteku.com/services/api/basic", " | ") ==
          '<a href="/">HOME</a> | <a href="/services">SERVICES</a> | ' +
          '<a href="/services/api">API</a> | <span class="active">BASIC</span>')


if __name__ == '__main__':
    main()
