import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def tets_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪'
    jar.deposit(4)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        assert jar.deposit(12) == 'Jar is too small'

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size == 8
    with pytest.raises(ValueError):
        assert jar.withdraw(11) == 'There are too few cookies inside the Jar'

def test_capacity():
    jar = Jar(2)
    with pytest.raises(ValueError):
        assert jar.deposit(3) == 'Jar is too small'
