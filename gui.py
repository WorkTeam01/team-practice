import tkinter as tk
from calculator import (
                add, subtract, multiply, divide, power, valor_maximo, valor_minimo, abs_value
            )

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("330x420")
        self.root.configure(bg="#1E1E1E")  # Fondo más elegante
        
        # Estado
        self.current_value =  "" 
        self.operator =  None
        self.first_number =  None

        # Interfaz de usuario
        self.create_widgets()

    def create_widgets(self):

        COLORS = {
            "bg": "#1E1E1E",
            "display": "#2B2B2B",
            "numbers": "#3A3A3A",
            "operators": "#FF8C00",  # naranja más suave (Apple)
            "equal": "#FF8C00",
            "clear": "#6E6E6E",
            "text": "#FFFFFF"
        }

        # ==== DISPLAY ====
        self.display = tk.Entry(
            self.root,
            font=("Arial", 28, "bold"),
            justify="right",
            bg=COLORS["display"],
            fg=COLORS["text"],
            relief="flat",
            bd=10
        )
        self.display.grid(row=0, column=0, columnspan=4,
                          sticky="nsew", padx=10, pady=10)

        # ==== BOTONES ====
        buttons = [
            ('C', 1, 0, COLORS["clear"]),
            ('(', 1, 1, COLORS["numbers"]),
            (')', 1, 2, COLORS["numbers"]),
            ('⌫', 1, 3, COLORS["clear"]),

            ('max', 2, 0, COLORS["numbers"]),
            ('min', 2, 1, COLORS["numbers"]),
            ('abs', 2, 2, COLORS["numbers"]),
            ('/', 2, 3, COLORS["operators"]),

            ('7', 3, 0, COLORS["numbers"]),
            ('8', 3, 1, COLORS["numbers"]),
            ('9', 3, 2, COLORS["numbers"]),
            ('*', 3, 3, COLORS["operators"]),

            ('4', 4, 0, COLORS["numbers"]),
            ('5', 4, 1, COLORS["numbers"]),
            ('6', 4, 2, COLORS["numbers"]),
            ('-', 4, 3, COLORS["operators"]),

            ('1', 5, 0, COLORS["numbers"]),
            ('2', 5, 1, COLORS["numbers"]),
            ('3', 5, 2, COLORS["numbers"]),
            ('+', 5, 3, COLORS["operators"]),

            ('^', 6, 0, COLORS["operators"]),
            ('0', 6, 1, COLORS["numbers"]),
            ('.', 6, 2, COLORS["numbers"]),
            ('=', 6, 3, COLORS["equal"]),
        ]

        # Conectar cada botón con su respectiva función
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
            elif txt in ['abs', 'max', 'min']:
                cmd = lambda t=txt: self.scientific_click(t)
            else:
                cmd = None  # Por ahora, otros botones sin funcionalidad
            
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

        # Expandir filas y columnas
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        

    def number_button_click (self , valor):
        """Maneja clicks de botones numéricos.
        
        Args:
            value (str): Dígito presionado (0-9)
        
        Examples:
            >>> # Usuario presiona 2, 3, 5
            >>> # Display muestra: "235"
        """
        self.current_value += str(valor)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_value)
    

    def decimal_click(self):
        """Maneja click del botón decimal.
        
        Agrega un punto decimal solo si no existe uno ya en el número actual.

        Examples:
            >>> "5" → click(.) → "5."
            >>> "5." → click(.) → "5." (no cambia)
            >>> "" → click(.) → "0."
        """
        if '.' not in self.current_value:
            if not self.current_value:
                self.current_value = "0"
            self.current_value += '.'
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_value)


    def operation_click(self, operation):
        """Maneja clicks de operadores matemáticos.
    
        Guarda el primer número y operador para calcular cuando 
        el usuario presione "=".
        
        Args:
            operation (str): Operador (+, -, *, /, ^, max, min)
        
        Examples:
            >>> # Usuario: 5 + 3 =
            >>> # 1. Ingresa "5"
            >>> # 2. Click "+": first_number=5, operator="+"
            >>> # 3. Ingresa "3"  
            >>> # 4. Click "=": calcula 5+3=8
        """
        if self.current_value:
            # Si hay operación pendiente, calcularla primero
            if self.first_number is not None and self.operator:
                self.equals_click()
            
            self.first_number = float(self.current_value)
            self.operator = operation
            self.current_value = ""


    def equals_click(self):
        """Calcula el resultado de la operación actual.
        
        Usa las funciones de calculator.py para realizar el cálculo.
        
        Examples:
            >>> # Usuario: 5 + 3 =
            >>> # first_number=5, operator="+", current_value="3"
            >>> # Ejecuta: add(5, 3) = 8
            >>> # Display: "8"
        """
        if self.current_value and self.first_number is not None and self.operator:
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
                
            except ZeroDivisionError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error: División por 0")
                self.current_value = ""
                self.first_number = None
                self.operator = None


    def clear_click(self):
        """Limpia completamente el display y resetea el estado de la calculadora.
        
        Resetea:
            - current_value: cadena vacía
            - operator: None
            - first_number: None
            - Display: vacío
        
        Examples:
            >>> # Display muestra: "235"
            >>> # Usuario presiona C
            >>> # Display muestra: ""
        """
        self.current_value = ""
        self.operator = None
        self.first_number = None
        self.display.delete(0, tk.END)


    def backspace_click(self):
        """Elimina el último carácter del display.
        
        Si el display está vacío, no hace nada.
        
        Examples:
            >>> # Display muestra: "1234"
            >>> # Usuario presiona ⌫
            >>> # Display muestra: "123"
            >>> # Usuario presiona ⌫ tres veces más
            >>> # Display muestra: ""
        """
        if self.current_value:
            self.current_value = self.current_value[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_value)


    def unary_operation(self, func):
        if self.current_value:
            try:
                result = None

                if func == 'abs':
                    result = abs_value(self.first_number)
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
        
        # Funciones de 1 argumento se calculan inmediatamente
        if func in ['abs', 'cos', 'sin', 'tan']:
            self.unary_operation(func)
        # Funciones de 2 argumentos usan la lógica de operación normal
        elif func in ['max', 'min']:
            self.operation_click(func)        



def main():
    root = tk.Tk()
    app = CalculatorGUI(root)  
    root.mainloop()

if __name__ == "__main__":
    main()
