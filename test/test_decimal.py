from decimal import Decimal, getcontext


def test_1():
    a = Decimal(1)
    assert a == 1


def test_div_1_by_7():
    getcontext().prec=6
    a = Decimal(1)
    b = Decimal(7)
    c = a/b
    d = Decimal('0.142857')
    assert c == d


def test_div_1_by_7_long():
    getcontext().prec=24
    a = Decimal(1)
    b = Decimal(7)
    c = a/b
    d = Decimal('0.142857142857142857142857')
    assert c == d
