print("Hecho por: Romero Perez Azul")
print("Triangulo de Pascal")
def factorial(num):
    if num > 0:
        return int(num*factorial(num-1))
    else:
        return 1

def combinador(num1, num2):
    return int(factorial(num1) / (factorial(num2)*factorial(num1-num2)))

def crear_piramide(n_filas):
    for fila in range(n_filas):
        for i in range(n_filas-fila+1):
            print(" ", end="")
        if fila == 0:
            print("1 1")
        else:
            for i in range(fila+2):
                print(combinador(fila+1, i), end=" ")
            print()

crear_piramide(int(input("Indica el número de filas que desea obtener: ")))