import pytest
from um import count

def test_surrounded():
    assert count('yummuy') == 0
    assert count('umbles') == 0
    assert count('forum') == 0

def test_case():
    assert count('hello um world') == 1
    assert count('hello Um world') == 1
    assert count('hello uM world') == 1
    assert count('hello UM world') == 1

def test_valide():
    assert count(' um, ') == 1
