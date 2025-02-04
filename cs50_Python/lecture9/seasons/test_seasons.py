import pytest
from seasons import convert

def test_format():
    assert convert('1999-01-01') == 'Thirteen million, one hundred twenty-nine thousand, nine hundred twenty'
