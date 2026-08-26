from two_sum import two_sum


def test_exemplo_basico():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_numeros_no_final_da_lista():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_numeros_repetidos():
    assert two_sum([3, 3], 6) == [0, 1]


def test_numeros_negativos():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
