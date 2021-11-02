import base64


def encode_b32(msg: str) -> bytes:
    """
    >>> encode_b32('ini contoh')
    b'NFXGSIDDN5XHI33I'
    """
    encoded = msg.encode("utf-8")
    b32_encode = base64.b32encode(encoded)

    return b32_encode


if __name__ == "__main__":
    import doctest

    doctest.testmod()
