#!/usr/bin/env python3
"""Archivo principal de ejemplo para el proyecto Team Practice.

Demuestra cómo usar los módulos del proyecto y cómo estructurar
un punto de entrada principal.
"""

from calculator import add, subtract, multiply, divide, power, valor_maximo, valor_minimo, abs_value

def main():
    """Función principal del programa."""
    print("\n=== Team Practice - Calculadora Demo ===")
    print("Este es un ejemplo de cómo usar el módulo calculator.\n")
    
    # Ejemplos de uso de las funciones
    print("Ejemplos de operaciones:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"5 * 6 = {multiply(5, 6)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"2 ^ 4 = {power(2, 4)}")
    print(f"-7 abs = {abs_value(-7)}")
    print(f"Valor máximo entre 10 y 20 = {valor_maximo(10, 20)}")
    print(f"Valor mínimo entre 10 y 20 = {valor_minimo(10, 20)}")
    
    # Ejemplo de manejo de errores
    print("\nEjemplo de manejo de errores:")
    try:
        result = divide(10, 0)
        print(f"10 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    
    # Calculadora interactiva simple
    print("\n=== Calculadora Interactiva ===")
    print("Operaciones disponibles: +, -, *, /, ^, max, min")
    print("Escribe 'quit' para salir\n")
    
    while True:
        try:
            user_input = input("Ingresa una operación (ej: 5 + 3): ").strip()
            
            if user_input.lower() == 'quit':
                print("\n¡Hasta luego!")
                break
            
            # Parse simple de la entrada
            parts = user_input.split()
            
            # Realizar la operación formato: "num1 + operador + num2"
            if len(parts) == 3:

                num1, operator, num2 = parts
                num1, num2 = float(num1), float(num2)
            
                if operator == '+':
                   result = add(num1, num2)
                elif operator == '-':
                    result = subtract(num1, num2)
                elif operator == '*':
                    result = multiply(num1, num2)
                elif operator == '/':
                    result = divide(num1, num2)
                elif operator == '^':
                    result = power(num1, num2)
                elif operator == 'max':
                    result = valor_maximo(num1, num2)
                elif operator == 'min':
                    result = valor_minimo(num1, num2)
                else:
                    print(f"Operador '{operator}' no válido")
                    continue
                print(f"Resultado: {result}\n")
                
                
                # Realizar la operación formato: "num + funcion"
            elif len(parts) == 2:

                num, function = parts
                num = float(num)
                
                if function == 'abs':
                   result = abs_value(num)
                else:
                   print(f"Función '{function}' no válida")
                   continue
                print(f"Resultado: {result}\n")
            else:
                print("Formato inválido")
                continue
            
            
        except ValueError:
            print("Error: Ingresa números válidos")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()