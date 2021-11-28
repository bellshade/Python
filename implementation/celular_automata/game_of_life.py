# implementasi game of life
# peraturan main game of life
# 1. setiap sel hdup kurang dari dua maka mati, seolah olah
# disebabkan oleh kekurangan populasi
# 2. setiap sel hidup dengan dua atau tiga orang hidup hidup
# ke generasi berikutnya
# 3. setiap sel hidup dengan lebih dari tiga orang hidup mati,
# seolah olah oleh populasi berlebihan
# 4. setiap sel mati dengan tepat tiga orang hidup menjadi sel hidup,
# seolah olah dengan reproduksi (repopulasi)

from __future__ import annotations
import random
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

usage_doc = "Usaage of script: script_nama <size_of_canvas:int>"

choice = [0] * 100 + [1] * 10
random.shuffle(choice)


def create_canvas(size: int) -> list[list[bool]]:
    """
    membuat canvas
    @param size: ukuran canvas = int
    @return: canvas = list[list[bool]]
    >>> create_canvas(2)
    [[False, False], [False, False]]
    """
    canvas = [[False for i in range(size)] for j in range(size)]
    return canvas


def seed(canvas: list[list[bool]]) -> None:
    for i, row in enumerate(canvas):
        for j, _ in enumerate(row):
            canvas[i][j] = bool(random.getrandbits(1))


def run(canvas: list[list[bool]]) -> list[list[bool]]:
    """
    fungsi ini menjalankan aturan permainan melalui semua poin
    dan mengubah status yang sesuai
    @param canvas: canvas = list[list[bool]]
    @return: canvas = list[list[bool]]
    >>> run([[False, False], [False, False]])
    [[False, False], [False, False]]
    """
    current_canvas = np.array(canvas)
    next_gen_canvas = np.array(create_canvas(current_canvas.shape[0]))
    for r, row in enumerate(current_canvas):
        for c, pt in enumerate(row):
            next_gen_canvas[r][c] = __judge_point(
                pt, current_canvas[r - 1 : r + 2, c - 1 : c + 2]
            )

    current_canvas = next_gen_canvas
    # bersihkan canvas (memori)
    del next_gen_canvas
    return_canvas: list[list[bool]] = current_canvas.tolist()

    return return_canvas


def __judge_point(pt: bool, neighbours: list[list[bool]]) -> bool:
    dead = 0
    alive = 0

    # menghitung jumlah hidup dan mati
    for i in neighbours:
        for status in i:
            if status:
                alive += 1
            else:
                dead += 1

    # penanganan entri duplikat untuk fokus pt
    if pt:
        alive -= 1
    else:
        dead -= 1

    # membuat peraturan dari game
    state = pt
    if pt:
        if alive < 2:
            state = False
        elif alive == 2 or alive == 3:
            state = True
        elif alive > 3:
            state = False
    else:
        if alive == 3:
            state = True

    return state


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    if len(sys.argv) != 2:
        raise Exception(usage_doc)

    canvas_size = int(sys.argv[1])

    c = create_canvas(canvas_size)
    seed(c)
    fig, ax = plt.subplots()
    fig.show()

    cmap = ListedColormap(["w", "k"])
    try:
        while True:
            c = run(c)
            ax.matshow(c, cmap=cmap)
            fig.canvas.draw()
            ax.cla()
    except KeyboardInterrupt:
        pass
