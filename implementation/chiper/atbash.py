import string


def atbash(sequence: str) -> str:
    """
    >>> atbash("ABCDEFG")
    'ZYXWVUT'
    """
    letters = string.ascii_letters
    letters_reversed = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]
    return "".join(
        letters_reversed[letters.index(c)] if c in letters else c for c in sequence
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
