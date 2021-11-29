# Simulasikan evolusi jalan
# raya dengan hanya satu jalan yaitu loop.
# Jalan raya dibagi dalam sel, setiap sel dapat
# memiliki paling banyak satu mobil di dalamnya.
# Jalan raya adalah lingkaran sehingga ketika
# sebuah mobil datang ke satu ujung,
# itu akan keluar di ujung yang lain.
# Setiap mobil diwakili oleh kecepatannya (dari 0 hingga 5).

# Beberapa informasi tentang kecepatan:
# -1 berarti sel di jalan raya kosong
# 0 hingga 5 adalah kecepatan mobil
# dengan 0 terendah dan 5 tertinggi

# jalan raya: list[int] Di mana setiap
# posisi dan kecepatan setiap mobil akan disimpan

# Probabilitas Probabilitas bahwa seorang
# pengemudi akan melambat

# initial_speed Kecepatan mobil saat start

# frekuensi Berapa banyak sel
# yang ada di antara dua mobil di awal?

# max_speed Kecepatan maksimum yang dapat dicapai mobil
# number_of_cells Berapa banyak sel yang ada di jalan raya
# number_of_update Berapa kali posisi akan diperbarui

# informasi lebih lanjut
# jalan raya: list[int] Di mana setiap
# posisi dan kecepatan setiap mobil akan disimpan

# informasi lebih lanjut
# https://en.wikipedia.org/wiki/Nagel%E2%80%93Schreckenberg_model

from __future__ import annotations

from random import randint, random


def construct_highway(
    number_of_cells: int,
    frequency: int,
    initial_speed: int,
    random_frequency: bool = False,
    random_speed: bool = False,
    max_speed: int = 5,
) -> list:
    """
    membuat jalan raya dengan mengikuti parameter
    >>> construct_highway(10, 2, 6)
    [[6, -1, 6, -1, 6, -1, 6, -1, 6, -1]]
    """

    # membuat jalan tanpa ada kendaraan
    highway = [[-1] * number_of_cells]
    i = 0
    if initial_speed < 0:
        initial_speed = 0
    while i < number_of_cells:
        # menamruh kendaran
        highway[0][i] = randint(0, max_speed) if random_speed else initial_speed
        i += randint(1, max_speed * 2) if random_frequency else frequency
    return highway


def get_distance(highway_now: list, car_index: int) -> int:
    """
    membuat jarak antara kendaraan dan kendaraan selanjutnya
    >>> get_distance([6, -1, 6, -1, 6], 2)
    1
    """
    distance = 0
    cells = highway_now[car_index + 1 :]
    for cell in range(len(cells)):
        if cells[cell] != -1:
            return distance
        distance += 1
    return distance + get_distance(highway_now, -1)


def update(highway_now: list, probability: float, max_speed: int) -> list:
    """
    update dari kecepatan kendaraan
    >>> update([-1, -1, -1, -1, -1, 2, -1, -1, -1, -1, 3], 0.0, 5)
    [-1, -1, -1, -1, -1, 3, -1, -1, -1, -1, 4]
    >>> update([-1, -1, 2, -1, -1, -1, -1, 3], 0.0, 5)
    [-1, -1, 3, -1, -1, -1, -1, 1]
    """
    number_of_cells = len(highway_now)

    # sebelum kalkulasi
    next_highway = [-1] * number_of_cells

    for car_index in range(number_of_cells):
        if highway_now[car_index] != -1:
            # menambahkan 1 dari kecepatan sekarang kendaraan
            next_highway[car_index] = min(highway_now[car_index] + 1, max_speed)
            # jumlah dari sel yang kosong sebelum masuk kendaraan
            dn = get_distance(highway_now, car_index) - 1
            next_highway[car_index] = min(next_highway[car_index], dn)
            if random() < probability:
                # mengacak, kendaraa mencoba melambat
                next_highway[car_index] = max(next_highway[car_index] - 1, 0)

    return next_highway


def simulasi(
    highway: list,
    number_of_update: int,
    probability: float,
    max_speed: int,
) -> list:
    """
    >>> simulasi([[-1, 2, -1, -1, -1, 3]], 2, 0.0, 3)
    [[-1, 2, -1, -1, -1, 3], [-1, -1, -1, 2, -1, 0], [1, -1, -1, 0, -1, -1]]
    >>> simulasi([[-1, 2, -1, 3]], 4, 0.0, 3)
    [[-1, 2, -1, 3], [-1, 0, -1, 0], [-1, 0, -1, 0], [-1, 0, -1, 0], [-1, 0, -1, 0]]
    """
    number_of_cells = len(highway[0])

    for i in range(number_of_update):
        next_speeds_calculated = update(highway[i], probability, max_speed)
        real_next_speeds = [-1] * number_of_cells

        for car_index in range(number_of_cells):
            speed = next_speeds_calculated[car_index]
            if speed != -1:
                # mengganti posisi berdasarkan kecepatan
                index = (car_index + speed) % number_of_cells
                # commit merubah posisi
                real_next_speeds[index] = speed
        highway.append(real_next_speeds)

    return highway


if __name__ == "__main__":
    import doctest

    doctest.testmod()
