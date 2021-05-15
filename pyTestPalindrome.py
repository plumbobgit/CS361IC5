import pytest
import palindrome


def test_palindromeness():
    value = palindrome.is_palindrome('racecar')
    assert value == True


def test_notpalindromeness():
    value = palindrome.is_palindrome('hello')
    assert value == False
