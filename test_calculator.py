from calculator import add, subtract
import pytest
def test_add():
    test1 = add(1, 3)
    assert(test1 == 4)

    test2 = add(5.1, 5.4)
    assert(test2 == 10.5)

def test_subtract():
    test3 = subtract(10, 5)
    assert(test3 == 5)

    test4 = subtract(4, 6)
    assert(test4 == -2)

    test5 = subtract(2.5, 6.8)
    assert(test5 == -4.3)