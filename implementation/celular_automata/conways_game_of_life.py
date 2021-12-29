# implementasi game of life pada python
# informasi lebih lanjut
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

from __future__ import annotations

from PIL import Image

GLIDER = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

BLINKER = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]


def new_generation(cells: list[list[int]]) -> list[list[int]]:
    """
    menghasilkan generasi berikutnya untuk kondisi
    tertentu dari game of life
    >>> new_generation(BLINKER)
    [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    """
    next_generation = []
    for i in range(len(cells)):
        next_generation_row = []
        for j in range(len(cells[i])):
            # melihat angka dari struktur yang masih hidup
            neighbour_count = 0
            if i > 0 and j > 0:
                neighbour_count += cells[i - 1][j - 1]
            if i > 0:
                neighbour_count += cells[i - 1][j]
            if i > 0 and j < len(cells[i]) - 1:
                neighbour_count += cells[i - 1][j + 1]
            if j > 0:
                neighbour_count += cells[i][j - 1]
            if j < len(cells[i]) - 1:
                neighbour_count += cells[i][j + 1]
            if i < len(cells) - 1 and j > 0:
                neighbour_count += cells[i + 1][j - 1]
            if i < len(cells) - 1:
                neighbour_count += cells[i + 1][j]
            if i < len(cells) - 1 and j < len(cells[i]) - 1:
                neighbour_count += cells[i + 1][j + 1]

            alive = cells[i][j] == 1
            if (
                (alive and 2 <= neighbour_count <= 3)
                or not alive
                and neighbour_count == 3
            ):
                next_generation_row.append(1)
            else:
                next_generation_row.append(0)

        next_generation.append(next_generation_row)

    return next_generation


def generate_image(cells: list[list[int]], frames: int) -> list[Image.Image]:
    # menghasilkan daftar gambar status game of life berikutnya
    images = []
    for _ in range(frames):
        # membuat output image
        img = Image.new("RGB", (len(cells[0]), len(cells)))
        pixels = img.load()

        # menyimpan cell ke dalam image yang dibuat
        for x in range(len(cells)):
            for y in range(len(cells[0])):
                colour = 255 - cells[y][x] * 255
                pixels[x, y] = (colour, colour, colour)

        # menyimpan gambar
        images.append(img)
        cells = new_generation(cells)

    return images


if __name__ == "__main__":
    import doctest

    images = generate_image(GLIDER, 16)
    images[0].save("hasil.gif", save_all=True, append_images=images[1:])

    doctest.testmod(verbose=True)