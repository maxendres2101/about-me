import pytest
from bank import value

def test_hello():
    assert value('hello, world') == 0
    assert value('Hello, world ') == 0

def test_h():
    assert value('help') == 20
    assert value('Help') == 20
    #assert value('helo') == 0

def test_otherwise():
    assert value('') == 100
    assert value('1234') == 100


