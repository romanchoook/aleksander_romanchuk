"""1. Оставь только строки и списки из списка:
items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
Ожидаемый результат:
['hello', [1, 2], 'world']"""
from lesson_11.homework_11 import greet

items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
res = []
for x in items:
    if isinstance(x,(str, list)):
        res.append(x)
print(res)

print(8*"=")
"""2. Создай функцию describe_type(x), которая:
печатает "Это строка", если x — строка
"Это число", если x — int или float
"Это булевое значение", если x — bool
"Неизвестный тип" — в остальных случаях
Пример вызова:
describe_type(5.5)       # Это число
describe_type(True)      # Это булево значение
describe_type("Привет")  # Это строка
describe_type([1, 2, 3]) # Неизвестный тип"""

def describe_type(x):
    if isinstance(x, str):
        print('Это строка')
    elif isinstance(x, bool):
        print("Это булевое значение")
    elif isinstance(x, (int, float)):
        print("Это число")
    else:
        print("Неизвестный тип")


describe_type(5.5)
describe_type(True)
describe_type("Привет")
describe_type([1, 2, 3])

print(8*"=")
"""3. Создай функцию filter_list(f, data: list[int]) -> list[int],
которая возвращает только те элементы из data, которые проходят проверку функцией f.
Проверь на функции lambda x: x > 3 и списке [1, 3, 5, 7]."""

def filter_list(f, data: list[int]) -> list[int]:
    result = []
    for i in data:
        if f(i):
            result.append(i)
    return result
print(filter_list(lambda x: x > 3, [1, 3, 5, 7]))
print(8*"=")
"""4. Добавь аннотацию типов в следующую функцию и укажи, что она возвращает None:
def print_info(name, age, tags):
    print(name, age, tags)"""

def print_info(name: str, age: int, tags: str) -> None:
    print(name, age, tags)
print_info("Александр", 30, "fds")

print(8*"=")
"""5. Создай функцию def analyze(data),
которая выводит количество элементов и среднее значение, если список не пустой."""

def analyze(data: list):
    if not data:
        print("Список пустой")
        return
    not_numbers = [item for item in data if not isinstance(item, (int, float))]
    if not_numbers:
        print(f"Ошибка: следующие элементы не являются числами: {not_numbers}")
        return
    count = len(data)
    average = sum(data)/count
    print(f"Количество элементов: {count}")
    print(f'Среднее значение: {average}')

analyze([2,3,4,65,76])
analyze(["fdsf"])

print(8*"=")
"""6. Список логических значений:
flags = [True, True, True, False]
Проверь:
Все ли значения истинные
Есть ли среди них хотя бы одно истинное
Ожидаемый результат:
False
True"""

flags = [True, True, True, False]
print(all(flags))
print(any(flags))

print(8*"=")
"""7. Поле в игре "Крестики-нолики" представлено так:
field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']
Проверь, победил ли 'x' по первой строке.
Ожидаемый результат:
True"""

field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']
first_row = all(cell == 'x' for cell in field[:3])
if first_row:
    print(True)
else:
    print(False)

print(8*"=")
"""8. На поле для "Сапёра" находится мина, если в ячейке символ *. Есть ли мина?
P = ['0', '0', '0', '*', '0']
Ожидаемый результат:
True"""

P = ['0', '0', '0', '*', '0']
mina = any(cell == "*" for cell in P)
print(mina)

print(8*"=")

"""9. Выбери случайное значение из списка:
colors = ["red", "green", "blue", "yellow", "purple"]
Ожидаемый результат:
Выбран цвет: blue"""

import random

colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Выбран цвет: {random.choice(colors)}")

print(8*"=")
"""10. Сгенерируй 10 случайных чисел от 0 до 100 и выведи их. Сделай так, чтобы результат был одинаковый при каждом запуске."""

random.seed(123)
x = 0
count = 0
while count < 10:
    x = int(random.uniform(1, 100))
    count += 1
    print(x)

print(8*"=")
"""11. Напиши функцию greet(), которая принимает строку name и возвращает строку Привет, <name>!.
Добавь аннотацию типов.
Ожидаемый вывод:
Привет, Анна!"""
def greet(name: str):
    print(f"Привет, {name}!")

greet("Александр")

print(8*"=")
"""12. Создай функцию multiply(a, b), которая принимает два числа int или float и возвращает их произведение.
Добавь аннотацию типов.
Ожидаемый вывод:
20"""
def multiply(a: int | float, b: int | float) -> int | float:
    print(a*b)
multiply(5,6)

print(8*"=")
"""13. Проверь типы аргументов функции через __annotations__.
Создай функцию area(length: float, width: float) -> float и распечатай её аннотации.
Ожидаемый вывод:
{'length': <class 'float'>, 'width': <class 'float'>, 'return': <class 'float'>}"""

def area(length: float, width: float) -> float:
    pass

print(area.__annotations__)
