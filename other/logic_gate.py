# Program sedergana untuk membuat gerbang logika
# https://en.wikipedia.org/wiki/Logic_gate


def NOT_gate(input_1 : int) -> int | str:
    """
    NOT gate adalah gerbang logika yang menghasilkan 0
    jika input satu dan begitu juga sebaliknya.

    >>> NOT_gate(1)
    0
    >>> NOT_gate(0)
    1

    """
    error = "angka hanya satu dan nol"
    if input_1 == 1 :
        return 0
    elif input_1 == 0 :
        return 1
    else :
        return error


def OR_gate(int_1 : int , int_2 : int) -> int | str:
    """
    OR gate adalah gerbang yang menghasilkan 0 jika dua
    input 0.

    >>> OR_gate(0,0)
    0
    >>> OR_gate(0,1)
    1
    >>> OR_gate(1,0)
    1
    >>> OR_gate(1,1)
    1
    >>> OR_gate(3,0)
    'angka hanya satu dan nol'

    """
    error = "angka hanya satu dan nol"
    if int_1 == 0 and int_2 == 0:
        return 0
    elif int_1 == 1 and int_2 == 0:
        return 1
    elif int_1 == 0 and int_2 == 1:
        return 1
    elif int_1 == 1 and int_2 == 1:
        return 1
    else:
        return error


def AND_gate(int_1 : int , int_2 : int) -> int | str:
    """
    AND gate adalah gerbang yang menghasilkan 1 jika dua
    input 1.

    >>> AND_gate(0,0)
    0
    >>> AND_gate(0,1)
    0
    >>> AND_gate(1,0)
    0
    >>> AND_gate(1,1)
    1
    >>> NAND_gate(3,0)
    'angka hanya satu dan nol'

    """
    error = "angka hanya satu dan nol"
    if int_1 == 0 and int_2 == 0:
        return 0
    elif int_1 == 1 and int_2 == 0:
        return 0
    elif int_1 == 0 and int_2 == 1:
        return 0
    elif int_1 == 1 and int_2 == 1:
        return 1
    else:
        return error


def NAND_gate(int_1 : int , int_2 : int) -> int | str:
    """
    NAND gate adalah gerbang yang menghasilkan 0 jika dua
    input 1.

    >>> NAND_gate(0,0)
    1
    >>> NAND_gate(0,1)
    1
    >>> NAND_gate(1,0)
    1
    >>> NAND_gate(1,1)
    0
    >>> NAND_gate(3,0)
    'angka hanya satu dan nol'

    """
    error = "angka hanya satu dan nol"
    if int_1 == 0 and int_2 == 0:
        return 1
    elif int_1 == 1 and int_2 == 0:
        return 1
    elif int_1 == 0 and int_2 == 1:
        return 1
    elif int_1 == 1 and int_2 == 1:
        return 0
    else:
        return error


def NOR_GATE(int_1 : int , int_2 : int) -> int | str:
    """
    NOR gate adalah gerbang yang menghasilkan 1 jika dua
    input 0.

    >>> NAND_gate(0,0)
    1
    >>> NAND_gate(0,1)
    1
    >>> NAND_gate(1,0)
    1
    >>> NAND_gate(1,1)
    0
    >>> NAND_gate(3,0)
    'angka hanya satu dan nol'

    """
    error = "angka hanya satu dan nol"
    if int_1 == 0 and int_2 == 0:
        return 1
    elif int_1 == 1 and int_2 == 0:
        return 0
    elif int_1 == 0 and int_2 == 1:
        return 0
    elif int_1 == 1 and int_2 == 1:
        return 0
    else:
        return error


def XOR_gate(int_1 : int , int_2 : int) -> int | str:
    """
    XOR gate adalah gerbang yang akan menghasilkan angka 1 jika
    input nya berlawanan.
    >>> XOR_gate(0,0)
    0
    >>> XOR_gate(1,0)
    1
    >>> XOR_gate(0,1)
    1
    >>> XOR_gate(1,1)
    0
    """
    error = "angka hanya satu dan nol"
    if int_1 == 0 and int_2 == 0:
        return 0
    elif int_1 == 1 and int_2 == 0:
        return 1
    elif int_1 == 0 and int_2 == 1:
        return 1
    elif int_1 == 1 and int_2 == 1:
        return 0
    else:
        return error


def XNOR_gate(int_1  : int, int_2 : int) -> int | str:
    """
    XNOR gate adalah gerbang yang yang akan menghasilkan 1 jika
    inputnya sama.
    >>> XNOR_gate(0,0)
    1
    >>> XNOR_gate(1,0)
    0
    >>> XNOR_gate(0,1)
    0
    >>> XNOR_gate(1,1)
    1
    """
    error = "angka hanya satu dan nol"
    if int_1 == 0 and int_2 == 0:
        return 1
    elif int_1 == 1 and int_2 == 0:
        return 0
    elif int_1 == 0 and int_2 == 1:
        return 0
    elif int_1 == 1 and int_2 == 1:
        return 1
    else:
        return error


if __name__ == "__main__":
    import doctest

    doctest.testmod()
