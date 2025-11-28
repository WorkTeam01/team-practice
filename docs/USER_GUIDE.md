# 📖 Guía de Usuario - Calculadora GUI

## 🚀 Inicio Rápido

### Requisitos

- Python 3.12 o superior
- tkinter (incluido en Python estándar)

### Ejecutar la aplicación

```bash
python gui.py
```

![Vista Principal](https://raw.githubusercontent.com/WorkTeam01/team-practice/dev/docs/screenshots/calculator-main.jpeg)

---

## 🖥️ Interfaz de Usuario

### Display

El display en la parte superior muestra:

- Números ingresados
- Resultados de operaciones
- Mensajes de error

### Botones Numéricos (0-9)

Click en estos botones para ingresar números.

**Ejemplo:**

1. Click en "5"
2. Click en "2"
3. Display muestra: "52"

### Botón Punto Decimal (.)

Permite ingresar números decimales.

**Ejemplo:**

- Click en "5", ".", "2" → Display: "5.2"

### Botones de Operadores (+, -, \*, /, ^)

Realizan operaciones matemáticas.

**Ejemplo de suma:**

1. Ingresa "5"
2. Click en "+"
3. Ingresa "3"
4. Click en "="
5. Resultado: "8"

**Ejemplo de resta:**

1. Ingresa "7"
2. Click en "-"
3. Ingresa "3"
4. Click en "="
5. Resultado: "4"

**Ejemplo de multipicación:**

1. Ingresa "5"
2. Click en "\*"
3. Ingresa "5"
4. Click en "="
5. Resultado: "25"

**Ejemplo de división:**

1. Ingresa "15"
2. Click en "/"
3. Ingresa "3"
4. Click en "="
5. Resultado: "5"

**Ejemplo de elevado:**

1. Ingresa "5"
2. Click en "^"
3. Ingresa "3"
4. Click en "="
5. Resultado: "125"

![Operaciones basicas](https://raw.githubusercontent.com/WorkTeam01/team-practice/dev/docs/screenshots/operaciones-basicas.gif)

---

## 🔬 Funciones Científicas

### Valor Absoluto (abs)

Convierte números negativos en positivos.

**Ejemplo:**

1. Ingresa "-5"
2. Click en "abs"
3. Resultado: "5"

### Máximo (max)

Encuentra el mayor de dos números.

**Ejemplo:**

1. Ingresa "10"
2. Click en "max"
3. Ingresa "20"
4. Click en "="
5. Resultado: "20"

### Mínimo (min)

Encuentra el menor de dos números.

**Ejemplo:**

1. Ingresa "10"
2. Click en "min"
3. Ingresa "20"
4. Click en "="
5. Resultado: "10"

![Funciones Científicas](https://raw.githubusercontent.com/WorkTeam01/team-practice/dev/docs/screenshots/calculator-scientific.gif)

---

## 🗑️ Botón Clear (C)

Limpia el display y resetea la calculadora.

**Uso:**

- Click en "C" en cualquier momento
- Todo se resetea, listo para nuevo cálculo

---

## ⚠️ Manejo de Errores

### División por Cero

La calculadora muestra un mensaje de error.

**Ejemplo:**

1. Ingresa "5"
2. Click en "/"
3. Ingresa "0"
4. Click en "="
5. Display: "Error: No se puede dividir por cero"

![Error](https://raw.githubusercontent.com/WorkTeam01/team-practice/dev/docs/screenshots/calculator-error.gif)

**Solución:** Click en "C" para comenzar de nuevo

---

## 💡 Consejos y Trucos

### Operaciones Consecutivas

Puedes continuar operando con el resultado:

- `5 + 3 = 8` → `* 2 = 16` → `- 1 = 15`

### Números Decimales

- Puedes ingresar decimales en cualquier operación
- Solo un punto por número
- Ejemplo: `5.5 + 2.3 = 7.8`

---

## 🆘 Troubleshooting

### Problema: Display no muestra nada

**Solución:** Click en "C" para resetear

### Problema: Error después de operación

**Solución:** Click en "C" y comienza de nuevo

### Problema: No puedo ingresar más dígitos

**Solución:** Probablemente alcanzaste el resultado, usa "C" o continúa operando

---

## 📞 Soporte

Si encuentras un bug o tienes sugerencias:

- Crea un issue en GitHub
- Contacta al equipo de desarrollo
