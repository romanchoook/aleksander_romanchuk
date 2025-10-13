#1. Вывод чисел от 1 до N
n = int(input("Введите число N: "))
i = 1
while i <= n:
    print(i)
    i += 1

#2. Сумма четных чисел до N
n = int(input("Введите число N: "))
sum = 0
i = 1
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)

#3. Подсчет количества цифр в числе
x = input("Введите натуральное число: ")
i = 0
while i < len(x):
    i += 1
print("количество цифр в указанном числе: ", i)

#4. Определение максимальной цифры в числе
x = int(input("Введите натуральное число: "))
i = 0
maks = 0
spisok = list(str(x))
while i < len(spisok):
    current_value = int(spisok[i])
    if current_value > maks:
        maks = current_value
    i += 1
print(maks)

#5. Запрос пароля
correct_pass = "qwerty123"
password = input("Введите пароль: ")
while password != correct_pass:
    print("Пароль неверный, попробуйте снова")
    password = input("Введите пароль: ")
print("Доступ разрешен")

#1. Поиск первого четного числа
numbers = [23, 43, 75, 33, 66, 51, 80]
found = False
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print("Первое четное число равно ", numbers[i])
        found = True
        break
    i += 1
if found == False:
    print("Четное число не найдено")

#2. Пропуск отрицательных чисел
num = 1
res_sum = 0
while num != 0:
   num = int(input("Введите целое число или 0 для выхода: "))
   if num > 0:
       res_sum = res_sum + num
   else:
       continue
print(res_sum)

#3. Вывод нечетных чисел из диапазона
a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
x = a
result = []
if a <= b:
    while x <= b:
        if x % 2 == 0:
            x += 1
            continue
        result.append(x)
        x += 1
else:
    while x >= b:
        if x % 2 == 0:
            x -= 1
            continue
        result.append(x)
        x -= 1
print(result)

#4. Проверка на простое число
N = int(input("Введите число N: "))
delitel = 2
count = 1
result = ""
while delitel <= N:
    if N % delitel == 0:
        count += 1
        if count > 2:
            break
    delitel += 1
if count == 2:
    result = "Число простое"
else:
    result = "Число не является простым"
print(result)


#5. Поиск максимального числа
num = 1
res_sum = []
while num != 0:
   num = input("Введите целое число или 0 для выхода: ")
   if num == "":
       result = ("Введено пустое значение")
       break
   num = int(num)
   if num != 0:
       res_sum.append(num)
       result = max(res_sum)
   else:
       continue
print(result)

#1. Вывести все символы строки в обратном порядке
result = []
str1 = input("Введите строку: ")
for i in range(len(str1)-1, -1, -1):
    result.append(str1[i])
print(result)

#2.Замена четных элементов списка на 0
spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(spisok)):
    if spisok[i] % 2 == 0:
        spisok[i] = 0
print(spisok)

#3. Генерация списка степеней двойки
N = int(input("Введите число N: "))
result = []
for i in range(0, N +1, 1):
    result.append(2 ** i)
print(result)

#4. Вывод всех чисел от A до B с шагом K
A = int(input("Введите А: "))
B = int(input("Введите B: "))
K = int(input("Введите K: "))
res = []
for i in range(A, B + 1, K):
    res.append(i)
print(res)