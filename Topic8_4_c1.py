from string_ops import is_palindrome


def test_palindrome():
    assert is_palindrome("madam") is True


def test_non_palindrome():
    assert is_palindrome("hello") is False