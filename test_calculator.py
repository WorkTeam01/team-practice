"""Tests para el módulo calculator.

Pruebas básicas usando pytest.
Para correr los tests: pytest test_calculator.py
"""

import pytest
from calculator import add, subtract, multiply, divide, power, valor_maximo


def test_add():
    """Test suma básica."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 5) == 5


def test_subtract():
    """Test resta básica."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    """Test multiplicación básica."""
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0
    assert multiply(-2, 3) == -6


def test_divide():
    """Test división básica."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    """Test que división por cero lanza excepción."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_power():
    """Test potencia básica."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(4, 0.5) == 2.0


def test_valor_maximo():
    assert valor_maximo(10, 5) == 10
    assert valor_maximo(-2, 3) == 3
    assert valor_maximo(4, 4) == 4
    assert valor_maximo(-10, -5) == -5
