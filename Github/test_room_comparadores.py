print(7==9)
print(7!=9)
print(7>=9)
print(7<=9)
def funcion(x,y,z): #definir funcion
    r=x+y+z
    return r
print(funcion(1,2,3,))
c=0
if 5>4:
    print("5>4")
elif 5>3:
    print("5>3")
else:
    print("")

while (c<5): #rutina del while condition:
    pass
    print(str(c))
    c+=1 #incremento
class punto:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
pto_1=punto(3.0,3.0,3.0)
print("dist"+str(dist=punto.xy))
print(funcion(pto_1.x,pto_1.y,pto_1.z))

def espar(x): #función par
    z = {
         0: True,
         1: False,
    }
    return z.get((x%2),"Empty")
# uso de
print(espar(2))

for i in [1,5,9]:
    print(str(i))
for i in (1,5,9):
    print(str(i))

s1="A B C"
s2="B C A"
a=[]

def word2number(x): #convierte la palabra a ascii
    r=[]
    for i in x:
        v=r.append(int(ord(i)))
    return r
v=word2number(s1)
print(v)
u=v.copy()
w=v.sort()
print(v)
