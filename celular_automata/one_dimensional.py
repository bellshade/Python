# Mengembalikan gambar 16 generasi automata seluler satu
# dimensi berdasarkan yang diberikan nomor aturan
# https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
from __future__ import annotations

from PIL import Image

CELLS = [
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
]


def format_ruleset(ruleset: int) -> list[int]:
    """
    >>> format_ruleset(11100)
    [0, 0, 0, 1, 1, 1, 0, 0]
    """
    return [int(c) for c in f"{ruleset:08}"[:8]]


def new_generation(cells: list[list[int]], rule: list[int], time: int) -> list[int]:
    populasi = len(cells[0])
    next_generation = []
    for i in range(populasi):
        left = 0 if i == 0 else cells[time][i - 1]
        right = 0 if i == populasi - 1 else cells[time][i + 1]
        situasi = 7 - int(f"{left}{cells[time][i]}{right}", 2)
        next_generation.append(rule[situasi])
    return next_generation


def generate_image(cells: list[list[int]]) -> Image.Image:
    """
    Ubah sel menjadi PIL.Image.
    Image skala abu-abu dan kembalikan ke pemanggil.
    >>> from random import random
    >>> cells = [[random() for w in range(31)] for h in range(16)]
    >>> img = generate_image(cells)
    >>> isinstance(img, Image.Image)
    True
    >>> img.width, img.height
    (31, 16)
    """
    # membuat ouput
    img = Image.new("RGB", (len(cells[0]), len(cells)))
    pixels = img.load()
    for w in range(img.width):
        for h in range(img.height):
            color = 255 - int(255 * cells[h][w])
            pixels[w, h] = (color, color, color)
    return img


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    rule_num = bin(int(input("input pada rule:").strip()))[2:]
    rule = format_ruleset(int(rule_num))
    for time in range(16):
        CELLS.append(new_generation(CELLS, rule, time))
    img = generate_image(CELLS)
    # img.save(f"rule_{rule_num}.png")
    img.show()
