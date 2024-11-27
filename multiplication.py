def multiply(a, b):
    """
    Multiplica dos números y devuelve el resultado.
    """
    return a * b

if __name__ == "__main__":
    import sys
    # Asegúrate de que hay suficientes argumentos
    if len(sys.argv) != 3:
        print("Uso: python multiplication.py <num1> <num2>")
        sys.exit(1)

    # Convierte los argumentos a enteros
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    # Imprime el resultado
    print(f"El resultado de {a} x {b} es: {multiply(a, b)}")
