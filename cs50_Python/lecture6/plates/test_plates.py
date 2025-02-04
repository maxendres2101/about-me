import pytest
from plates import is_valid
#, find_first_digit

def test_length():
    assert is_valid('a') == False
    assert is_valid('abcdefg') == False
    assert is_valid('abcd') == True

def test_first_number():
    assert is_valid('ab2cd') == False
    assert is_valid('21234') == False

def test_special_characters():
    assert is_valid('ab.cd') == False
    assert is_valid('ab dc') == False