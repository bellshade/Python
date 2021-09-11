import base64


def encode_b16(msg: str) -> bytes:
    """
    >>> encode_b16('ini contoh')
    b'696E6920636F6E746F68'
    """
    encoded = msg.encode("utf-8")
    b16_encode = base64.b16encode(encoded)

    return b16_encode


if __name__ == "__main__":
    import doctest

    doctest.testmod()
