# CLAUDE.md

Este archivo proporciona orientación a Claude Code (claude.ai/code) al trabajar con el código en este repositorio.

## Comandos

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar todas las pruebas (sin interfaz gráfica, funciona en CI)
pytest -v

# Ejecutar un archivo de pruebas específico
pytest tests/test_calculator.py -v
pytest tests/test_gui.py -v

# Ejecutar una prueba específica por palabra clave
pytest tests/test_gui.py -k "parenthesis" -v

# Ejecutar con cobertura
pytest --cov=src -v

# Lanzar la aplicación con GUI
python src/gui.py

# Lanzar la aplicación por CLI
python src/cli.py
```

## Arquitectura

Calculadora Python con tres capas:

**Core (`src/calculator.py`):** Funciones puras sin dependencias externas — `add`, `subtract`, `multiply`, `divide`, `power`, `valor_maximo`, `valor_minimo`, `abs_value`. Lanza `ZeroDivisionError` y `ValueError` para entradas inválidas.

**GUI (`src/gui.py`):** Clase única `CalculatorGUI` con tkinter. Funciona en dos modos controlados por `use_expression_mode`:
- **Modo normal:** Cálculos de dos operandos usando el estado `first_number` + `operator` + `current_value`
- **Modo expresión:** Se activa al usar paréntesis; construye una cadena `expression` que se evalúa mediante parsing con regex y las funciones de `calculator.py`

**CLI (`src/cli.py`):** Bucle interactivo que parsea entradas como `"5 + 3"` o `"5 abs"`.

**Tests (`tests/`):** `conftest.py` provee mocks `DummyRoot`, `DummyEntry`, `DummyButton`, `DummyLabel` que reemplazan tkinter automáticamente (fixture autouse), permitiendo pruebas de GUI sin pantalla en CI.

## Ramas y Convención de Commits

Nomenclatura de ramas: `feature/*`, `bugfix/*`, `hotfix/*`, `release/*` a partir de `dev`; los PRs se fusionan a `dev` y luego a `main`.

Los commits siguen [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `test:`, `docs:`, `refactor:`, `chore:`.

El CI ejecuta pytest en push/PR a `main` y `dev` mediante `.github/workflows/ci.yml`.
