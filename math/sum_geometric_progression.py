# penjelasan tentang sum of geometric progression
# https://www.cuemath.com/algebra/sum-of-a-gp/


def sum_geometric_progression(
    ist_pertama: int, rasio_umum: int, ist_bilangan: int
) -> float:
    """
    mengembalikan jumlah n suku dalam
    deret geometric
    >>> sum_geometric_progression(1, 2, 10)
    1023.0
    >>> sum_geometric_progression(1, 10, 5)
    11111.0
    >>> sum_geometric_progression(0, 2, 10)
    0.0
    """
    if rasio_umum == 1:
        # rumus untuk hasil jika rasio umum adalah 1
        return ist_bilangan * ist_pertama

    # rumus untuk menemukan hasil dari suku ke n dari
    # geometric progression
    return (ist_pertama / (1 - rasio_umum)) * (1 - rasio_umum ** ist_bilangan)
