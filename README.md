# Team Practice - Calculadora con GUI 🧮✨

[![CI/CD](https://github.com/WorkTeam01/team-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/WorkTeam01/team-practice/actions/workflows/ci.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Proyecto colaborativo para practicar flujo de trabajo en equipo usando **Python**. Calculadora con interfaz gráfica (GUI), interfaz de línea de comandos (CLI), testing automatizado y CI/CD.

---

## 🎯 Propósito del Proyecto

- **Practicar Git Flow**: Ramas, pull requests, resolución de conflictos
- **Aprender colaboración**: Code reviews, pair programming, comunicación efectiva
- **Desarrollar en Python**: Aprovechar la simplicidad del lenguaje para enfocarse en las prácticas de trabajo en equipo
- **Establecer buenas prácticas**: Documentación, testing, CI/CD, estructura de proyecto

---

## ✨ Características v2.0.0

### 🖥️ Interfaz Gráfica (GUI)

- **Calculadora visual moderna** con tkinter
- **Tema oscuro profesional** con diseño elegante
- **Display de alta resolución** para números y resultados
- **Soporte completo de teclado** + mouse
- **Funciones científicas** integradas (abs, max, min)
- **Manejo visual de errores**

### ⌨️ Atajos de Teclado

| Tecla               | Acción                  |
| ------------------- | ----------------------- |
| `0-9`               | Ingresar dígitos        |
| `. `                | Punto decimal           |
| `+` `-` `*` `/` `^` | Operaciones matemáticas |
| `Enter` o `=`       | Calcular resultado      |
| `Escape`            | Limpiar display (Clear) |
| `Backspace`         | Borrar último carácter  |

### 💻 Interfaz de Línea de Comandos (CLI)

- Interfaz interactiva en terminal
- Todas las operaciones matemáticas disponibles
- Manejo robusto de errores

### 🧪 Testing Automatizado

- Tests unitarios con **pytest**
- Tests de GUI con mocks de Tkinter
- Ejecutable sin interfaz gráfica (headless)
- Ideal para CI/CD

### 🤖 CI/CD con GitHub Actions

- Ejecución automática de tests en cada PR
- Validación continua de calidad de código
- Pipeline configurado para `main` y `dev`

---

## 🚀 Instalación y Uso

### Prerrequisitos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/WorkTeam01/team-practice.git
cd team-practice

# Instalar dependencias
pip install pytest
```

### Ejecutar la Aplicación

#### Interfaz Gráfica (GUI)

```bash
python gui.py
```

#### Interfaz de Línea de Comandos (CLI)

```bash
python main.py
```

### Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest -v

# Tests de calculadora básica
pytest test_calculator.py -v

# Tests de GUI
pytest test_gui_calculator.py -v

# Tests con cobertura
pytest --cov=.  -v
```

---

## 📁 Estructura del Proyecto

```
team-practice/
├── calculator. py              # Lógica de operaciones matemáticas
├── main.py                    # CLI - Interfaz de línea de comandos
├── gui.py                     # GUI - Interfaz gráfica con tkinter
├── test_calculator.py         # Tests unitarios de calculator. py
├── test_gui_calculator.py     # Tests de la interfaz gráfica
├── conftest.py                # Fixtures de pytest (mocks de Tkinter)
├── .github/
│   ├── workflows/
│   │   └── ci.yml            # Pipeline de CI/CD
│   ├── ISSUE_TEMPLATE/       # Plantillas para issues
│   ├── PULL_REQUEST_TEMPLATE/ # Plantillas para PRs
│   ├── pull_request_template.md
│   └── REVIEW_COMMENTS.md
├── README.md                  # Este archivo
├── CHANGELOG.md               # Historial de cambios
├── LICENSE                    # Licencia MIT
└── .gitignore                 # Archivos ignorados por Git
```

---

## 🧮 Operaciones Disponibles

### Operaciones Básicas

- ➕ **Suma**: `a + b`
- ➖ **Resta**: `a - b`
- ✖️ **Multiplicación**: `a * b`
- ➗ **División**: `a / b`
- 🔢 **Potencia**: `a ^ b`

### Funciones Científicas

- `abs(x)` - Valor absoluto
- `max(a, b)` - Valor máximo entre dos números
- `min(a, b)` - Valor mínimo entre dos números

### Manejo de Errores

- ⚠️ División por cero detectada y manejada
- 🛡️ Validación de entrada en ambas interfaces
- 📢 Mensajes de error claros

---

## 🤝 Flujo de Trabajo Colaborativo

### 1. Antes de comenzar

```bash
# Actualizar rama main
git checkout main
git pull origin main

# Crear rama para tu feature
git checkout -b feature/nombre-descriptivo
```

### 2. Durante el desarrollo

- ✅ Commits frecuentes y descriptivos
- ✅ Seguir [Conventional Commits](https://www.conventionalcommits.org/)
- ✅ Escribir tests para nuevas funcionalidades
- ✅ Ejecutar tests localmente antes de push

### 3. Al finalizar

```bash
# Push de tu rama
git push origin feature/nombre-descriptivo

# Crear Pull Request en GitHub
# Solicitar code review
# Mergear después de aprobación
```

---

## 📋 Convenciones

### Commits (Conventional Commits)

```
tipo: descripción breve

Descripción más detallada si es necesario

Ejemplos:
feat: agregar soporte de teclado para calculadora
fix: corregir división por cero
docs: actualizar instrucciones de instalación
test: agregar tests para botones numéricos
refactor: eliminar lógica redundante en operadores
```

**Tipos de commit:**

- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `test`: Agregar o modificar tests
- `refactor`: Refactorización de código
- `style`: Cambios de formato (sin afectar lógica)
- `chore`: Tareas de mantenimiento

### Ramas

- `main`: Rama principal (siempre estable, producción)
- `dev`: Rama de desarrollo (integración)
- `feature/nombre-funcionalidad`: Nuevas características
- `bugfix/descripcion-del-bug`: Corrección de errores
- `hotfix/descripcion-urgente`: Correcciones urgentes en producción
- `release/vX.Y.Z`: Preparación de releases

---

## 👥 Contribuir

### Proceso de Contribución

1. **Asigna o crea un issue** usando las plantillas proporcionadas
   - Para bugs: usa la plantilla de "reporte de error"
   - Para nuevas funciones: usa la plantilla de "nueva funcionalidad"
2. **Crea tu rama** desde `dev` (no desde `main`)

   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feature/mi-funcionalidad
   ```

3. **Implementa tu cambio**

- Escribe código limpio y documentado
- Sigue las convenciones del proyecto

4. **Agrega tests** si aplica

   ```bash
   # Ejecutar tests localmente
   pytest -v
   ```

5. **Actualiza documentación** si es necesario

   - README.md
   - Docstrings en el código
   - CHANGELOG.md (si es un cambio significativo)

6. **Crea Pull Request** usando la plantilla de PR

   - Describe claramente los cambios
   - Referencia el issue relacionado
   - Agrega capturas de pantalla si hay cambios visuales

7. **Espera code review**
   - Responde a los comentarios
   - Realiza los cambios solicitados
8. **Mergea** después de aprobación del equipo

---

## 📦 Releases

El proyecto sigue **[Versionamiento Semántico](https://semver.org/)**:

### Versión Actual: **v2.0.0** 🎉

**Changelog completo:**

- [CHANGELOG.md](CHANGELOG.md) - Historial detallado de todos los cambios

**Versiones disponibles:**

- **v2.0.0** (2025-11-28) - Interfaz gráfica + Testing + CI/CD
- **v1.0.0** (2025-11-04) - Calculadora CLI básica

---

## 🧪 Testing

### Ejecutar Tests

```bash
# Todos los tests
pytest -v

# Tests específicos
pytest test_calculator.py -v
pytest test_gui_calculator.py -v

# Con cobertura
pytest --cov=. --cov-report=html -v

# Tests en modo verbose con detalles
pytest -vv
```

### Estructura de Tests

- **`test_calculator.py`**: Tests de lógica matemática
- **`test_gui_calculator.py`**: Tests de interfaz gráfica
- **`conftest.py`**: Fixtures y mocks de Tkinter

---

## 📞 Comunicación

- **Issues**: Para reportar bugs o proponer features
- **Pull Requests**: Para code reviews y discusión técnica
- **Comentarios en código**: Para aclaraciones específicas
- **Discussions**: Para temas generales del proyecto

---

## 🔧 Comandos Útiles de Git

```bash
# Ver estado del repositorio
git status

# Ver historial de commits
git log --oneline --graph

# Cambiar a rama dev y actualizar
git checkout dev && git pull origin dev

# Ver diferencias antes de commit
git diff

# Agregar cambios y commitear
git add .
git commit -m "tipo(alcance): descripción"

# Actualizar rama feature con cambios de dev
git checkout feature/mi-rama
git merge dev

# Ver ramas locales y remotas
git branch -a

# Eliminar rama local
git branch -d feature/mi-rama
```

---

## 🎓 Recursos de Aprendizaje

### Git y Flujo de Trabajo

- [Git Flow Cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)

### Python

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Python Docstring Conventions (PEP 257)](https://peps.python.org/pep-0257/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

### Testing

- [Pytest Documentation](https://docs.pytest.org/)
- [Testing Best Practices](https://docs.pytest.org/en/stable/goodpractices.html)

---

## 🚧 Próximas Características (v2.1.0)

- [ ] Soporte de operaciones con paréntesis (#44)
- [ ] Fix: Manejo de números decimales negativos (#49)
- [ ] Fix: Raíces pares de números negativos (#50)
- [ ] Historial de operaciones
- [ ] Más funciones matemáticas (√, log, sin, cos, tan)
- [ ] Temas personalizables (claro/oscuro)
- [ ] Exportar historial de cálculos

---

## 🙏 Agradecimientos

Este proyecto fue desarrollado colaborativamente por:

- **[@Jandres25](https://github.com/Jandres25)** - Coordinador, GUI, CI/CD, Testing
- **[@Jhos3ph](https://github.com/Jhos3ph)** - Funciones científicas, Lógica, Refactoring
- **[@alexricardotapiacarita-ai](https://github.com/alexricardotapiacarita-ai)** - Diseño GUI, Documentación

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

---

## 📊 Estadísticas del Proyecto

- **Lenguaje**: Python 3.12+
- **Framework GUI**: Tkinter
- **Framework Testing**: Pytest
- **CI/CD**: GitHub Actions
- **Commits**: 60+
- **Pull Requests**: 24+
- **Issues Cerradas**: 15+

---

**¡Happy coding y colaboración efectiva! ** 🐍✨🚀

Para más información, consulta el [CHANGELOG.md](CHANGELOG.md) para ver el historial completo de cambios.
