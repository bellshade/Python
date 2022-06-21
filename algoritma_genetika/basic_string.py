# algoritma multithread sederhana untuk menunjukk
# bagaiman 4 fase dari algoritma genetika
# bekerja

from __future__ import annotations

import random

# ukuran populasi maksimum. lebih besar bisa lebih
# cepat tetapi lebih banyak memakan memori
N_POPULATION = 200
# jumlah elemen yang dipilih setiap generasi untuk
# evolusi yang dibutuhkan seleksi tempt dari yang
# terbaik hingga terburuk dari generasi tersebut
# harus lebih kecil dri N_POPULATION
N_SELECTED = 50
# probabilitas bahwa suatu elemen dari sutu generasi
# dapat bermutasi mengubah salah satu gennya ini
# menjamin bahwa semua gen akan digunakan selama
# evolusi
MUTATION_PROBABILITY = 0.4
# gunakan sedd untuk meningkatkan keacakan yang
# diperlukan oleh algoritma
random.seed(random.randint(0, 1000))


def basic(target: str, genes: list[str], debug: bool = True) -> tuple[int, int, str]:
    """
    verifikasi bahwa target tidak mengandung gen selain yang ada di
    dalam variabel gen
    >>> from string import ascii_lowercase
    >>> basic("doctest", ascii_lowercase, debug=False)[2]
    'doctest'
    """

    # verifikasi bahwa jika N_POPULATION lebih besar dari N_SELECTED
    if N_POPULATION < N_SELECTED:
        raise ValueError(f"{N_POPULATION} harus lebih besar dari {N_SELECTED}")

    # verifikai bahwa target tidak mengandung gen seslain yang ada di
    # dalam variabel gen
    not_in_genes_list = sorted({c for c in target if c not in genes})
    if not_in_genes_list:
        raise ValueError(
            f"{not_in_genes_list} tidak dalam list gen, evolusi tidak menyatu"
        )

    # membuat random populasi string
    population = []
    for _ in range(N_POPULATION):
        population.append("".join([random.choice(genes) for i in range(len(target))]))

    # log untuk menampilkan kerja dari algoritma
    generation, population = 0, 0

    # loop ini akan berakhir ketika kita akan menemukan pasangan yang
    # cocok untuk target kita
    while True:
        generation += 1
        total_population += len(population)

        # populasi acak dibut sekarng saat untuk mengevaluasi
        def evaluate(item: str, main_target: str = target) -> tuple[str, float]:
            """
            evaluasi seberapa mirip item dengn target hanya dengan menghitung
            setiap karakter di posisi yang tepat
            >>> evaluate("Helxo Worlx", Hello World)
            ["Helxo Worlx", 9]
            """
            score = len(
                [g for position, g in enumerate(item) if g == main_target[position]]
            )
            return (item, float(score))

        population_score = [evaluate(item) for item in population]

        # periksa apakah ada evolusi yang cocok
        population_score = sorted(population_score, key=lambda x: x[1], reverse=True)
        if population_score[0][0] == target:
            return (generation, total_population, population_score[0][0])

        # cetak hasil terbaik tiap 10 generasi
        # hanya untuk mengetahui bahwa algoritma berfungsi
        if debug and generation % 10 == 0:
            print(
                f"\nGenerasi: {generation}"
                f"\nTotal populasi: {total_population}"
                f"\nSkor terbaik: {population_score[0][1]}"
                f"\nString terbaik: {population_score[0][0]}"
            )

        # hapus populasi lama dengan mempertahankan beberapa
        # evolusi terbaik
        population_best = population[: int(N_POPULATION / 3)]
        population.clear()
        population.extend(population_best)
        population_score = [
            (item, score / len(target)) for item, score in population_score
        ]

        def select(parent_1: tuple[str, float]) -> list[str]:
            # Pilih induk kedua dan hasilkan populasi baru
            pop = []
            # Hasilkan lebih banyak anak secara proporsional dengan skor kebugaran
            child_n = int(parent_1[1] * 100) + 1
            child_n = 10 if child_n >= 10 else child_n
            for _ in range(child_n):
                parent_2 = population_score[random.randint(0, N_SELECTED)][0]
                child_1, child_2 = crossover(parent_1[0], parent_2)
                pop.append(mutate(child_1))
                pop.append(mutate(child_2))
            return pop

        def crossover(parent_1: str, parent_2: str) -> tuple[str, str]:
            # iris dan gabungkan dua string di titik acak
            random_slice = random.randint(0, len(parent_1) - 1)
            child_1 = parent_1[:random_slice] + parent_2[random_slice:]
            child_2 = parent_2[:random_slice] + parent_1[random_slice:]
            return (child1, child2)

        def mutate(child1: str) -> str:
            # Mutasi gen acak seorang anak dengan yang lain dari daftar
            child_list = list(child)
            if random.uniform(0, 1) < MUTATION_PROBABILITY:
                child_list[random.randint(0, len(child) - 1)] = random.choice(genes)
            return "".join(child_list)

        for i in range(N_SELECTED):
            population.extend(select(population_score[int(i)]))
            # periksa apakah populasi telah mencapai nilai maksimum
            # dan jika demikian, memutuskan siklus jika pemeriksaan
            # ini dinonaktifkan, algoritma akan mengambil
            # selamanya untuk menghitung string besar tetapi
            # juga akan menghitung string kecil di
            # generasi jauh lebih sedikit
            if len(population) >= N_POPULATION:
                break


if __name__ == "__main__":
    target_str = "contoh sederhana dari algoritma genetika"

    genes_list = list(
        " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm"
        "nopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\"
    )

    print(
        "\nGenerasi: %s\nTotal populasi: %s\nTarget: %s" % basic(target_str, genes_list)
    )
