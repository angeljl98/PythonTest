import random
print(chr(70)) #convierte numero ascii a letra
print(int("15",16)) #convierte hexadecimal a decimal
print(random.randint(10,20))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
#map genera un resultado de una operación matemática
print(list(result))
