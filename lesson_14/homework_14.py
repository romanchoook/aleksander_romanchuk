"""1. Импортируйте только функции sqrt и pow из модуля math и вычислите:
Квадратный корень из 64
5 в степени 3
Ожидаемый вывод:
8.0
125.0"""

from math import sqrt, pow

print(sqrt(64))
print(pow(5, 3))


"""2. Импортируйте модуль random и:
Выведите случайное число от 1 до 10
Выберите случайный элемент из списка [Python, Java, C++]
Ожидаемый вывод:
Случайное число: 7  # (значение может отличаться)
Выбранный язык: Python  # (значение может отличаться)"""

import random

print(random.randint(1,10)) # тут думал что граница диапазона не входит и с начала ввел 11, опытным путем понял что граница входит и вернул 10
print(random.choice(["Python", "Java", "C++"]))

"""3. Создайте свой модуль my_module.py, в котором будут функции:
add(a, b): складывает два числа
multiply(a, b): умножает два числа
Cоздайте my_module.py в той же папке!"""
import my_module

print(my_module.add(3,5))
print(my_module.multiply(4, 6))

"""4. Создайте два Python-файла:

utils.py – в нем создайте функцию greet(name), которая выводит приветствие.
main.py – в нем импортируйте greet() из utils.py и вызовите её.
Пример вызова в main.py
from utils import greet

greet("Алексей")  # Привет, Алексей!
Запустите main.py и убедитесь, что импорт работает!"""


"""5. Напишите программу, которая измеряет время выполнения кода с помощью time.sleep(2), используя модуль time.
Ожидаемый вывод:
Код выполнялся 2.0001 сек"""

import time

def size_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        res = {end - start}
        print(f"Код выполнялся {res} сек")
        return res
    return wrapper

@size_time
def slow_func_2():
    time.sleep(2)
slow_func_2()


"""6. Установите библиотеку requests и проверьте, работает ли она.
Напишите код, который делает HTTP-запрос и получает данные с сайта:"""

import requests

response = requests.get("https://api.github.com")
print(response.status_code) #получил 200 код - ок

"""7. Установите библиотеку matplotlib и постройте график.
Напишите код:"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

"""8. Создайте requirements.txt с зависимостями вашего проекта.
Удалите один из установленных модулей, например requests
Восстановите зависимости с помощью установки из requirements.txt"""

#(.venv) PS C:\Users\Александр\PycharmProjects\PythonProject> pip freeze > requrements.txt
# (.venv) PS C:\Users\Александр\PycharmProjects\PythonProject> pip uninstall requests
# Found existing installation: requests 2.32.5
# Uninstalling requests-2.32.5:
#   Would remove:
#     c:\users\александр\pycharmprojects\pythonproject\.venv\lib\site-packages\requests-2.32.5.dist-info\*
#     c:\users\александр\pycharmprojects\pythonproject\.venv\lib\site-packages\requests\*
# Proceed (Y/n)? y
#   Successfully uninstalled requests-2.32.5
# (.venv) PS C:\Users\Александр\PycharmProjects\PythonProject> pip install --upgrade pip
# Requirement already satisfied: pip in c:\users\александр\pycharmprojects\pythonproject\.venv\lib\site-packages (25.2)
# (.venv) PS C:\Users\Александр\PycharmProjects\PythonProject>

"""9. Создание простого пакета
Создайте пакет math_operations с модулями:
addition.py → Функция add(a, b) складывает 2 числа
subtraction.py → Функция subtract(a, b) вычитает
Структура проекта:

math_operations/
│── __init__.py
│── addition.py
│── subtraction.py
main.py

И запустите обе функции в main.py"""

