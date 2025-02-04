import pytest
from twttr import shorten

def test_shorten():
    assert shorten('') == ''
    assert shorten('alphabet') == 'lphbt'
    assert shorten('Max') == 'Mx'

def test_exception():
    
