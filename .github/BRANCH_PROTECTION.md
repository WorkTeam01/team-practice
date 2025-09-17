# Configuración de Protección de Ramas

Este documento describe la configuración recomendada para proteger las ramas `main` y `dev` en el repositorio.

## 🔒 Estado Actual

### Ramas Protegidas
- ✅ **main**: Protegida
- ✅ **dev**: Protegida

## 📋 Configuración Recomendada

### Para la rama `main`:
```yaml
Configuraciones esenciales:
- Require a pull request before merging: ✅ Habilitado
- Require approvals: ✅ Mínimo 1 aprobación
- Dismiss stale PR approvals when new commits are pushed: ✅ Habilitado
- Require review from code owners: ⚠️ Recomendado (si existe CODEOWNERS)
- Require status checks to pass before merging: ✅ Habilitado
- Require branches to be up to date before merging: ✅ Habilitado
- Require linear history: ⚠️ Opcional (recomendado para equipos grandes)
- Include administrators: ✅ Habilitado
```

### Para la rama `dev`:
```yaml
Configuraciones esenciales:
- Require a pull request before merging: ✅ Habilitado
- Require approvals: ⚠️ Opcional (puede ser 0 para desarrollo)
- Require status checks to pass before merging: ✅ Habilitado
- Require branches to be up to date before merging: ✅ Habilitado
- Include administrators: ✅ Habilitado
```

## 🔧 Checks de Estado Requeridos

Los siguientes checks deben pasar antes de permitir merge:

1. **CI - Tests y Validación / test**: Ejecuta tests en múltiples versiones de Python
2. **CI - Tests y Validación / code-quality**: Verifica calidad del código

## 📝 Flujo de Trabajo Recomendado

### 1. Crear Feature Branch
```bash
git checkout main
git pull origin main
git checkout -b feature/nueva-funcionalidad
```

### 2. Desarrollar y Probar
```bash
# Hacer cambios
git add .
git commit -m "feat: agregar nueva funcionalidad"

# Ejecutar tests localmente
pytest test_calculator.py
```

### 3. Crear Pull Request
```bash
git push origin feature/nueva-funcionalidad
# Crear PR en GitHub hacia dev o main según corresponda
```

### 4. Code Review y Merge
- El PR debe pasar todos los checks automáticos
- Debe ser revisado por al menos 1 persona (para main)
- Se debe actualizar la rama antes del merge si hay cambios

## ⚠️ Restricciones Implementadas

### Prohibido en ramas protegidas:
- ❌ Push directo (bypass de PR)
- ❌ Force push
- ❌ Eliminación de la rama
- ❌ Merge sin aprobaciones (en main)
- ❌ Merge con checks fallidos

### Requerido para merge:
- ✅ Pull Request creado
- ✅ Checks de CI pasando
- ✅ Aprobación de código (en main)
- ✅ Rama actualizada con la base

## 🎯 Beneficios de esta Configuración

1. **Calidad del Código**: Todos los cambios pasan por review
2. **Estabilidad**: Tests automáticos previenen regresiones
3. **Trazabilidad**: Historial claro de cambios via PRs
4. **Colaboración**: Fomenta discusión y aprendizaje en equipo
5. **Mejores Prácticas**: Refuerza el flujo de Git Flow

## 🔄 Verificación de la Configuración

Para verificar que la protección está activa:

1. Intentar push directo a main/dev (debe fallar)
2. Crear PR y verificar que requiere checks
3. Confirmar que aparecen los status checks configurados

## 📚 Recursos Adicionales

- [GitHub Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
- [Git Flow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)