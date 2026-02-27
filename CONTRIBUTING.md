# Guía de Contribución

Gracias por tu interés en contribuir. Este documento describe el proceso y las convenciones del proyecto para mantener un flujo de trabajo ordenado y consistente.

---

## Configuración del entorno

```bash
git clone https://github.com/WorkTeam01/team-practice.git
cd team-practice
pip install -r requirements.txt

# Verificar que todo funciona
pytest -v
```

---

## Flujo de trabajo

Este proyecto sigue **Git Flow**. Todo el desarrollo ocurre en `dev`; `main` solo recibe merges de releases estables.

### 1. Crear una rama desde `dev`

```bash
git checkout dev
git pull origin dev
git checkout -b <tipo>/nombre-descriptivo
```

| Prefijo      | Cuándo usarlo                            |
| ------------ | ---------------------------------------- |
| `feature/`   | Nueva funcionalidad                      |
| `bugfix/`    | Corrección de un error                   |
| `hotfix/`    | Corrección urgente directamente en `main`|
| `release/`   | Preparación de una nueva versión         |

### 2. Desarrollar y hacer commits

Sigue el formato de [Conventional Commits](https://www.conventionalcommits.org/):

```
<tipo>: <descripción breve en imperativo>
```

| Tipo         | Cuándo usarlo                                       |
| ------------ | --------------------------------------------------- |
| `feat`       | Nueva funcionalidad                                 |
| `fix`        | Corrección de bug                                   |
| `test`       | Agregar o modificar tests                           |
| `docs`       | Cambios en documentación                            |
| `refactor`   | Cambios de código sin afectar comportamiento        |
| `style`      | Formato, espaciado, nombres (sin cambios de lógica) |
| `chore`      | Tareas de mantenimiento, dependencias, CI           |

**Ejemplos:**
```
feat: agregar función de historial de operaciones
fix: corregir validación de paréntesis desbalanceados
test: cubrir casos borde en abs_value con negativos
```

### 3. Abrir un Pull Request

- La rama destino siempre es `dev` (nunca directamente a `main`)
- Usa la plantilla de PR del repositorio
- Referencia el issue relacionado con `Closes #<número>`
- Ejecuta los tests antes de hacer push:

```bash
pytest -v
```

### 4. Code review

- Todo PR requiere al menos una aprobación antes de mergear
- Responde los comentarios y realiza los cambios solicitados
- No hagas force push a una rama que ya tiene un PR abierto

---

## Reportar issues

Usa las plantillas disponibles en GitHub según el caso:

- **Reporte de error** — para bugs o comportamiento inesperado
- **Mejora de función** — para proponer cambios en funcionalidad existente
- **Nueva funcionalidad** — para proponer features nuevas
- **Sugerencia general** — para ideas o discusiones abiertas

---

## Estándares de código

- **Estilo:** [PEP 8](https://pep8.org/)
- **Docstrings:** [PEP 257](https://peps.python.org/pep-0257/) — todas las funciones públicas deben tenerlos
- **Tests:** Toda nueva funcionalidad debe incluir tests en `tests/`. Los tests de GUI deben usar los mocks de `conftest.py` para ser ejecutables sin pantalla

---

## Preguntas

Si tienes dudas, abre un issue con la plantilla de **sugerencia general** o comenta directamente en el PR correspondiente.
