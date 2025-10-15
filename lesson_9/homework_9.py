#1.Создайте словарь, в котором хранятся названия фруктов и их цены за 1 кг.
dict_price = {"Апельсины": 120, "Бананы": 110, "Яблоки": 95}
dict_price.update({"Груши": 34})
print(dict_price)

#2. Дан словарь с оценками студентов:
grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
for key, value in grades.items():
    if value >= 4:
        print(key)
    continue

#3. Создайте словарь, содержащий название стран в качестве ключей и их столицы в качестве значений.
dict_capitals = {"Россия": "Москва", "Беларусь": "Минск", "Великобритания": "Лондон"}
country = input("Введите название страны: ")
result = (f"Столица - {dict_capitals[country]}") if country in dict_capitals else "Страна не найдена"
print(result)

#4. Дан список студентов и их курсов:
students = [
    ("Анна", "Python"),
    ("Борис", "Java"),
    ("Виктор", "Python"),
    ("Галина", "C++"),
    ("Дмитрий", "Python")
]
dict_stud = {}
for key, value in students:
    if value not in dict_stud:
        dict_stud[value] = []
    dict_stud[value].append(key)
print(dict_stud)

5. Создайте словарь, содержащий оценки студентов:
grades = {"Анна": 5, "Борис": 4, "Виктор": 1, "Галина": 3, "Дмитрий": 2}
min_grade = min(grades, key=grades.get)
remove_stud = grades.pop(min_grade)
print(grades)

# 6. Дан список студентов:
i = 25
students = ["Анна", "Борис", "Виктор", "Галина"]
dict_students = dict.fromkeys(students)
print(dict_students)
for item in dict_students:
    dict_students[item] = i
    i += 3
print(dict_students)

#7. Дан словарь с курсами валют:
result = ""
exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
currency = input("Введите валюту: ")
if currency in exchange_rates:
    result = f"Курс - {exchange_rates[currency]}"
else:
    result = "Неизвестная валюта"
    exchange_rates[currency] = None
print(result)

#8. Создайте два словаря:
dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
dict1.update(dict2)
print(dict1)

# 1. Создайте кортеж из пяти элементов (разных типов данных).
t = (1, 2, 1,434, 64564, 46535, "fw", [6,6,6,3,'sdfsd'])
print(t[1])
print(t[-1])

# 2. Дан кортеж чисел:
nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
count = 0
for num in nums:
    if num == 4:
        count += 1
    continue
print(count)
print(nums.index(7))

# 3. Преобразуйте следующий список в кортеж:
lst = ["Python", "Java", "C++", "JavaScript"]
lst1 = tuple(lst)
print(lst1)
print("C++" in lst1)

# 4. Создайте кортеж с числами от 1 до 10.
nums = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(nums[0:3])
print(nums[len(nums)-3 :])
print(nums[::2])

# 5. Создайте кортеж, содержащий вложенные список и словарь.
t = (1, 46535, "fw", [6,6,6,3,'sdfsd'], {"a":1, "b":2, "c":3, "d":4})
t[3].append("новый элемент")
print(t)