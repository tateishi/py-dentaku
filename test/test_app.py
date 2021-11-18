def test_1():
    a = 1
    b = 1
    assert a == b


def test_2():
    a = 1
    b = 2
    assert a != b



def test_is_prime():
    from dentaku.lib import is_prime
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)
