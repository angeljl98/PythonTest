a=([1,2,3,4],[5,6,7,8],[9,10,11,12])
print(a)
b=a[0][0]
fila=a[:][1]
columna=a[0]
print(b)
print(columna)
o=columna.append(9) #agregar
o=columna.extend([1,2]) #agregar al final
o=columna.pop(4) #elimina el elemento 4
o=columna.sort() #ordena
try:
    o=columna.index(15) #trata de encontrar
except ValueError:
    print("15"+" is not here")
o=columna.remove(3) #eliminar de la lista
o=columna.insert(len(columna),99) #insertar al final
o=columna.count(99) #ver en donde está el 99
o=columna.reverse() #voltear un array
file1=a[0]
print("file1:"+str(file1))
file2=file1.copy()
p=file2.extend([88,77])
print("comparativa:")
print("file1:"+str(file1))
print("file2:"+str(file2))
o=columna.clear() #vaciars
print(columna)
word1="creative"
word2="reactive"
print(sorted(word1)==sorted(word2)) #sorted separa en vectores y además compara
