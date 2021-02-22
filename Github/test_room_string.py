#!/usr/bin/env python
# -*- coding: cp1252 -*-

from string import ascii_letters
print(ascii_letters)
x1="{} es el primer valor, {} el segundo y {} el tercero"
print (x1.format("1er", "2do", "3ro")) #formateo de strings
txt="-"
x2=txt.join("123456") #coloca un texto - en el intermedio
print(x2) #union de strings
x3="Esto es un párrafo"
print(x3[2:]) #imprime del caracter 2 hasta el final
print(x3.split( )) #separa en vectores una oración
print(x3.replace(" ","-")) #reemplaza un parametro por otro
print(x3.strip("Esto")) #eliminar
print(x3.strip("Esto")) #eliminar
print(x3.lower()) #pone en minusculas
print(x3.encode("ascii","ignore")) #codifica
print(x3.startswith("Esto")) #dice si comienza, devuelve un True
print(x3.find("á")) #dice el lugar donde está el valor
#print(x3.decode("ascii","ignore"))
print(x3.upper()) #pone en mayúsculas
print(x3.endswith("afo")) #dice si termina, devuelve un True
print(x3.rstrip("fo")) #remueve al final, se usa para puntos o comas, o espacios
print(x3.splitlines()) #divine en líneas si tiene el /n
print(x3.count("s")) #cuenta la cantidad de veces que está
print(x3.index("á")) #es igual que find, pero si no lo encuentra hace una excepción
print(x3.isdigit()) #dice si es un dígito
print(x3.lstrip("E")) #remueve el inicio
print(x3.zfill(25)) #rellena con 0 los espacios faltantes
print(x3.ljust(30,"*")) #rellena a la derecha con los caracteres restantes
print(x3.title()) #imprime todas las palabras con el inicio en mayúsculas
