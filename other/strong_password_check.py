# cek password kuat atau tidak

from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def strong_password_detector(password: str, min_length: int = 8) -> str:
    """
    >>> strong_password_detector("Hwea7$2!")
    'password kuat'

    >>> strong_password_detector("Sh0r1")
    'password setidaknya melebihi 8 karakter'

    >>> strong_password_detector("Test123")
    'password setidaknya melebihi 8 karakter'
    """

    if len(str(password)) < 8:
        return "password setidaknya melebihi 8 karakter"

    upper = any(char in ascii_uppercase for char in password)
    lower = any(char in ascii_lowercase for char in password)
    num = any(char in digits for char in password)
    spec_char = any(char in punctuation for char in password)

    if upper and lower and num and spec_char:
        return "password kuat"

    else:
        return (
            "password harus mengandung HURUF BESAR, huruf kecil, "
            "angka, karakter lain"
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
