import base64


def base85(msg: str) -> bytes:
    """
    >>> base85("ini contoh")
    b'Bl7W-@rH7,DeK'
    """
    encoded = msg.encode("utf-8")
    encoded85 = base64.a85encode(encoded)

    return encoded85


if __name__ == "__main__":
    import doctest

    doctest.testmod()
