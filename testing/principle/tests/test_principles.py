import sys
sys.path.append("../scr")

from math_demo import add, add_with_bug, tax_calculator_bugged, tax_calculator

def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 6) == 13
    print("Test Addition passed")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    #assert add_with_bug(7, 6) == 13
    print("Test bugged Addition passed")

def test_addition_dublicate():
    assert add(6, 7) == 6 + 7
    print("Test Duplicate Addition passed")

def test_addition_overkill():
    for i in range(0, 2 ** 32):
        for j in range(0, 2 ** 32):
            assert add(i, j) == i + j
            assert add(i, j) == -i + j
            assert add(-i, -j) == -i - j
            assert add(i, -j) == i - j

def test_addition_clasters():
    assert add(7, 6) == 13
    assert add(7, 0) == 7
    assert add(0, 0) == 0
    assert add(10, -11) == -1
    assert add(-10, -11) == -21
    assert add(-5, 0) == -5
    assert add(0, -2) == -2
    assert add(9, 5) == 14
    assert add(5, 9) == 14
    print("test clasters passed")

def test_addition_commutative():
    assert add(9, 5) == 14
    assert add(5, 9) == 14
    print("test commutative passed")

def test_tax_calculator_pesticide():
    assert tax_calculator_bugged(1000) == 150
    assert tax_calculator_bugged(100) == 15
    assert tax_calculator_bugged(10) == 1.5
    assert tax_calculator_bugged(1) == 0.15
    assert tax_calculator_bugged(234) == 35.1
    print("Test tax calculator pesticide passed")
    #assert tax_calculator_bugged(2.34) == 0.35

def test_tax_calculator():
    assert tax_calculator(1000) == 150
    assert tax_calculator(100) == 15
    assert tax_calculator(10) == 1.5
    assert tax_calculator(1) == 0.15
    assert tax_calculator(234) == 35.1
    assert tax_calculator(2.34) == 0.35
    print("Test tax calculator passed")

def test_negative_income():
    try:
        tax_calculator(-100)
        print("Test negative income failed")
    except ValueError as ve:
        print("Test negative income passed")

if __name__ == '__main__':
    test_addition()
    test_addition_with_bug()
    test_addition_dublicate()
    #test_addition_overkill()
    test_addition_clasters()
    test_addition_commutative()
    test_tax_calculator_pesticide()
    test_tax_calculator()
    test_negative_income()