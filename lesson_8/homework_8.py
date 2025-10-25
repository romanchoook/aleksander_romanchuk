#1. Пройти по списку с помощью итератора
spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
it_spisok = iter(spisok)
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))
print(next(it_spisok))

#2. Итератор для строки
stroka = "Привет"
it_stroka = iter(stroka)
print(next(it_stroka))
print(next(it_stroka))
print(next(it_stroka))
print(next(it_stroka))
print(next(it_stroka))
print(next(it_stroka))

#Задачи по теме "Генераторы списков (List Comprehensions)"
#1
N = int(input("Введите N: "))
result = [num ** 2 for num in range(1, N + 1)]
print(result)

#2
result = [i for i in range(-10,11) if i % 2 == 0]
print(result)

#3
spisok_slov = ['один', "два", "три", "четыре"]
new_spisok = [len(x) for x in spisok_slov]
print(new_spisok)

#4
spisok_1 = ["четное" if num % 2 == 0 else "нечетное" for num in range(1, 21)]
print(spisok_1)

#5
result = []
obj = [17, 'строка', [1, 2, 3]]
is_iter = [hasattr(i, '__iter__') for i in obj]
print(is_iter)