# Team Practice - Flujo de Trabajo Colaborativo

[![CI - Tests y Validación](https://github.com/WorkTeam01/team-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/WorkTeam01/team-practice/actions/workflows/ci.yml)

Este repositorio está diseñado para practicar y aprender el flujo de trabajo colaborativo en equipo usando **Python** como lenguaje principal, elegido por su facilidad de uso y aprendizaje.

## 🎯 Propósito del Proyecto

- **Practicar Git Flow**: Ramas, merge requests, resolución de conflictos
- **Aprender colaboración**: Code reviews, pair programming, comunicación efectiva
- **Desarrollar en Python**: Aprovechar la simplicidad del lenguaje para enfocarse en las prácticas de trabajo en equipo
- **Establecer buenas prácticas**: Documentación, testing, estructura de proyecto

## 🚀 Configuración Inicial

### Prerrequisitos
- Python 3.8 o superior
- Git
- Editor de código (VS Code recomendado)

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
├── calculator.py        # Código fuente principal
├── test_calculator.py   # Pruebas unitarias
├── main.py             # Programa principal
├── .gitignore          # Archivos ignorados por Git
├── README.md          # Este archivo
└── LICENSE           # Licencia del proyecto
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

### 🔒 Protección de Ramas
Las ramas `main` y `dev` están **protegidas** y requieren:
- ✅ Pull Request obligatorio (no push directo)
- ✅ Aprobación de código (mínimo 1 reviewer en main)
- ✅ Checks de CI/Tests pasando
- ✅ Rama actualizada antes del merge

Para más detalles, consulta: [Configuración de Protección](.github/BRANCH_PROTECTION.md)

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
```bash
# Ejecutar todas las pruebas
pytest test_calculator.py

# Ejecutar el programa principal
python main.py
```

## 👥 Contribuir

1. Asigna o crea un issue
2. Crea tu rama desde main
3. Implementa tu cambio
4. Agrega tests si aplica
5. Actualiza documentación
6. Crea Pull Request
7. Espera code review
8. Mergea después de aprobación

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
- [Conventional Commits](https://www.conventionalcommits.org/)

---
**¡Happy coding y colaboración efectiva!** 🐍✨
