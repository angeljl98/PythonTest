print('xyyzxxyxyy'.lstrip('xyy'))
print(min([3,5,25,1,3]))
if (9<0) and (0<-9):
    print("hello")
elif (9>0) or False:
    print("good")
else:
    print("bad")
a={1:"A",2:"B",3:"C"}
b=a.copy()
b[2]="D"
print(a)
print('helo'.partition('lo'))
print('abcdefcdghcd'.split('cd',0))
print('abcd'.translate('a'.maketrans('abc','bcd')))
str1='hello'
str2=','
str3='world'
print(str1[-1:])
for index in range(10):
    if index==5:
        break
    else:
        print(index)
else:
    print("Here")
statement="hello world"
result=[(i.upper(),len(i)) for i in statement]
print(result)
word1="Apple"
word2="Apple"
list1=[1,2,3]
list2=[1,2,3]
print(word1 is word2)
print(list1 is list2)
a={1:"A",2:"B",3:"C"}
#del a #borra algo en el diccionario
print(a)
s1="a"
s2="b"
s3=s1+s2
print(s3+"---")
def decorator1(x):
    def f1(a,b):
        print("hello")
        if b==0:
            print("NO--")
            return
        return decorator1(a,b)
    return f1
@decorator1
def decorator1(a,b):
    return a%b
#decorator1(4,0)
#
#print('There are %g %d birds.' %4 %blue)
#print('There are %d %s birds.' %(4,blue))
#print('There are %d %s birds.' 4,blue)
#print('There are %d %s birds.' %[4,blue])
print("---")
alphabets="abcdef"
i="i"
while i in alphabets:
    print(i,end=" ")
print("---")
s=["silicon","valley","sf"]
print([(w.upper(),len(w)) for w in s])
x=-122
print("-%006d"%x)
t1=(1,2,4,3)
t2=(1,2,3,4)
print(t1 < t2)
a=(2,3,4)
print(str(sum(a,3)))

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

print('{:,}'.format(1112223334))
d={"john":40,"peter":45}
print("john" in d)

print("---")
a={1:"A",2:"B",3:"C"}
print(a.get(1,4))
print("---")
x1=2
for i in range(x1):
    x1-=2
    print(x1)
print("---")
def cube(x):
    return x*x*x
x2=cube(3)
print(x2)
print("---")
#nums=[0,1,2,3]
#index=-2
#for index not in nums:
#    print(index)
#    index +=1
print("---")
a=[1,4,3,5,2]
b=[3,1,5,2,4]
print(a==b)
print(set(a)==set(b))
print("---")
print("D",end=' ')
print("C",end=' ')
print("B",end=' ')
print("A",end=' ')
print("---")
print(round(0.5)-round(-0.5))
print("---")
t=32.00
print([round((i1-32)*5/9)] for i1 in t)
