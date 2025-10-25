print("Задание_1:")

name = "Александр"
age = 30
text = ("Меня зовут " + name + ", мне " + str(age) + " лет.")
print(text)
#print(text + 43) # - ошибка can only concatenate str (not "int") to str

print("Задание_2:")

name = "Александр"
age = 30
text1 = "Привет, меня зовут {}, мне {} лет.".format(name, age)
print(text1)

text2 = "Привет, меня зовут {0}, мне {1} лет.".format(name, age)
print(text2)

text3 = "Привет, меня зовут {name}, мне {age} лет.".format(name=name, age=age)
print(text3)

text4 = "Привет, меня зовут {1}, мне {0} лет.".format(age, name)
print(text4)

text5 = "Привет, мне {age} лет, меня зовут {name}.".format(name=name, age=age)
print(text5)

print("Задание_3:")

city = "Куровское"
year = 2025
print(f"Сегодня {year} год, и я живу в {city}.")
print(f"Через 5 лет будет {year + 5} год")

print("Задание_4:")

print(f"Дважды мой возраст: {age * 2}")
print(name.upper())

print("Задание_5:")
valuta = "доллар"
rub = 92.5
print("Курс валют: 1 {0} = {1} рубля.".format(valuta, rub))
x = 7
print(f"Квадрат числа {x} равен {x**2}.")