from src.main import compare_val


def test_compare_val1():
    assert compare_val(1, 1)


def test_compare_val2():
    assert not compare_val(1, 2)
