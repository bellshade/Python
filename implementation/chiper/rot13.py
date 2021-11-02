# program rot13
# https://en.wikipedia.org/wiki/ROT13


def decrypt(s: str, n: int = 13) -> str:
    """
    >>> msg = "keadaan pantai aman"
    >>> decrypt(msg)
    'xrnqnna cnagnv nzna'
    """
    out = ""
    for c in s:
        if "A" <= c <= "Z":
            out += chr(ord("A") + (ord(c) - ord("A") + n) % 26)
        elif "a" <= c <= "z":
            out += chr(ord("a") + (ord(c) - ord("a") + n) % 26)
        else:
            out += c

    return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
