cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [365, 'строка', False, 36.5]

print(cities[0])
print(numbers[-1])
#print(cities[10]) - ошибка list index out of range - такого индекса в списке cities не существует

numbers[1] = 10
mixed[-1] = "Python"
print(len(numbers))
print(f"Максимальное значение равно {max(numbers)}, минимальное значение равно {min(numbers)}")
print(sum(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

obed = [1, 2, 3] + [4, 5]
zad5 = ["Python", "is", "awesome"] * 3

print(3 in numbers)
print('Москва' in cities)
print([1, 2] in mixed)

del numbers[2]
del cities[-1]

str8 = "Python"
spisok8 = list(str8)
print(f"Максимальный символ в списке равен \"{max(spisok8)}\", минимальный символ в списке равен \"{min(spisok8)}\"")
#print(sum(spisok8)) - sum не может суммировать строки внутри списка, ошибка unsupported operand type(s) for +: 'int' and 'str'


cities1 = ["Волгоград", "Сан-Франциско", "Белград", "Санкт-Петербург"]
cities2 = cities1[::]
print(f"Два списка являются разными объектами? - {id(cities1) != id(cities2)}")


print(cities1[1], cities1[2])
print(cities1[2:])
print(cities1[:3])
print(cities1[:])
print(cities1[-2:])


print(cities1[1::2]) # - возможно неверно, но начиная с нулевого выводится сначала первый элемент, потом третий. Раз нужен каждый второй - решил начать с индекса 1
print(cities1[::-1])
print(cities1[-2::-2]) # - ты же логика :)

cities1[1:3] = ["Сочи", "Нижний Новгород"]
cities1[1::2] = ["Город"] * len(cities1[1::2])
cities1[1:3] = "Волгоград", "Омск"

#остановился на 5. Операции с объединением списков