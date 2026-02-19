from script import sum, divide, mul, sub

def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a, b) == result

def test_divide():
    a = 4
    b = 2
    result = 0.5
    assert divide(a, b) == result

def test_devison_problem():
    try:
        divide("A", "B")
        assert False
    except ValueError as e:
        print("Error!")

def test_mul():
    a = 4
    b = 9
    result = 36
    assert mul(a, b) == result

def test_division_problem():
    try:
        divide([1,2,3], [1,2,3])
        return False
    except:
        print("All good!")

def test_sub():
    a = 5
    b = 3
    result = 2
    assert sub(a, b) == 2

if __name__ == "__main__":
    test_sum()
    test_mul()
    test_sub()
    test_divide()
