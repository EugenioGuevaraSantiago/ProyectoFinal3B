print("Hecho por Eugenio Guevara Santiago")
def triangulo_de_pascal(filas):
    i = 0 
    while i < filas:
        valor = 1  
        j = 0  
        while j <= i:
            if j > 0:
                valor = valor * (i - j + 1) // j
            print(valor, end=" ")  
            j += 1 
        print() 
        i += 1  
n = int(input("Ingresa número de filas del Triángulo de Pascal: "))
triangulo_de_pascal(n)
