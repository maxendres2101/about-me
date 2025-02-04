import pytest
from numb3rs import validate

def test_negative():
    assert validate('-242.52.89.55') == False
    assert validate('-8.-100.-69.-5') == False

def test_inclusion():
    assert validate('254.254.254.254') == True
    assert validate('0.0.0.0') == True

def test_leadingzero():
    assert validate('023.025.25.023') == True

def test_limit():
    assert validate('256.257.355.258') == False
    assert validate('254.257.355.258') == False
    assert validate('253.254.355.258') == False
    assert validate('226.253.253.258') == False


def test_firstbyte():
    assert validate('255.0.0.0') == True

def test_letters():
    assert validate('abc.def.ghi.jkl') == False

def test_wrongSize():
    assert validate('12.13.234') == False
    assert validate('12.234.32.12.142') == False

def test_wrongChar():
    assert validate('12,25,68,25') == False


