import tkinter as tk
from tkinter import ttk

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

        for (txt, r, c, color) in buttons:
            # Conectar solo botones numéricos
            if txt.isdigit():
                cmd = lambda t=txt: self.number_button_click(t)
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
        

    def number_button_click ( self , valor ):
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


    def  operación_clic ( self , op ):
        """Maneja clics de operadores"""
        pass


    def  equals_click ( self ):
        """Calcula el resultado usando calculadora.py"""
        pass


    def  clear_click ( self ):
        """Exhibición de Limpia"""
        pass



def main():
    root = tk.Tk()
    app = CalculatorGUI(root)  
    root.mainloop()

if __name__ == "__main__":
    main()
