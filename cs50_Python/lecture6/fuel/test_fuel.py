import pytest
from fuel import convert, gauge

def test_errors():
    with pytest.raises(ValueError):
        convert('cat')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('4/3')

def test_convert():
    assert convert('1/2') == 50
    assert convert('3/4') == 75

def test_gauge():
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(75) == '75%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'