import tkinter as tk
from tkinter import ttk

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("320x400")
        
        # Estado
        self.current_value = ""
        self.operator = None
        self.first_number = None
        
        # UI
        self.create_widgets()
        
    def create_widgets(self):
        # Display
        self.display = tk.Entry(
            self.root,
            font=('Arial', 24),
            justify='right',
            bg='white',
            relief='sunken',
            bd=3
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=6, pady=6)
        
        # Estilo para los botones
        style = ttk.Style()
        # Un estilo simple para todos los botones
        style.configure('Calculator.TButton', 
                       font=('Arial', 14),
                       padding=6)
        
        # Definir botones y su posición
        buttons = [
            # Fila 1
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('⌫', 1, 3),
            # Fila 2-5
            ('max', 2, 0), ('min', 2, 1), ('abs', 2, 2), ('/', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
            ('^', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3)
        ]
        
        # Crear y posicionar botones
        for (text, row, col) in buttons:
            btn = ttk.Button(
                self.root,
                text=text,
                style='Calculator.TButton'
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
        
        # Configurar expansión de grid
        for i in range(6):  # 6 filas
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4 columnas
            self.root.grid_columnconfigure(i, weight=1)
            
        # Configurar expansión del root
        self.root.grid_rowconfigure(1, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        
    def button_click(self, value):
        """Maneja clicks de botones numéricos"""
        pass
        
    def operation_click(self, op):
        """Maneja clicks de operadores"""
        pass
        
    def equals_click(self):
        """Calcula resultado usando calculator.py"""
        pass
        
    def clear_click(self):
        """Limpia display"""
        pass

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()