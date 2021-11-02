# informasi tentang burrows wheeler
# https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform

from __future__ import annotations


def all_rotations(s: str) -> list[str]:
    """
    :param s: string akan berotasi sebanyak len(s).
    :return: rotiasi dari string.
    :raises TypeError: jika tidak sesuai dengan string.
    Contoh:
    >>> all_rotations("^BANANA|") # doctest: +NORMALIZE_WHITESPACE
    ['^BANANA|', 'BANANA|^', 'ANANA|^B', 'NANA|^BA', 'ANA|^BAN', 'NA|^BANA',
    'A|^BANAN', '|^BANANA']
    >>> all_rotations("a_asa_da_casa") # doctest: +NORMALIZE_WHITESPACE
    ['a_asa_da_casa', '_asa_da_casaa', 'asa_da_casaa_', 'sa_da_casaa_a',
    'a_da_casaa_as', '_da_casaa_asa', 'da_casaa_asa_', 'a_casaa_asa_d',
    '_casaa_asa_da', 'casaa_asa_da_', 'asaa_asa_da_c', 'saa_asa_da_ca',
    'aa_asa_da_cas']
    >>> all_rotations("panamabanana") # doctest: +NORMALIZE_WHITESPACE
    ['panamabanana', 'anamabananap', 'namabananapa', 'amabananapan',
    'mabananapana', 'abananapanam', 'bananapanama', 'ananapanamab',
    'nanapanamaba', 'anapanamaban', 'napanamabana', 'apanamabanan']
    >>> all_rotations(5)
    Traceback (most recent call last):
        ...
    TypeError: parameter harus berupa string.
    """
    if not isinstance(s, str):
        raise TypeError("parameter harus berupa string.")

    return [s[i:] + s[:i] for i in range(len(s))]


def bwt_transform(s: str) -> dict:
    """
    >>> bwt_transform("^BANANA")
    {'bwt_string': 'BNN^AAA', 'idx_ori_string': 6}
    >>> bwt_transform("a_asa_da_casa")
    {'bwt_string': 'aaaadss_c__aa', 'idx_ori_string': 3}
    >>> bwt_transform("panamabanana")
    {'bwt_string': 'mnpbnnaaaaaa', 'idx_ori_string': 11}
    >>> bwt_transform(4)
    Traceback (most recent call last):
    ...
    TypeError: parameter harus berupa string.
    >>> bwt_transform('')
    Traceback (most recent call last):
    ...
    ValueError: parameter s tidak boleh kosong.
    """
    if not isinstance(s, str):
        raise TypeError("parameter harus berupa string.")
    if not s:
        raise ValueError("parameter s tidak boleh kosong.")

    rotations = all_rotations(s)
    rotations.sort()

    return {
        "bwt_string": "".join([word[-1] for word in rotations]),
        "idx_ori_string": rotations.index(s),
    }


def reverse_bwt(bwt_string: str, idx_ori_string: int) -> str:
    """
    >>> reverse_bwt("BNN^AAA", 6)
    '^BANANA'
    >>> reverse_bwt("aaaadss_c__aa", 3)
    'a_asa_da_casa'
    >>> reverse_bwt("mnpbnnaaaaaa", 11)
    'panamabanana'
    >>> reverse_bwt(4, 11)
    Traceback (most recent call last):
    ...
    TypeError: Parameter bwt_string harus string.
    >>> reverse_bwt("", 11)
    Traceback (most recent call last):
    ...
    ValueError: Parameter bwt_string tidak boleh kosong.
    >>> reverse_bwt("mnpbnnaaaaaa", "asd") # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    ...
    TypeError: The parameter idx_ori_string harus bertipe int
    >>> reverse_bwt("mnpbnnaaaaaa", -1)
    Traceback (most recent call last):
    ...
    ValueError: Parameter idx_ori_string tidak boleh dibawah 0.
    >>> reverse_bwt("mnpbnnaaaaaa", 12) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    ...
    ValueError: Parameter idx_original_string tidak boleh dibawah len(bwt_string).
    >>> reverse_bwt("mnpbnnaaaaaa", 11.0)
    'panamabanana'
    >>> reverse_bwt("mnpbnnaaaaaa", 11.4)
    'panamabanana'
    """
    if not isinstance(bwt_string, str):
        raise TypeError("Parameter bwt_string harus string.")
    if not bwt_string:
        raise ValueError("Parameter bwt_string tidak boleh kosong.")
    try:
        idx_original_string = int(idx_ori_string)
    except ValueError:
        raise TypeError("The parameter idx_ori_string harus bertipe int")
    if idx_original_string < 0:
        raise ValueError("Parameter idx_ori_string tidak boleh dibawah 0.")
    if idx_original_string >= len(bwt_string):
        raise ValueError(
            "Parameter idx_original_string tidak boleh dibawah len(bwt_string)."
        )

    ordered_rotations = [""] * len(bwt_string)
    for x in range(len(bwt_string)):
        for i in range(len(bwt_string)):
            ordered_rotations[i] = bwt_string[i] + ordered_rotations[i]
        ordered_rotations.sort()
    return ordered_rotations[idx_original_string]


if __name__ == "__name__":
    import doctest

    # msg_info = "Berikan string yang akan hasilkan transformasi BWT-nya"
    # s = input(msg_info).strip()
    # result = bwt_transform(s)
    # print(
    #     f"Burrows wheeler untuk string {s} adalah "
    #     f"{result['bwt_string']}"
    # )

    doctest.testmod()
