# Fibonacci

# Primera versión -> con tres variables

iteraciones = int(input("Ingrese la cantidad de numeros de la secuencia que desea calcular: ")) 
a = 0
b = 1
c = 0

for i in range(iteraciones):
    print(a, end=" ")
    c = a + b
    a, b = b, c



# Segunda versión -> con dos variables, aprovechando una asignación simultánea de variables

iteraciones = int(input("Ingrese la cantidad de numeros de la secuencia que desea calcular: ")) 
a = 0
b = 1

for i in range(iteraciones):
    print(a, end=" ")
    a, b = b, a+b



# Tercera versión -> hasta llegar a un número concreto

ultimo_numero = int(input("Ingrese el último número de la secuencia que desea calcular: ")) 
a = 0
b = 1

while a <= ultimo_numero:
    print(a, end=" ")
    a, b = b, a+b



# Cuarta versión -> funciones (de la segunda y tercera versión)

def fibonacci_1(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b

def fibonacci_2(max):
    a, b = 0, 1
    while a <= max:
        print(a, end=" ")
        a, b = b, a+b

print("")
fibonacci_1(18)
print("")
fibonacci_2(1597)
print("")
print("")



# Quinta versión -> función recursiva

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(18):
    print(fibonacci(n), end=" ")