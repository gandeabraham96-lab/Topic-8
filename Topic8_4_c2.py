from grading import letter_grade


def test_39_is_f():
    assert letter_grade(39) == "F"


def test_40_is_c():
    assert letter_grade(40) == "C"


def test_59_is_c():
    assert letter_grade(59) == "C"


def test_60_is_b():
    assert letter_grade(60) == "B"


def test_79_is_b():
    assert letter_grade(79) == "B"


def test_80_is_a():
    assert letter_grade(80) == "A"