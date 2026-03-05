import sys
sys.path.append("../scr")

from math_demo import add, add_with_bug

def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 6) == 13
    print("Test Addition past")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    #assert add_with_bug(7, 6) == 13
    print("Test bugged Addition past")

if __name__ == '__main__':
    test_addition()
    test_addition_with_bug()