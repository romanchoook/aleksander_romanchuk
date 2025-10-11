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

print([1, 2, 4] + [4, 5, 6])
print(["Python", "rocks"] * 2)

print([1, 2, 3] == [1, 2, 3])
print([10, 5, 3] > [5, 10, 3])
#print([1, 2, 3] > [1, 2, "abc"]) - возвращается ошибка '>' not supported between instances of 'int' and 'str' - нельзя сравнить строку с целым числом

chars = list("Python")
print(max(chars))
print(min(chars))
#print(sum(chars[:])) - unsupported operand type(s) for +: 'int' and 'str'. не получится сложить строковые составляющие, их можно либо объединить, либо преобразовать в числа и только тогда сложить


#Методы списков
numbers = [5, 10, 15]
numbers.append(20)
numbers.insert(1, 7)
numbers.append("Python")

numbers.remove(10)
print(numbers.pop(-1))
numbers.pop(1)
numbers.clear()

letters = ["a", "b", "c"]
letters_1 = letters.copy()
letters_2 = list(letters)
print(f"копия и оригинальный список - разные объекты? - {id(letters_1) != id(letters_2) != id(letters)}")

marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks.count(3))
print(6 in marks)
print(marks.index(5))


nums = [8, 2, 5, 1, 7]
nums.sort()
nums.sort(reverse=True)
nums.reverse()

cities = ["Москва", "Якутск", "Санкт-Петербург"]
cities.sort()
sort_cities = sorted(cities) # - sort изменяет исходный список, получается что новый список по содержанию равен исходному

chars = list("programming")
print(chars.count("g"))
chars.reverse()
chars.sort() #- список отсортируется в алфавитном порядке


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix)
print(matrix[1])
print(matrix[2][0])
matrix[0] = len(matrix[0]) * [0]
matrix[1][-1] = "Python"