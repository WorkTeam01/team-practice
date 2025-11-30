"""Tests para la interfaz gráfica de la calculadora.

Pruebas usando pytest para verificar funcionalidad de GUI.
Para correr los tests: pytest test_gui_calculator.py -v
"""
import tkinter as tk
from gui import CalculatorGUI


# ============================================================================
# TESTS BÁSICOS
# ============================================================================

def test_initial_state():
    """Test del estado inicial de la calculadora."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    assert calc.current_value == ""
    assert calc.operator is None
    assert calc.first_number is None

    root.destroy()


def test_number_button_click():
    """Test de clicks en botones numéricos: simples y múltiples."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: Un solo dígito
    calc.number_button_click("5")
    assert calc.current_value == "5"

    # Caso 2: Múltiples dígitos
    calc.number_button_click("3")
    calc.number_button_click("7")
    assert calc.current_value == "537"

    calc.clear_click()

    # Caso 3: Ceros al inicio
    calc.number_button_click("0")
    calc.number_button_click("0")
    calc.number_button_click("5")
    assert calc.current_value == "005"

    root.destroy()


def test_decimal_click():
    """Test del botón de punto decimal."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: Decimal con número
    calc.number_button_click("3")
    calc.decimal_click()
    calc.number_button_click("5")
    assert calc.current_value == "3.5"

    calc.clear_click()

    # Caso 2: Solo permite un punto decimal
    calc.number_button_click("3")
    calc.decimal_click()
    calc.number_button_click("5")
    calc.decimal_click()  # Este no debería agregarse
    assert calc.current_value == "3.5"
    assert calc.current_value.count(".") == 1

    calc.clear_click()

    # Caso 3: Decimal sin número (debe agregar 0)
    calc.decimal_click()
    assert calc.current_value == "0."

    root.destroy()


def test_clear_click():
    """Test del botón clear (C)."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Configurar estado con valores
    calc.number_button_click("5")
    calc.operation_click("+")
    calc.number_button_click("3")

    # Limpiar todo
    calc.clear_click()

    assert calc.current_value == ""
    assert calc.operator is None
    assert calc.first_number is None

    root.destroy()


def test_backspace_click():
    """Test del botón backspace (⌫)."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: Borrar dígitos normales
    calc.number_button_click("1")
    calc.number_button_click("2")
    calc.number_button_click("3")
    calc.backspace_click()
    assert calc.current_value == "12"

    calc.backspace_click()
    assert calc.current_value == "1"

    # Caso 2: Backspace con display vacío
    calc.clear_click()
    calc.backspace_click()
    assert calc.current_value == ""

    # Caso 3: Borrar número negativo
    calc.operation_click("-")
    calc.number_button_click("5")
    calc.backspace_click()
    assert calc.current_value == "-"

    root.destroy()


def test_gui_structure():
    """Test de que los componentes GUI se crean correctamente."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Verificar que el display existe
    assert calc.display is not None

    # Verificar título de ventana
    assert calc.root.title() == "Calculadora"

    root.destroy()


# ============================================================================
# TESTS DE OPERACIONES BÁSICAS
# ============================================================================

def test_suma():
    """Test de operación suma: positivos, negativos y mixtos."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: Suma básica positiva: 5 + 3 = 8
    calc.number_button_click("5")
    calc.operation_click("+")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == 8.0

    calc.clear_click()

    # Caso 2: Suma con negativo: -5 + 3 = -2
    calc.operation_click("-")
    calc.number_button_click("5")
    calc.operation_click("+")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == -2.0

    calc.clear_click()

    # Caso 3: Suma de dos negativos: -5 + (-3) = -8
    calc.operation_click("-")
    calc.number_button_click("5")
    calc.operation_click("+")
    calc.operation_click("-")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == -8.0

    calc.clear_click()

    # Caso 4: Suma con cero: 0 + 5 = 5
    calc.number_button_click("0")
    calc.operation_click("+")
    calc.number_button_click("5")
    calc.equals_click()
    assert float(calc.current_value) == 5.0

    root.destroy()


def test_resta():
    """Test de operación resta: positivos, negativos y mixtos."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: Resta básica: 10 - 4 = 6
    calc.number_button_click("1")
    calc.number_button_click("0")
    calc.operation_click("-")
    calc.number_button_click("4")
    calc.equals_click()
    assert float(calc.current_value) == 6.0

    calc.clear_click()

    # Caso 2: Resta que resulta en negativo: 3 - 10 = -7
    calc.number_button_click("3")
    calc.operation_click("-")
    calc.number_button_click("1")
    calc.number_button_click("0")
    calc.equals_click()
    assert float(calc.current_value) == -7.0

    calc.clear_click()

    # Caso 3: Resta con negativo: -5 - 3 = -8
    calc.operation_click("-")
    calc.number_button_click("5")
    calc.operation_click("-")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == -8.0

    calc.clear_click()

    # Caso 4: Resta de negativos: 5 - (-3) = 8
    calc.number_button_click("5")
    calc.operation_click("-")
    calc.operation_click("-")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == 8.0

    root.destroy()


def test_multiplicacion():
    """Test de operación multiplicación: positivos, negativos y cero."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: Multiplicación básica: 7 * 6 = 42
    calc.number_button_click("7")
    calc.operation_click("*")
    calc.number_button_click("6")
    calc.equals_click()
    assert float(calc.current_value) == 42.0

    calc.clear_click()

    # Caso 2: Multiplicación por cero: 5 * 0 = 0
    calc.number_button_click("5")
    calc.operation_click("*")
    calc.number_button_click("0")
    calc.equals_click()
    assert float(calc.current_value) == 0.0

    calc.clear_click()

    # Caso 3: Negativo * positivo: -2 * 3 = -6
    calc.operation_click("-")
    calc.number_button_click("2")
    calc.operation_click("*")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == -6.0

    calc.clear_click()

    # Caso 4: Negativo * negativo: -2 * -3 = 6
    calc.operation_click("-")
    calc.number_button_click("2")
    calc.operation_click("*")
    calc.operation_click("-")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == 6.0

    root.destroy()


def test_division():
    """Test de operación división: positivos, negativos y error."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: División básica: 15 / 3 = 5
    calc.number_button_click("1")
    calc.number_button_click("5")
    calc.operation_click("/")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == 5.0

    calc.clear_click()

    # Caso 2: División con decimales: 10 / 4 = 2.5
    calc.number_button_click("1")
    calc.number_button_click("0")
    calc.operation_click("/")
    calc.number_button_click("4")
    calc.equals_click()
    assert float(calc.current_value) == 2.5

    calc.clear_click()

    # Caso 3: División negativo/positivo: -10 / 2 = -5
    calc.operation_click("-")
    calc.number_button_click("1")
    calc.number_button_click("0")
    calc.operation_click("/")
    calc.number_button_click("2")
    calc.equals_click()
    assert float(calc.current_value) == -5.0

    calc.clear_click()

    # Caso 4: División positivo/negativo: 10 / -2 = -5
    calc.number_button_click("1")
    calc.number_button_click("0")
    calc.operation_click("/")
    calc.operation_click("-")
    calc.number_button_click("2")
    calc.equals_click()
    assert float(calc.current_value) == -5.0

    root.destroy()


def test_potencia():
    """Test de operación potencia: positivos y negativos."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: Potencia básica: 2 ^ 3 = 8
    calc.number_button_click("2")
    calc.operation_click("^")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == 8.0

    calc.clear_click()

    # Caso 2: Potencia con base negativa: -2 ^ 3 = -8
    calc.operation_click("-")
    calc.number_button_click("2")
    calc.operation_click("^")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == -8.0

    calc.clear_click()

    # Caso 3: Potencia decimal (raíz): 4 ^ 0.5 = 2
    calc.number_button_click("4")
    calc.operation_click("^")
    calc.number_button_click("0")
    calc.decimal_click()
    calc.number_button_click("5")
    calc.equals_click()
    assert float(calc.current_value) == 2.0

    calc.clear_click()

    # Caso 4: Potencia a cero: 5 ^ 0 = 1
    calc.number_button_click("5")
    calc.operation_click("^")
    calc.number_button_click("0")
    calc.equals_click()
    assert float(calc.current_value) == 1.0

    root.destroy()


# ============================================================================
# TESTS DE FUNCIONES CIENTÍFICAS
# ============================================================================

def test_valor_absoluto():
    """Test de valor absoluto: negativos, positivos y cero."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: abs de negativo: abs(-5) = 5
    calc.operation_click("-")
    calc.number_button_click("5")
    calc.scientific_click("abs")
    assert float(calc.current_value) == 5.0

    calc.clear_click()

    # Caso 2: abs de positivo: abs(3) = 3
    calc.number_button_click("3")
    calc.scientific_click("abs")
    assert float(calc.current_value) == 3.0

    calc.clear_click()

    # Caso 3: abs de decimal negativo: abs(-2.5) = 2.5
    calc.operation_click("-")
    calc.number_button_click("2")
    calc.decimal_click()
    calc.number_button_click("5")
    calc.scientific_click("abs")
    assert float(calc.current_value) == 2.5

    calc.clear_click()

    # Caso 4: abs de cero: abs(0) = 0
    calc.number_button_click("0")
    calc.scientific_click("abs")
    assert float(calc.current_value) == 0.0

    root.destroy()


def test_valor_maximo():
    """Test de valor máximo: positivos, negativos y mixtos."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: max de positivos: max(10, 20) = 20
    calc.number_button_click("1")
    calc.number_button_click("0")
    calc.scientific_click("max")
    calc.number_button_click("2")
    calc.number_button_click("0")
    calc.equals_click()
    assert float(calc.current_value) == 20.0

    calc.clear_click()

    # Caso 2: max con negativos: max(-5, -10) = -5
    calc.operation_click("-")
    calc.number_button_click("5")
    calc.scientific_click("max")
    calc.operation_click("-")
    calc.number_button_click("1")
    calc.number_button_click("0")
    calc.equals_click()
    assert float(calc.current_value) == -5.0

    calc.clear_click()

    # Caso 3: max negativo y positivo: max(-2, 3) = 3
    calc.operation_click("-")
    calc.number_button_click("2")
    calc.scientific_click("max")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == 3.0

    calc.clear_click()

    # Caso 4: max de iguales: max(4, 4) = 4
    calc.number_button_click("4")
    calc.scientific_click("max")
    calc.number_button_click("4")
    calc.equals_click()
    assert float(calc.current_value) == 4.0

    root.destroy()


def test_valor_minimo():
    """Test de valor mínimo: positivos, negativos y mixtos."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: min de positivos: min(10, 20) = 10
    calc.number_button_click("1")
    calc.number_button_click("0")
    calc.scientific_click("min")
    calc.number_button_click("2")
    calc.number_button_click("0")
    calc.equals_click()
    assert float(calc.current_value) == 10.0

    calc.clear_click()

    # Caso 2: min con negativos: min(-5, -10) = -10
    calc.operation_click("-")
    calc.number_button_click("5")
    calc.scientific_click("min")
    calc.operation_click("-")
    calc.number_button_click("1")
    calc.number_button_click("0")
    calc.equals_click()
    assert float(calc.current_value) == -10.0

    calc.clear_click()

    # Caso 3: min negativo y positivo: min(-2, 3) = -2
    calc.operation_click("-")
    calc.number_button_click("2")
    calc.scientific_click("min")
    calc.number_button_click("3")
    calc.equals_click()
    assert float(calc.current_value) == -2.0

    calc.clear_click()

    # Caso 4: min de iguales: min(7, 7) = 7
    calc.number_button_click("7")
    calc.scientific_click("min")
    calc.number_button_click("7")
    calc.equals_click()
    assert float(calc.current_value) == 7.0

    root.destroy()


# ============================================================================
# TESTS DE CASOS EXTREMOS Y ERRORES
# ============================================================================

def test_division_por_cero():
    """Test de división por cero: debe mostrar error."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    calc.number_button_click("5")
    calc.operation_click("/")
    calc.number_button_click("0")
    calc.equals_click()

    # Después del error, debería limpiar el estado
    assert calc.current_value == ""
    assert calc.operator is None
    assert calc.first_number is None

    root.destroy()


def test_operaciones_consecutivas():
    """Test de operaciones encadenadas sin presionar igual."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # 5 + 3 + 2 = 10 (presionando + después de 3 debe calcular 5+3)
    calc.number_button_click("5")
    calc.operation_click("+")
    calc.number_button_click("3")
    calc.operation_click("+")  # Debe calcular 5+3=8 primero
    calc.number_button_click("2")
    calc.equals_click()

    assert float(calc.current_value) == 10.0

    root.destroy()


def test_decimales():
    """Test de operaciones con decimales: positivos y negativos."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: Suma con decimales: 5.5 + 2.3 = 7.8
    calc.number_button_click("5")
    calc.decimal_click()
    calc.number_button_click("5")
    calc.operation_click("+")
    calc.number_button_click("2")
    calc.decimal_click()
    calc.number_button_click("3")
    calc.equals_click()
    result = float(calc.current_value)
    assert abs(result - 7.8) < 0.0001

    calc.clear_click()

    # Caso 2: Multiplicación con decimal negativo: -2.5 * 2 = -5
    calc.operation_click("-")
    calc.number_button_click("2")
    calc.decimal_click()
    calc.number_button_click("5")
    calc.operation_click("*")
    calc.number_button_click("2")
    calc.equals_click()
    assert float(calc.current_value) == -5.0

    calc.clear_click()

    # Caso 3: División con decimales: 10.5 / 2 = 5.25
    calc.number_button_click("1")
    calc.number_button_click("0")
    calc.decimal_click()
    calc.number_button_click("5")
    calc.operation_click("/")
    calc.number_button_click("2")
    calc.equals_click()
    assert float(calc.current_value) == 5.25

    root.destroy()


def test_numeros_negativos():
    """Test de manejo de números negativos al inicio."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # Caso 1: Ingresar número negativo directamente: -5
    calc.operation_click("-")
    calc.number_button_click("5")
    assert calc.current_value == "-5"

    calc.clear_click()

    # Caso 2: Número negativo decimal: -3.14
    calc.operation_click("-")
    calc.number_button_click("3")
    calc.decimal_click()
    calc.number_button_click("1")
    calc.number_button_click("4")
    assert calc.current_value == "-3.14"

    calc.clear_click()

    # Caso 3: Solo signo menos (incompleto) + abs debe dar error
    calc.operation_click("-")
    calc.scientific_click("abs")
    # Debe mostrar error
    assert calc.current_value == ""

    root.destroy()


def test_equals_sin_operacion():
    """Test de presionar = sin operación previa."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    calc.number_button_click("5")
    calc.equals_click()

    # No debería crashear, mantiene el número
    assert calc.current_value == "5"

    root.destroy()


def test_equals_sin_segundo_numero():
    """Test de presionar = sin segundo número."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    calc.number_button_click("5")
    calc.operation_click("+")
    calc.equals_click()

    # Debería mostrar error y limpiar
    assert calc.current_value == ""

    root.destroy()


def test_resultado_como_operando():
    """Test de usar resultado en nueva operación: (5 + 3) * 2 = 16."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # 5 + 3 = 8
    calc.number_button_click("5")
    calc.operation_click("+")
    calc.number_button_click("3")
    calc.equals_click()

    # 8 * 2 = 16
    calc.operation_click("*")
    calc.number_button_click("2")
    calc.equals_click()

    assert float(calc.current_value) == 16.0

    root.destroy()


def test_clear_durante_operacion():
    """Test de limpiar en medio de una operación."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    calc.number_button_click("5")
    calc.operation_click("+")
    calc.number_button_click("3")
    calc.clear_click()

    # Todo debería estar limpio
    assert calc.current_value == ""
    assert calc.operator is None
    assert calc.first_number is None

    root.destroy()


def test_numeros_grandes():
    """Test con números grandes."""
    root = tk.Tk()
    calc = CalculatorGUI(root)

    # 99999 * 99999 = 9999800001
    for _ in range(5):
        calc.number_button_click("9")

    calc.operation_click("*")

    for _ in range(5):
        calc.number_button_click("9")

    calc.equals_click()

    # Solo verificamos que no crashee
    assert calc.current_value != ""
    assert float(calc.current_value) == 9999800001.0

    root.destroy()