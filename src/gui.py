"""Interfaz gráfica de usuario (GUI) para la calculadora. 

Este módulo implementa una calculadora con interfaz tkinter que incluye:
- Operaciones básicas: suma, resta, multiplicación, división, potencia
- Funciones científicas: valor absoluto, máximo, mínimo
- Soporte para paréntesis en expresiones matemáticas
- Soporte para teclado y números negativos
- Manejo de errores con mensajes visuales
"""
import tkinter as tk
import re

try:
    from .calculator import add, subtract, multiply, divide, power, valor_maximo, valor_minimo, abs_value
except ImportError:
    from calculator import add, subtract, multiply, divide, power, valor_maximo, valor_minimo, abs_value

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("330x450")
        self.root.configure(bg="#1E1E1E")
        
        # Variables de estado de la calculadora
        self.expression = ""  # Guarda expresiones completas como "(2+3)*4"
        self.current_value = ""
        self.operator = None
        self.first_number = None
        self.use_expression_mode = False  # True cuando usamos paréntesis

        # Crear la interfaz
        self.create_widgets()
        
        # Habilitar el uso del teclado
        self.root.bind('<Key>', self.handle_keypress)

    def create_widgets(self):

        COLORS = {
            "bg": "#1E1E1E",
            "display": "#2B2B2B",
            "numbers": "#3A3A3A",
            "operators": "#FF8C00",
            "equal": "#FF8C00",
            "clear": "#6E6E6E",
            "text": "#FFFFFF",
            "error": "#FF4444"
        }

        # Display principal
        self.display = tk.Entry(
            self.root,
            font=("Arial", 28, "bold"),
            justify="right",
            bg=COLORS["display"],
            fg=COLORS["text"],
            relief="flat",
            bd=10
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(10, 0))

        # Label para mensajes de error
        self.error_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            bg=COLORS["bg"],
            fg=COLORS["error"],
            height=1
        )
        self.error_label.grid(row=1, column=0, columnspan=4, sticky="ew", padx=10, pady=(0, 5))

        # Definición de botones
        buttons = [
            ('C', 2, 0, COLORS["clear"]),
            ('(', 2, 1, COLORS["numbers"]),
            (')', 2, 2, COLORS["numbers"]),
            ('⌫', 2, 3, COLORS["clear"]),

            ('max', 3, 0, COLORS["numbers"]),
            ('min', 3, 1, COLORS["numbers"]),
            ('abs', 3, 2, COLORS["numbers"]),
            ('/', 3, 3, COLORS["operators"]),

            ('7', 4, 0, COLORS["numbers"]),
            ('8', 4, 1, COLORS["numbers"]),
            ('9', 4, 2, COLORS["numbers"]),
            ('*', 4, 3, COLORS["operators"]),

            ('4', 5, 0, COLORS["numbers"]),
            ('5', 5, 1, COLORS["numbers"]),
            ('6', 5, 2, COLORS["numbers"]),
            ('-', 5, 3, COLORS["operators"]),

            ('1', 6, 0, COLORS["numbers"]),
            ('2', 6, 1, COLORS["numbers"]),
            ('3', 6, 2, COLORS["numbers"]),
            ('+', 6, 3, COLORS["operators"]),

            ('^', 7, 0, COLORS["operators"]),
            ('0', 7, 1, COLORS["numbers"]),
            ('.', 7, 2, COLORS["numbers"]),
            ('=', 7, 3, COLORS["equal"]),
        ]

        # Asignar función a cada botón
        for (txt, r, c, color) in buttons:
            if txt.isdigit():
                cmd = lambda t=txt: self.number_button_click(t)
            elif txt == '.':
                cmd = self.decimal_click
            elif txt in ['+', '-', '*', '/', '^']:
                cmd = lambda t=txt: self.operation_click(t)
            elif txt == '=':
                cmd = self.equals_click
            elif txt == 'C':
                cmd = self.clear_click
            elif txt == '⌫':
                cmd = self.backspace_click
            elif txt == '(':
                cmd = self.open_parenthesis_click
            elif txt == ')':
                cmd = self.close_parenthesis_click
            elif txt in ['abs', 'max', 'min']:
                cmd = lambda t=txt: self.scientific_click(t)
            else:
                cmd = lambda: None
            
            tk.Button(
                self.root,
                text=txt,
                bg=color,
                fg=COLORS["text"],
                font=("Arial", 16, "bold"),
                relief="flat",
                bd=0,
                activebackground=color,
                activeforeground=COLORS["text"],
                highlightthickness=0,
                command=cmd
            ).grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

        # Hacer que los botones se expandan con la ventana
        for i in range(8):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        

    def handle_keypress(self, event):
        """Maneja las teclas presionadas por el usuario.
        
        Mapea las teclas del teclado a las funciones de la calculadora,
        incluyendo paréntesis.
        """
        key = event.char
        
        # Dígitos 0-9
        if key.isdigit():
            self.number_button_click(key)
        
        # Operadores básicos
        elif key in ['+', '-', '*', '/']:
            self.operation_click(key)
        
        # Potencia
        elif key == '^':
            self.operation_click('^')
        
        # Decimal
        elif key == '.':
            self.decimal_click()
        
        # Paréntesis desde el teclado
        elif key == '(':
            self.open_parenthesis_click()
        
        elif key == ')':
            self.close_parenthesis_click()
        
        # Calcular (Enter o =)
        elif key in ['\r', '\n', '=']:
            self.equals_click()
        
        # Limpiar todo (Escape)
        elif event.keysym == 'Escape':
            self.clear_click()
        
        # Borrar último carácter (Backspace)
        elif event.keysym == 'BackSpace':
            self.backspace_click()


    def open_parenthesis_click(self):
        """Agrega un paréntesis de apertura a la expresión. 
        
        Activa el modo de expresión para evaluar con paréntesis.
        
        Examples:
            >>> # Usuario presiona "("
            >>> # Display muestra: "("
            >>> # use_expression_mode = True
        """
        # Si hay algo en current_value o ya hay operación en curso, transferir a expression
        if not self.use_expression_mode:
            if self.first_number is not None:
                self.expression = str(self.first_number)
                if self.operator:
                    self.expression += self.operator
                if self.current_value:
                    self.expression += self.current_value
            elif self.current_value:
                self.expression = self.current_value
        
        self.use_expression_mode = True
        self.expression += '('
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


    def close_parenthesis_click(self):
        """Agrega un paréntesis de cierre a la expresión.
        
        Examples:
            >>> # Expression: "(2+3"
            >>> # Usuario presiona ")"
            >>> # Display muestra: "(2+3)"
        """
        self.use_expression_mode = True
        self.expression += ')'
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


    def number_button_click(self, valor):
        """Maneja clicks de botones numéricos.
        
        Funciona tanto en modo normal como en modo de expresión con paréntesis.
        
        Args:
            valor (str): Dígito presionado (0-9)
        
        Examples:
            >>> # Usuario presiona 2, 3, 5
            >>> # Display muestra: "235"
            >>> # Con paréntesis: "(2+3)*5"
        """
        # Asegurarnos de que es un número
        if not str(valor).isdigit():
            self.show_error("Número inválido")
            return
        
        if self.use_expression_mode:
            self.expression += str(valor)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        else:
            self.current_value += str(valor)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_value)
    

    def decimal_click(self):
        """Maneja click del botón decimal con validaciones mejoradas.
    
        Funciona en modo normal y en modo de expresión con paréntesis.
        
        Corrige casos como:
            "-" + "." → "-0."
            "-.3"     → "-0.3"
        
        Previene:
            "-." como número inválido. 
        """
        if self.use_expression_mode:
            # Si estamos en modo expresión, solo agregamos el punto
            self.expression += '.'
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
            return

        # Si escribieron solo "-" y presionan ".", convertir a "-0."
        if self.current_value == "-":
            self.current_value = "-0."
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_value)
            return

        # Si no hay nada, empezar con "0."
        if not self.current_value:
            self.current_value = "0."
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_value)
            return

        # No permitir más de un punto decimal
        if '.' in self.current_value:
            return

        # Verificar que lo que hay sea un número válido
        try:
            float(self.current_value)
        except ValueError:
            self.show_error("Número inválido")
            return

        # Todo bien, agregar el punto
        self.current_value += '.'
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_value)


    def operation_click(self, operation):
        """Maneja clicks de operadores matemáticos.
    
        Funciona en modo normal y en modo de expresión con paréntesis.
        Guarda el primer número y operador para calcular cuando 
        el usuario presione "=".
        
        Args:
            operation (str): Operador (+, -, *, /, ^, max, min)
        
        Examples:
            >>> # Usuario: 5 + 3 =
            >>> # 1.Ingresa "5"
            >>> # 2.Click "+": first_number=5, operator="+"
            >>> # 3.  Ingresa "3"  
            >>> # 4.Click "=": calcula 5+3=8
            >>> 
            >>> # Con paréntesis: (2+3)*4
            >>> # expression = "(2+3)*4"
        """
        if self.use_expression_mode:
            self.expression += operation
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
            return

        # Caso especial: permitir escribir números negativos
        if operation == '-' and (self.current_value == "" or self.current_value is None):
            self.current_value = '-'
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_value)
            return
        if operation == '-' and self.current_value == '-':
            return

        # Si cambiaron de opinión sobre el operador, actualizarlo
        if not self.current_value:
            if self.first_number is not None:
                self.operator = operation
            return

        # Verificar que lo ingresado sea un número válido
        try:
            value = float(self.current_value)
        except ValueError:
            self.show_error("Número inválido")
            return

        # Primera vez: guardar el número y el operador
        if self.first_number is None:
            self.first_number = value
            self.operator = operation
            self.current_value = ""
            return

        # Ya hay una operación pendiente, calcularla primero
        if self.first_number is not None and self.operator is not None:
            self.equals_click()
            try:
                self.first_number = float(self.current_value)
            except ValueError:
                self.show_error("Número inválido")
                return
            self.operator = operation
            self.current_value = ""

    def equals_click(self):
        """Calcula el resultado de la operación o expresión actual.
        
        Soporta dos modos:
        1.Modo normal: operaciones simples con dos números
        2.Modo expresión: expresiones completas con paréntesis
        
        Examples:
            >>> # Modo normal: 5 + 3 =
            >>> # first_number=5, operator="+", current_value="3"
            >>> # Ejecuta: add(5, 3) = 8
            >>> # Display: "8"
            >>> 
            >>> # Modo expresión: (2+3)*4 =
            >>> # expression = "(2+3)*4"
            >>> # Evalúa: eval("(2+3)*4") = 20
            >>> # Display: "20"
        """
        # Si estamos en modo expresión (con paréntesis)
        if self.use_expression_mode and self.expression:
            try:
                # Verificar que los paréntesis estén balanceados
                if self.expression.count('(') != self.expression.count(')'):
                    self.show_error('Paréntesis desbalanceados')
                    return
                
                # Por seguridad, solo permitir números y operadores básicos
                if not re.match(r'^[\d\s\+\-\*\/\^\(\)\.]+$', self.expression):
                    self.show_error('Expresión inválida')
                    return
                
                # Python usa ** para potencias, no ^
                expr = self.expression.replace('^', '**')
                
                # Calcular el resultado
                result = eval(expr)
                
                # Mostrar en pantalla
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                
                # Preparar para la siguiente operación
                self.current_value = str(result)
                self.expression = str(result)
                self.use_expression_mode = False
                
            except ZeroDivisionError:
                self.show_error("No se puede dividir por 0")
            except SyntaxError:
                self.show_error("Sintaxis incorrecta")
            except Exception as e:
                self.show_error("Error en la expresión")
            return

        # Modo normal (operaciones simples sin paréntesis)
        if self.first_number is not None and self.operator is not None and not self.current_value:
            self.show_error("Ingresa el segundo número")
            return
        
        elif self.first_number is not None and self.operator is not None and self.current_value:
            try:
                second_number = float(self.current_value)
                result = None
                
                if self.operator == '+':
                    result = add(self.first_number, second_number)
                elif self.operator == '-':
                    result = subtract(self.first_number, second_number)
                elif self.operator == '*':
                    result = multiply(self.first_number, second_number)
                elif self.operator == '/':
                    result = divide(self.first_number, second_number)
                elif self.operator == '^':
                    result = power(self.first_number, second_number)
                elif self.operator == 'max':
                    result = valor_maximo(self.first_number, second_number)
                elif self.operator == 'min':
                    result = valor_minimo(self.first_number, second_number)
                
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current_value = str(result)
                self.first_number = None
                self.operator = None
                
            except ValueError:
                self.show_error("Entrada inválida")
                return
            except ZeroDivisionError:
                self.show_error("No se puede dividir por 0")
                return
            except Exception as e:
                self.show_error(str(e))
                return


    def clear_click(self):
        """Limpia completamente el display y resetea el estado de la calculadora.
        
        Resetea tanto el modo normal como el modo de expresión. 
        
        Resetea:
            - current_value: cadena vacía
            - operator: None
            - first_number: None
            - expression: cadena vacía
            - use_expression_mode: False
            - Display: vacío
        
        Examples:
            >>> # Display muestra: "(2+3)*4"
            >>> # Usuario presiona C
            >>> # Display muestra: ""
        """
        self.current_value = ""
        self.operator = None
        self.first_number = None
        self.expression = ""
        self.use_expression_mode = False
        self.display.delete(0, tk.END)
        self.error_label.config(text="")  # Quitar cualquier mensaje de error


    def backspace_click(self):
        """Elimina el último carácter del display.
        
        Funciona en modo normal y en modo de expresión. 
        Si el display está vacío, no hace nada.
        
        Examples:
            >>> # Display muestra: "1234"
            >>> # Usuario presiona ⌫
            >>> # Display muestra: "123"
            >>> # Display muestra: "(2+3)"
            >>> # Usuario presiona ⌫
            >>> # Display muestra: "(2+3"
        """
        if self.use_expression_mode and self.expression:
            self.expression = self.expression[:-1]
            # Si ya no quedan paréntesis, volver al modo simple
            if '(' not in self.expression and ')' not in self.expression:
                self.use_expression_mode = False
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        elif self.current_value:
            self.current_value = self.current_value[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_value)


    def show_error(self, message):
        """Muestra un mensaje de error en el label de errores.
        
        Args:
            message (str): Mensaje de error a mostrar
        
        Examples:
            >>> self.show_error("División por 0")
            >>> # Label de error: "⚠️ División por 0"
            >>> self.show_error("Paréntesis desbalanceados")
            >>> # Label de error: "⚠️ Paréntesis desbalanceados"
        """
        self.error_label.config(text=f"⚠️ {message}")
        
        # El mensaje desaparece solo después de 3 segundos
        self.root.after(3000, lambda: self.error_label.config(text=""))
        
        # Limpiar todo para empezar de nuevo
        self.current_value = ""
        self.first_number = None
        self.operator = None
        self.expression = ""
        self.use_expression_mode = False

        # Limpiar el display también
        self.display.delete(0, tk.END)


    def unary_operation(self, func):
        """Ejecuta operaciones unarias (que solo necesitan un número).
        
        Args:
            func (str): Nombre de la función a ejecutar (abs, cos, sin, tan)
        
        Examples:
            >>> # Display: "-5"
            >>> # Usuario presiona "abs"
            >>> # Display: "5"
        """
        if self.current_value:
            if self.current_value == "-":
                self.show_error("Número incompleto")
                return
            try:
                result = None

                if func == 'abs':
                    result = abs_value(float(self.current_value))   
                #elif func == 'cos':

                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current_value = str(result)
                self.first_number = None
                self.operator = None

            except Exception as e:
                self.show_error(str(e))

    def scientific_click(self, func):
        """Maneja clicks de funciones científicas.
        
        Args:
            func (str): Función científica (abs, max, min)
        
        Examples:
            >>> # abs: Display "-5" → click "abs" → "5"
            >>> # max: "10" → "max" → "20" → "=" → "20"
        """
        
        # Funciones que solo necesitan un número
        if func in ['abs', 'cos', 'sin', 'tan']:
            self.unary_operation(func)
        # Funciones que necesitan dos números
        elif func in ['max', 'min']:
            self.operation_click(func)        


def main():
    root = tk.Tk()
    app = CalculatorGUI(root)  
    root.mainloop()

if __name__ == "__main__":
    main()