"""Calculadora básica para demostrar prácticas de desarrollo colaborativo.

Este módulo contiene funciones matemáticas simples para practicar:
- Escritura de código limpio
- Documentación de funciones
- Testing
- Code reviews
"""


def add(a: float, b: float) -> float:
    """Suma dos números.
    
    Args:
        a: Primer número
        b: Segundo número
        
    Returns:
        La suma de a y b
        
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Resta dos números.
    
    Args:
        a: Primer número (minuendo)
        b: Segundo número (sustraendo)
        
    Returns:
        La diferencia de a menos b
        
    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(0, 5)
        -5
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplica dos números.
    
    Args:
        a: Primer número
        b: Segundo número
        
    Returns:
        El producto de a y b
        
    Examples:
        >>> multiply(4, 3)
        12
        >>> multiply(-2, 5)
        -10
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide dos números.
    
    Args:
        a: Dividendo
        b: Divisor
        
    Returns:
        El cociente de a dividido por b
        
    Raises:
        ZeroDivisionError: Si b es igual a 0
        
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Eleva un número a una potencia.
    
    Args:
        base: Número base
        exponent: Exponente
        
    Returns:
        El resultado de base elevado a exponent
        
    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
    """
    return base ** exponent

def valor_maximo(a: float, b: float) -> float:
    """Devuelve el número mayor entre dos valores.

    Args:
        a: Primer número
        b: Segundo número

    Returns:
        El número mayor entre a y b

    Examples:
        >>> valor_maximo(10, 5)
        10
        >>> valor_maximo(-2, 3)
        3
        >>> valor_maximo(4, 4)
        4
    """
    return a if a > b else b

def valor_minimo(a: float, b: float) -> float:
    """Devuelve el número menor entre dos valores.

    Args:
        a: Primer número
        b: Segundo número

    Returns:
        El número menor entre a y b

    Examples:
        >>> valor_minimo(10, 5)
        5
        >>> valor_minimo(-2, 3)
        -2
        >>> valor_minimo(4, 4)
        4
    """
    return a if a < b else b
  
  
def abs_value(a: float) -> float:
    """Devuelve el módulo de un número.
    Args:
        a: Número del cual obtener el valor absoluto
    Returns:
        El valor absoluto de a
    Examples:
        >>> abs_value(-5)
        5
        >>> abs_value(3)
        3 
    """
    return abs(a)
