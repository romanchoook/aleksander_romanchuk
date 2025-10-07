print("строки в Python")

###1
print("Задание 1:")
s1 = "Python"
s2 = 'Программирование'
print(s1)
print(s2)
s3 = """Многострочная 
строка"""
print(s3)
empty = ""
print(len(empty))

###2
print("Задание 2:")

first_name = "Иван"
last_name = "Петров"
full_name = first_name + " " + last_name
print(full_name)

###3
print("Задание 3:")

s = "Возраст: "
age = 25
print(s + str(age))

###4
print("Задание 4:")
print("ха " * 5)
# print("ха " * 2.5) - в консоль возвращается ошибка "TypeError: can't multiply sequence by non-int of type 'float'" - строку можно умножить только на целое число

###5
print("Задание 5:")
text = "Привет, мир!"
print(len(text))
empty1 = ""
print(len(empty1))

###6
print("Задание 6:")
sentence = "Я изучаю Python"
print("Python" in sentence)
print("Java" in sentence)

###7
print("Задание 7:")
a = "apple"
b = "banana"
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

###8
print("Задание 8:")

print(ord('A'))
print(ord('a'))
print(ord('Я'))
