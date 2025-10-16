# 1. Создайте множество с элементами .
set_1 = {1,2,3,4,("a","b","c","d")}
print(set_1)
set_1.add(6)
print(set_1)
set_1.add(2)
print(set_1)

# 2. Создайте множество из списка городов:
set_cities = {"Москва", "Владимир", "Люберцы"}
print(set_cities)
print(len(set_cities))

# 3. Создайте множество с числами от 1 до 10.
set_num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_num.remove(5)
set_num.discard(15)
print(set_num)

# 4. Преобразуйте строку "abrakadabra" в множество символов.
str_4 = "abrakadabra"
set_4 = set(str_4)
print(set_4)
print(len(set_4))

#5. Создайте пустое множество и попробуйте добавить в него следующие элементы:
set_5 = set()
set_5.add(10)
set_5.add("hello")
set_5.add((1, 2, 3))
# set_5.add([4, 5, 6]) - нельзя добавить изменяемые типы данных (set, list, dict)

##6. Создайте 2 множества, в которых совпадают 2 элемента
a = {1,3,5,7,9}
b = {9,7,2,4,6,8}
res = a & b
print("Пересечение a и b: ", res)
res = a.intersection(b)
print("Также пересечение равно: ", res)
res = a | b
print("Объединение равно: ", res)
res = a - b
print(res)
res = b - a
print(res)
res = a ^ b
print(res)

#7. Создайте два множества из чисел 1 до 10:
even_numbers = {1, 3, 5, 7, 9}
add_numbers = {2, 4, 6, 8, 10}
res = even_numbers & add_numbers # set() - пустое мн - во, потому что нет пересекающихся элементов
print(res)
res = even_numbers | add_numbers # - множество с числами от 1 до 10, записались уникальные значения (то есть все из обоих)
print(res)

# 8. Даны множества студентов, записавшихся на курсы:
python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
print("На оба курса записаны:", python_students & java_students)
print("Только на один курс записаны: ", python_students ^ java_students)
print("Хотя бы на один курс записаны: ", python_students | java_students)

## 9. Даны множества слов:
text1 = set("программирование")
text2 = set("автоматизация")
print(text1 | text2)
print(text1 - text2)
print(text1 ^ text2)

##1. Создайте множество из квадратов чисел от 1 до 10, но только для четных чисел.
set_1 = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print(set_1)

##2. Дан список:
words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
res = {i.upper() for i in words}
print(res)

##3. Дан словарь:
grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
res = {key: ("отлично" if value >=  80 else "удовлетворительно") for key, value in grades.items()}
print(res)

##4. Дано множество слов:
text = {"Python", "automation", "programming", "testing"}
text_dict = {key: len(key) for key in text}
print(text_dict)

#5. Создайте вложенный словарь, где ключи – числа от 1 до n (для примера пусть n = 10), а значения – множества квадратов чисел от 1 до ключа.
n = int(input("Введите n: "))
res = {
    k : {v ** 2 for v in range(1, k + 1)}
    for k in range(1, n + 1)
}
for key, value in res.items():
    print(key, sorted(value))