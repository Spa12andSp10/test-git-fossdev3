from script import sum, devide, mul

def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a, b) == result

def test_devide():
    a = 4
    b = 2
    result = 0.5
    assert devide(a, b) == result

def test_devison_problem():
    try:
        devide("A", "B")
        assert False
    except ValueError as e:
        print("Error!")

def test_mul():
    a = 4
    b = 9
    result = 36
    assert mul(a, b) == result

if __name__ == "__main__":
    test_devide() 
    test_sum()
    test_mul()
    test_devision_problem()
