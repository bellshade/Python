# Algoritma multithreaded sederhana
# untuk menunjukkan bagaimana
# 4 fase dari algoritma genetika bekerja

from __future__ import annotations

import random

# ukuran maksimal population, bisa besar, lebih cepat tapi memory feed
N_POPULATION = 200
# Jumlah elemen yang dipilih di setiap generasi
# untuk evolusi yang dibutuhkan seleksi
N_SELECTED = 50
MUTATION_PROBABILITY = 0.4

random.seed(random.randint(0, 1000))


def getbasic(target: str, genes: list[str], debug: bool = True) -> tuple[int, int, str]:
    """
    Verifikasi bahwa target tidak mengandung gen
    selain yang ada di dalam variabel gen.
    >>> from string import ascii_lowercase
    >>> getbasic("makan", ascii_lowercase, debug=False)[2]
    'makan'
    >>> gen = list(ascii_lowercase)
    >>> gen.remove("e")
    >>> getbasic("jennie", gen)
    Traceback (most recent call last):
    ...
    ValueError: ['e'] tidak ada dalam daftar, evolusi tidak dapat menyatu
    """
    # validasi jika N_POPULATION lebih besar dari N_SELECTED
    if N_POPULATION < N_SELECTED:
        raise ValueError(f"{N_POPULATION} harus lebih besar dari {N_SELECTED}")
    not_in_genes_list = sorted({c for c in target if c not in genes})
    if not_in_genes_list:
        raise ValueError(
            f"{not_in_genes_list} tidak ada dalam daftar, evolusi tidak dapat menyatu"
        )
    # buat random start population
    population = []
    for _ in range(N_POPULATION):
        population.append("".join([random.choice(genes) for i in range(len(target))]))

    # log untuk melihat kerja dari algoritma
    generation, total_population = 0, 0

    # Loop ini akan berakhir ketika kita akan menemukan
    # pasangan yang cocok untuk target kita
    while True:
        generation += 1
        total_population += len(population)

        # evaluasi dari random population yang sudah dibuat
        def evaluate(item: str, main_target: str = target) -> tuple[str, float]:
            """
            Evaluasi seberapa mirip item dengan target hanya dengan
            menghitung setiap karakter di posisi yang tepat
            >>> evaluate("Helxo worlx", hello world)
            ["Helxo Worlx", 9]
            """
            score = len(
                [g for position, g in enumerate(item) if g == main_target[position]]
            )
            return (item, float(score))

        population_score = [evaluate(item) for item in population]

        # mengecek jika ada evolusinya yang cocok
        population_score = sorted(population_score, key=lambda x: x[1], reverse=True)
        if population_score[0][0] == target:
            return (generation, total_population, population_score[0][0])

        # print hasil terbaiknya tiap 10 generasi
        if debug and generation % 10 == 0:
            print(
                f"\nGenerasi : {generation}"
                f"\nTotal populasi: {total_population}"
                f"\nskor: {population_score[0][1]}"
                f"\nstring: {population_score[0][0]}"
            )
        population_best = population[: int(N_POPULATION / 3)]
        population.clear()
        population.extend(population_best)

        # Normalisasi skor populasi dari 0 hingga 1
        population_score = [
            (item, score / len(target)) for item, score in population_score
        ]

        def select(parent_1: tuple[str, float]) -> list[str]:
            """
            Pilih parent kedua dan hasilkan populasi baru
            """
            popula = []
            child_n = int(parent_1[1] * 100) + 1
            child_n = 10 if child_n >= 10 else child_n
            for _ in range(child_n):
                parent_2 = population_score[random.randint(0, N_SELECTED)][0]
                child_1, child_2 = crossover(parent_1[0], parent_2)

                popula.append(mutate(child_1))
                popula.append(mutate(child_1))

            return popula

        def crossover(parent_1: str, parent_2: str) -> tuple[str, str]:
            """
            Slice    dan gabungkan dua string di titik acak
            """
            random_slice = random.randint(0, len(parent_1) - 1)
            child_1 = parent_1[:random_slice] + parent_2[random_slice:]
            child_2 = parent_2[:random_slice] + parent_1[random_slice:]

            return (child_1, child_2)

        def mutate(child: str) -> str:
            child_list = list(child)
            if random.uniform(0, 1) < MUTATION_PROBABILITY:
                child_list[random.randint(0, len(child) - 1)] = random.choice(genes)

            return "".join(child_list)

        for i in range(N_SELECTED):
            population.extend(select(population_score[int(i)]))
            # Periksa apakah populasi sudah mencapai nilai maksimum dan jika ya
            # memutuskan siklus. jika pemeriksaan ini dinonaktifkan,
            # algoritma akan mengambil
            # selamanya untuk menghitung string besar tetapi
            # juga akan menghitung string kecil di
            # generasi jauh lebih sedikit
            if len(population) > N_POPULATION:
                break


if __name__ == "__main__":
    import doctest

    target_str = "saya pergi ke pasar"
    genes_list = list(
        " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm"
        "nopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\"
    )
    print(
        "\nGenerasi: %s\nTotal Populasi: %s\nTarget: %s"
        % getbasic(target_str, genes_list)
    )
    doctest.testmod()
