###1
print("Задание 1:")
s = "Программирование"
print(s[0])
print(s[-1])
print(s[2], s[-2])

###2
print("Задание 2:")

#print(s[100]) # - возвращается ошибка "string index out of range", данный индекс за пределами существующих (у переменной s)
print(s[len(s) - 1])

###3
print("Задание 3:")

t = print(s[: 6])
m = print(s[-5 :])
k = print(s[ 2 : 8])
l = print(s[1::2]) # - каждый второй, значит индекс первого нужного символа = 1
r = print(s[::-1])

###4
print("Задание 4:")

print(s[0::3])
print(s[::-2])

###5
print("Задание 5:")

#s[0] = "п" - возвращается ошибка "'str' object does not support item assignment" - string неизменяемый тип данных
s2 = ("П" + s[1:])

###6
print("Задание 6:")

word = "abcdefgh"
word[2:5]
print(word[::-1])
print(word[1:-1])
