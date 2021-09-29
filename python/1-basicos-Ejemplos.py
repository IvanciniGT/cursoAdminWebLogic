# Definir una funcion que devuelva el máximo (mayor) de 2 números

def maximo(numero1,numero2):
    if numero1>numero2:
        return numero1
    return numero2

print(maximo(9,-18))

def maximoDeTres(numero1,numero2,numero3):
    return maximo(numero1, maximo(numero2,numero3))
    
print(maximoDeTres(9,-18,17))

# Factorial número    5! = 5 x 4 x 3 x 2 x 1
# Factorial número    5! = 1 x 2 x 3 x 4 x 5

# Factorial número    5! = 5 x 4!


#                     n! = n x (n-1)!      Si n > 0
#                     0! = 1               Por definición
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
    
print(factorial(5))
print(factorial(6))