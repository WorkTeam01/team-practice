# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2025-11-28

### 🎉 Major Release - Interfaz Gráfica + Testing Automatizado

Este release marca una evolución significativa del proyecto, introduciendo una interfaz gráfica completa, testing automatizado robusto, soporte de teclado y múltiples mejoras de usabilidad.

### Agregado

#### Interfaz Gráfica de Usuario (GUI)

- **Calculadora visual** con tkinter (#15, #16, #17)
  - Ventana principal con diseño moderno
  - Display interactivo de alta resolución para números y resultados
  - Grid de botones organizados por función
  - Tema oscuro profesional con paleta de colores elegante (#18, #19, #20, #21)
  - Diseño responsive con grid layout adaptable

#### Funcionalidades de GUI

- **Entrada numérica** por clicks en botones (#22, #31)
- **Botón decimal (.)** con validación para evitar múltiples puntos (#25, #32)
- **Lógica de operadores** matemáticos: +, -, \*, /, ^ (#26, #33)
- **Botones de control**:
  - Clear (C): Limpia display y resetea estado (#28, #34)
  - Backspace (⌫): Elimina último carácter (#28, #34)
- **Funciones científicas** integradas en GUI (#30, #35):
  - Valor absoluto (abs)
  - Máximo (max)
  - Mínimo (min)
- **Soporte para números negativos** (#41, #45)
  - Ingreso de números negativos en la GUI
  - Manejo correcto de operaciones con negativos
- **Mejoras en manejo de múltiples números negativos** (#43)
- **Soporte completo de teclado** (#37, #47)
  - Atajos para todos los números (0-9)
  - Atajos para operadores (+, -, \*, /, ^)
  - Enter o = para calcular resultado
  - Escape para limpiar display
  - Backspace para borrar último carácter
  - Control completo mediante teclado o mouse

#### Testing Automatizado

- **Archivo `test_gui_calculator.py`** con suite completa de tests para GUI (#23, #48)
  - Tests de clicks en botones numéricos
  - Tests de botón Clear y Backspace
  - Tests de operaciones básicas
  - Tests de manejo de errores
- **Archivo `conftest.py`** con fixtures y mocks de Tkinter (#48)
  - Clases dummy: DummyRoot, DummyEntry, DummyButton, DummyLabel
  - Fixture `autouse` para sustituir componentes gráficos
  - Tests ejecutables sin display gráfico (ideal para CI/CD)
  - Compatibilidad con entornos headless

#### CI/CD con GitHub Actions

- **Pipeline automático** de integración continua (#36, #42)
  - Workflow configurado para ramas `main` y `dev`
  - Ejecución automática de tests en cada PR
  - Validación continua de calidad de código
  - Tests en ambiente headless sin Tcl/Tk
  - Archivo `.github/workflows/ci.yml` configurado

#### Documentación

- **Guía de usuario** para la interfaz gráfica (#24, #40)
  - Instrucciones de uso de la GUI
  - Ejemplos de operaciones
  - Atajos de teclado documentados
- **Mejoras en documentación** de funciones y manejo de errores (#29, #39)

### Mejorado

- **Experiencia de usuario** con dos interfaces disponibles:
  - CLI (`main.py`): Interfaz de línea de comandos original
  - GUI (`gui. py`): Interfaz gráfica moderna
- **Refactoring de lógica** redundante en manejo de operadores (#46)
- **Manejo visual de errores** en la GUI
  - División por cero detectada y manejada
  - Mensajes de error claros en el display
  - Validación de entrada de decimales y negativos
- **Organización del proyecto** con separación clara CLI/GUI/tests
- **Calidad de código** con validación continua

### Técnico

- Implementación de clase `CalculatorGUI` con tkinter
- Sistema de grid layout responsivo para botones
- Binding de eventos de teclado en tkinter
- Fixtures de pytest con `autouse=True`
- Mocks de componentes Tkinter para testing sin GUI
- Workflow de GitHub Actions para CI/CD
- Integración completa entre GUI y módulo `calculator. py`

### Mantenido

- Interfaz de línea de comandos (CLI) en `main.py`
- Todas las funciones matemáticas originales
- Compatibilidad con Python 3.12+
- Suite de tests unitarios (`test_calculator.py`)
- Templates de Issues y Pull Requests

### Issues y PRs Incluidas

**Issues Completadas:**

- #15 - Implementar: Prototipo inicial de GUI
- #18 - Mejorar diseño: Ajustes y refinamientos de la GUI
- #20 - Mejora: Estilos visuales de la GUI
- #22 - Agregar función: Clicks de botones numéricos en GUI
- #23 - Pruebas: Testing manual completo de GUI
- #24 - Documentación: Guía de usuario para GUI
- #25 - Agregar función: Botón punto decimal en GUI
- #26 - Agregar función: Lógica de operadores en GUI
- #28 - Agregar funcionalidad: Botones Clear y Backspace
- #29 - Mejora: Manejo de errores y validaciones en GUI
- #30 - Agregar función: Funciones científicas en GUI
- #36 - Configurar CI/CD con GitHub Actions
- #37 - Agregar soporte de teclado para calculadora GUI
- #41 - Mejora: Números negativos sin operación de resta
- #43 - Error: Difícil ingresar múltiples números negativos

**Pull Requests Mergeados:**

- #48 - test: agregar tests de GUI con mocks de tkinter
- #47 - feat: agregar soporte de teclado para calculadora GUI
- #46 - refactor(gui): eliminar lógica redundante en el manejo de operadores
- #45 - feat(gui): soporte para números negativos y actualización de documentación
- #42 - feat: Configurar CI/CD con GitHub Actions
- #40 - docs: Añadir guía de usuario para la GUI
- #39 - refactor(gui): mejorar funciones unarias y manejo de errores
- #35 - feat: Agregar funciones científicas (abs, max, min) con integración en GUI
- #34 - feat: implementar botones C y ⌫ con su funcionalidad correspondiente
- #33 - feat(core): añadir lógica de operaciones (+, -, \*, /, ^) y soporte para botón "="
- #32 - feat: implementar botón decimal con validación en la calculadora Tkinter
- #31 - feat: Implementar lógica de clic para entrada numérica
- #21 - feat: actualizar colores en gui.py
- #19 - feat: ajustar diseño según selección del equipo
- #17 - feat: Merge prototype calculator design from dev to main
- #16 - feat: agregar prototipo de GUI con diseño base

### Agradecimientos

Este release fue posible gracias a las contribuciones de:

- **@Jandres25** (Jose Andres Meneces Lopez)

  - Coordinador del release
  - Prototipo de GUI (#15, #16)
  - CI/CD con GitHub Actions (#42)
  - Testing automatizado de GUI (#23, #48)
  - Soporte de teclado (#47)

- **@Jhos3ph**

  - Funciones científicas en GUI (#35)
  - Lógica de operaciones (#26, #33)
  - Entrada numérica (#22, #31)
  - Refactoring y optimizaciones (#39, #46)
  - Soporte de números negativos (#45)

- **@alexricardotapiacarita-ai**
  - Diseño y estilos visuales (#18, #19, #20, #21)
  - Botón decimal con validación (#25, #32)
  - Botones Clear y Backspace (#28, #34)
  - Documentación y guía de usuario (#24, #40)

---

## [1.0.0] - 2025-11-04

### Agregado

- Operaciones matemáticas básicas (suma, resta, multiplicación, división)
- Funciones adicionales:
  - Potenciación
  - Valor máximo entre dos números
  - Valor mínimo entre dos números
  - Valor absoluto
- Interfaz de línea de comandos interactiva
- Manejo de errores y excepciones
- Pruebas unitarias con pytest
- Templates para Issues y Pull Requests en GitHub
  - Plantilla para reporte de errores
  - Plantilla para solicitud de funcionalidades

### Técnico

- Implementación base en Python 3.12
- Estructura del proyecto organizada
- Sistema de pruebas configurado con pytest

---

## [Próximamente] - v2.1.0

### Planeado

- Soporte de operaciones con paréntesis en GUI (#44)
- Fix: Manejo de números decimales negativos (#49)
- Fix: Raíces pares de números negativos (#50)
- Historial de operaciones
- Más funciones matemáticas (raíz cuadrada, logaritmos, trigonometría)
- Temas personalizables (claro/oscuro)
- Exportar historial de cálculos
