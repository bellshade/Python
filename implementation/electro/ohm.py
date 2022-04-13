from typing import Dict


def ohm(voltage: float, current: float, resistance: float) -> dict[str, float]:
    """
    Terapkan Hukum Ohm, pada dua nilai listrik yang diberikan,
    yang dapat berupa tegangan, arus,
    dan resistensi, dan kemudian dalam Python dict return nama/nilai dari nilai nol.
    >>> ohm(voltage=10, resistance=5, current=0)
    {'current': 2.0}
    >>> ohm(voltage=0, current=0, resistance=10)
    Traceback (most recent call last):
    ...
    ValueError: Hanya satu argumen 0, yang bisa diisi.
    >>> ohm(voltage=0, current=1, resistance=-2)
    Traceback (most recent call last):
    ...
    ValueError: Resistan tidak boleh negatif.
    >>> ohm(resistance=0, voltage=-10, current=1)
    {'resistance': -10.0}
    >>> ohm(voltage=0, current=-1.5, resistance=2)
    {'voltage': -3.0}
    """
    if (voltage, current, resistance).count(0) != 1:
        raise ValueError("Hanya satu argumen 0, yang bisa diisi.")
    if resistance < 0:
        raise ValueError("Resistan tidak boleh negatif.")
    if voltage == 0:
        return {"voltage": float(current * resistance)}
    elif current == 0:
        return {"current": voltage / resistance}
    elif resistance == 0:
        return {"resistance": voltage / current}
    else:
        raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
