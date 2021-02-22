# 	Goal
# The goal is to remove all duplicate characters (case sensitive), but the last one.
#
# Examples: abcaba becomes cba, Aa stays Aa, hello world!!!! becomes he world!.
# Input
# Line 1: Input string S.
# Output
# Line 1: String with duplicate characters removed.
# Constraints
# S contains no Unicode characters.
# Example
# Input
# abcaba
# Output
# cba
from string import ascii_letters
s = input()
def invertir_cadena(cadena):
    return cadena[::-1]
def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida
s="Hola Mundo"
s=invertir_cadena(s)
ct=1
for x in String:
    ct+=1
    ct2=0
    for y in s:
        if y=
