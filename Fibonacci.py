print("Hecho por: Azul Romero Perez")
print("Dado un numero obtener su serie Fibonacci")
def serie_Fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]

    fib_series = [0, 1]  
    for i in range(2, num):
        next_fib = fib_series[-1] + fib_series[-2] 
        fib_series.append(next_fib)

    return fib_series

num = int(input("Introduce un numero de la serie de Fibonacci: "))
print(serie_Fibonacci(num))
