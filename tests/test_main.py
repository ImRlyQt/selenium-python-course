def add_two_numbers(a, b):
    return a + b


def test_small_numbers():
    assert add_two_numbers(1, 2) == 30, "suma ma być 3"


def test_large_numbers():
    assert add_two_numbers(100, 300) == 400, "suma ma być 400"
