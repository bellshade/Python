# Minimax membantu mencapai skor maksimum dalam permainan
# dengan memeriksa semua kemungkinan gerakan
# kedalaman adalah kedalaman saat ini di pohon permainan.

# nodeIndex adalah indeks dari node saat ini dalam skor[]
# jika langkah adalah pemaksimal, return True
# jika tidak return False
# informasi lebih lanjut tentang game tree
# https://en.wikipedia.org/wiki/Game_tree


from __future__ import annotations

def minimax(
    depth: int, node_index: int, is_max: bool, scores: list[int], height: float
) -> float:
    """
    >>> import math
    >>> scores = [90, 23, 6, 33, 21, 65, 123, 34432]
    >>> height = math.log(len(scores), 2)
    >>> minimax(0,0, True, scores, height)
    65
    >>> minimax(-1, 0, True, scores, height)
    Traceback (most recent call last):
    ...
    ValueError: Kedalaman tidak boleh kurang dari 0
    >>> minimax(0, 0, True, [], 2)
    Traceback (most recent call last):
    ...
    ValueError: Skor tidak boleh kosong
    >>> scores = [3, 5, 2, 9, 12, 5, 23, 23]
    >>> height = math.log(len(scores), 2)
    >>> minimax(0, 0, True, scores, height)
    12
    """
    if depth < 0:
        raise ValueError("Kedalaman tidak boleh kurang dari 0")

    if len(scores) == 0:
        raise ValueError("Skor tidak boleh kosong")

    if depth == height:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height),
        )

    return min(
        minimax(depth + 1, node_index * 2, True, scores, height),
        minimax(depth + 1, node_index * 2 + 1, True, scores, height),
    )


if __name__ == "__main__":
    import doctest

    # import math
    # scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    # height = math.log(len(scores), 2)
    # print("optimasi value :", end="")
    # print(minimax(0, 0, True, scores, height))
    doctest.testmod()
