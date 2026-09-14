import pytest
from grading import letter_grade


def test_invalid_score():
    with pytest.raises(ValueError):
        letter_grade(150)