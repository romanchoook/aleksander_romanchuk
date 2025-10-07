###1
name = "Александр"
age = 30
height = 186.0
print ("Меня зовут", name, "мне", age, "лет и мой рост составляет", height, "см")
###2
x = 10
print(x,type(x))
x = 25.5
print(x,type(x))
x = "Python"
print(x,type(x))
###3
a = 7
b = a
print(a,b)
a = 10
print("b =", b) #Значение переменной b остается равное 7, так как ссылается на значение переменной a = 7 (до перезаписи нового значения)
###4
x = y = z = 100
print("x =", x, "y =", y, "z =", z)
print(id(x))
print(id(y))
print(id(z)) #их ID совпадают, так как при каскадном присваивании переменные x, y и z ссылаются на один и тот же объект

x, y, z = 1, 2, 3
print("x =", x, "y =", y, "z =", z)
print(id(x))
print(id(y))
print(id(z)) #их ID отличаются, так как при множественном присваивании каждая переменная ссылается на свой индивидуальный объект

###5
a = 5
b = 10
a, b = b,a
print(a,b)

###6
# True = "true"
# print = "Print"
# if = "If"   - нельзя использовать имена переменных из списка внутренних зарезервированных слов в Python

import keyword
print(keyword.kwlist)

###7
var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1))
print(type(var2))
print(type(var3))
var1 = "любое строковое значение"
print(type(var1))


###8
_prmn1 = 365
Prmnn1 = 36.6
prmnn1 = "переменная3"
_prmnn2 = "test"
_prmnn3 = 12
переменная = 10 #работает
