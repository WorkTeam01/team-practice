# Team Practice - Flujo de Trabajo Colaborativo

[![CI](https://github.com/WorkTeam01/team-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/WorkTeam01/team-practice/actions/workflows/ci.yml)

Este repositorio está diseñado para practicar y aprender el flujo de trabajo colaborativo en equipo usando **Python** como lenguaje principal, elegido por su facilidad de uso y aprendizaje.

## 🎯 Propósito del Proyecto

- **Practicar Git Flow**: Ramas, merge requests, resolución de conflictos
- **Aprender colaboración**: Code reviews, pair programming, comunicación efectiva
- **Desarrollar en Python**: Aprovechar la simplicidad del lenguaje para enfocarse en las prácticas de trabajo en equipo
- **Establecer buenas prácticas**: Documentación, testing, estructura de proyecto

## 🚀 Configuración Inicial

### Prerrequisitos

- Python 3.12 o superior
- Git
- Editor de código (VS Code recomendado)

### Características Implementadas

- Interfaz gráfica con tkinter

### Próximas Características

- Más operaciones matemáticas
- Historial de operaciones
- Soporte para expresiones matemáticas complejas

Para ver el historial detallado de cambios, consulta el archivo [CHANGELOG.md](CHANGELOG.md)

### Instalación

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd team-practice

# Instalar pytest (única dependencia necesaria)
pip install pytest
```

## 📁 Estructura del Proyecto

```
team-practice/
├── calculator.py       # Código fuente principal
├── test_calculator.py  # Pruebas unitarias
├── main.py             # Programa principal
├── gui.py              # Interfaz gráfica      
├── .gitignore          # Archivos ignorados por Git
├── .github/            # Configuración y templates de GitHub
│   ├── ISSUE_TEMPLATE/ # Plantillas para issues
│   ├── PULL_REQUEST_TEMPLATE/ # Plantillas para pull requests
│   ├── pull_request_template.md # Template para pull requests
│   └── REVIEW_COMMENTS.md      # Plantillas para comentarios de revisión
├── README.md           # Este archivo
├── CHANGELOG.md        # Historial de cambios
└── LICENSE             # Licencia del proyecto
```

## 🤝 Flujo de Trabajo

### 1. Antes de comenzar

- Hacer pull de la rama main
- Crear una nueva rama para tu feature: `git checkout -b feature/nombre-descriptivo`

### 2. Durante el desarrollo

- Commits frecuentes y descriptivos
- Seguir convenciones de naming
- Escribir tests para nuevas funcionalidades

### 3. Al finalizar

- Push de tu rama
- Crear Pull Request
- Solicitar code review
- Mergear después de aprobación

## 📋 Convenciones

### Commits

```
tipo: descripción breve

Descripción más detallada si es necesario

Ejemplos:
feat: agregar función de validación de email
fix: corregir error en cálculo de descuentos
docs: actualizar README con instrucciones de setup
```

### Ramas

- `main`: Rama principal (siempre estable)
- `feature/nombre-funcionalidad`: Nuevas características
- `bugfix/descripcion-del-bug`: Corrección de errores
- `hotfix/descripcion-urgente`: Correcciones urgentes

## 🧪 Testing

### Ejecutar pruebas localmente

```bash
# Ejecutar todas las pruebas
pytest -v

# Ejecutar pruebas de un archivo específico
pytest test_calculator.py -v

# Ejecutar el programa principal
python main.py

# Ejecutar la interfaz gráfica
python gui.py
```

### Integración Continua (CI)

Este proyecto usa **GitHub Actions** para ejecutar automáticamente las pruebas en cada push y pull request. El badge de estado al inicio del README muestra si las pruebas están pasando.

- ✅ **Verde**: Todas las pruebas pasan
- ❌ **Rojo**: Hay pruebas fallando

Para más detalles, revisa el archivo de configuración en `.github/workflows/ci.yml`

## 👥 Contribuir

1. Asigna o crea un issue usando las plantillas proporcionadas
   - Para bugs: usa la plantilla "reporte-error.md"
   - Para nuevas funciones: usa la plantilla "funcion-calculadora.md"
2. Crea tu rama desde main
3. Implementa tu cambio
4. Agrega tests si aplica
5. Actualiza documentación
6. Crea Pull Request usando la plantilla de PR
7. Espera code review
8. Mergea después de aprobación

### 📦 Releases

El proyecto sigue versionamiento semántico. Última versión estable: v1.0.0

- Operaciones básicas: suma, resta, multiplicación, división, potencia
- Funciones adicionales: valor máximo, valor mínimo, valor absoluto
- Sistema de manejo de errores
- Interfaz de línea de comandos interactiva

## 📞 Comunicación

- **Issues**: Para reportar bugs o proponer features
- **Pull Requests**: Para code reviews y discusión técnica
- **Comentarios en código**: Para aclaraciones específicas

## 🔧 Comandos Útiles

```bash
# Ver estado del repositorio
git status

# Ver historial de commits
git log --oneline

# Cambiar a rama main y actualizar
git checkout main && git pull

# Ver diferencias
git diff

# Agregar cambios y commitear
git add . && git commit -m "tu mensaje"
```

## 📚 Recursos de Aprendizaje

- [Git Flow Cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Python Style Guide (PEP 12)](https://www.python.org/dev/peps/pep-0012/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

**¡Happy coding y colaboración efectiva!** 🐍✨
