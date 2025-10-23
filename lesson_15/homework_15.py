"""1. Создайте текстовый файл data.txt со следующим содержимым:

Python – это мощный язык программирования.
Работа с файлами важна для автоматизации.
Чтение файлов в Python удобно и просто.

Напишите программу, которая полностью прочитает файл и выведет его содержимое."""
data = "data.txt"
f = open(data, encoding="utf-8")
print(f.read())
f.close()

print(8*"=")
"""2. Напишите программу, которая считает и выведет только первую строку из файла data.txt.
Ожидаемый вывод:
Python – это мощный язык программирования."""
f = open(data, encoding="utf-8")
first_line = f.readline()
print(first_line.strip())
f.close()

print(8*"=")
"""3. Откройте файл data.txt и прочитайте первые 10 символов.
Ожидаемый вывод:
Python – э"""

f = open(data, encoding="utf-8")
ten_symbols = f.read(10)
print(ten_symbols)
f.close()

print(8*"=")

"""4. Прочитайте все строки файла и сохраните их в список. Затем выведите этот список.
Ожидаемый вывод:
['Python – это мощный язык программирования.\n', 'Работа с файлами важна для автоматизации.\n', 'Чтение файлов в Python удобно и просто.\n']"""

f = open(data, encoding="utf-8")
spisok_f = list(f)
print(spisok_f)
f.close()

print(8*"=")
"""5. Напишите программу, которая считает строки файла data.txt в цикле и выводит их по одной, убирая символ \n в конце.
Ожидаемый вывод:
Строка: Python – это мощный язык программирования.
Строка: Работа с файлами важна для автоматизации.
Строка: Чтение файлов в Python удобно и просто."""
f = open(data, encoding="utf-8")
while True:
    line = f.readline()
    if not line:
        break
    print("Строка:", line.strip())
f.close()

print(8*"=")
"""6. Откройте файл data.txt, прочитайте 5 символов, затем переместите указатель в начало файла
и снова прочитайте 5 символов и выведите их.
Ожидаемый вывод:
Python
Python"""# - это же шесть символов?
f = open(data, encoding="utf-8")
five_symbols = f.read(5)
print(five_symbols)
f.seek(0)
print(five_symbols)
f.close()

print(8*"=")

"""7. Напишите программу, которая откроет файл data.txt, определит его размер (в байтах) и выведет его.
Ожидаемый вывод:
Размер файла: 128 байт  # (значение может отличаться)"""
f = open(data, encoding="utf-8")
f.read()
print(f"Размер файла: {f.tell()} байт")
f.close()

print(8*"=")
"""8. Используйте with open(), чтобы прочитать и вывести содержимое файла data.txt."""

with open(data, encoding="utf-8") as f:
    print(f.read())

print(8*"=")

"""9. Напишите программу, которая пытается открыть файл data.txt, прочитать его содержимое и вывести его.
Если файл не найден, программа должна вывести "Ошибка: Файл не найден"."""

try:
    f = open(data, encoding="utf-8")
    try:
        print(f.read())
    finally:
        f.close()
except FileNotFoundError:
    print("Ошибка: Файл не найден")

print(8*"=")

"""10. Модифицируйте программу из Задания 1, добавив гарантированное закрытие файла в блоке finally."""

try:
    f = open(data, encoding="utf-8")
    try:
        print(f.read())
    finally:
        f.close()
finally:
    f.close()


print(8*"=")

"""11. Используйте with open(), чтобы безопасно открыть файл data.txt и прочитать его построчно.
Если файл не найден, выведите "Ошибка: Файл не найден"."""

try:
    with open(data, encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("Ошибка: Файл не найден")

print(8*"=")

"""12. Создайте файл numbers.txt, который содержит по одному числу в каждой строке.
Напишите программу, которая читает файл, суммирует все числа и выводит их сумму.
Если файл не найден, программа должна вывести "Ошибка: Файл не найден".
"""
x = 0
file = "numbers.txt"
try:
    with open(file, encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            x += int(line)
    print(x)
except FileNotFoundError:
    print("Ошибка: Файл не найден")

print(8*"=")
"""13. Создайте файл log.txt.
Программа должна добавлять в него текущую дату и время при каждом запуске.
Используйте модуль datetime и режим "a".

Получение даты и времени для логирования:
import datetime
print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

Пример содержимого файла после нескольких запусков:

2024-02-16 14:30:01 Запуск программы
2024-02-16 14:35:15 Запуск программы
2024-02-16 14:40:22 Запуск программы"""
a = ""
import datetime
file = "log.txt"
with open(file, "a", encoding="utf-8") as f:
    a = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    text = (f"{a} Запуск программы\n")
    f.write(text)