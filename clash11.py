# The program:
# Your program must find the greatest common divisor for two integers.
#
# The greatest common divisor of two integers is the largest positive integer that divides the numbers without a remainder.
#
# INPUT:
# Two integer numbers separated by a whitespace, a and b.
#
# OUTPUT:
# The greatest common divisor of a and b.
#
# CONSTRAINTS:
# 0 < a,b ≤ 1000000
#
# EXAMPLE:
# Input
# 169 104
# Output
# 13
#
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# 
# a, b = [int(i) for i in input().split()]
#
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

import sys
import math

# print("answer")
def primo(num):
 if num < 2: #si es menor de 2 no es primo, devolverá Falso
   return False
 for i in range(2, num): #un ciclo desde el 2 hasta el num de entrada
   if num % i == 0: #si el resto da 0 no es primo, devuelve Falso
    return False
 return True #de lo contrario devuelve Verdadero

def get_prime_numbers(max_number):
    # Crear una lista que contiene el estado (tachado/no tachado)
    # de cada número desde 2 hasta max_number.
    numbers = [True, True] + [True] * (max_number-1)
    # Se comienza por el 2. Esta variable siempre tiene un
    # número primo.
    last_prime_number = 2
    # Esta variable contiene el número actual en la lista,
    # que siempre es un múltiplo de last_prime_number.
    i = last_prime_number

    # Proceder siempre que el cuadrado de last_prime_number (es decir,
    # el último número primo obtenido) sea menor o igual que max_number.
    while last_prime_number**2 <= max_number:
        # Tachar todos los múltiplos del último número primo obtenido.
        i += last_prime_number
        while i <= max_number:
            numbers[i] = False
            i += last_prime_number
        # Obtener el número inmediatamente siguiente al último
        # número primo obtenido (last_prime_number) que no esté tachado.
        j = last_prime_number + 1
        while j < max_number:
            if numbers[j]:
                last_prime_number = j
                break
            j += 1
        i = last_prime_number

    # Retornar todas los números de la lista que no están tachados.
    return [i + 2 for i, not_crossed in enumerate(numbers[2:]) if not_crossed]

print(get_prime_numbers(50))

# a=list(map(int,input().split()))
a=[169,104]
for i in range(max(a),0,-1):
 if a[0]%i==0 and a[1]%i==0:
  print(i)
  break
