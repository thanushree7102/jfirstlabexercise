from p1 import calculate_total
from p2 import calculate_grade


def test_total():
    assert calculate_total(80, 80, 80) == 240


def test_grade():
    assert calculate_grade(270) == "A"
    assert calculate_grade(240) == "B"
    assert calculate_grade(180) == "C"