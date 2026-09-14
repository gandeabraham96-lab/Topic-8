import pytest
from validators import validate_age


def test_valid_age():
    assert validate_age(25) is True


def test_boundary_age():
    assert validate_age(120) is True


def test_invalid_age():
    with pytest.raises(ValueError):
        validate_age(121)