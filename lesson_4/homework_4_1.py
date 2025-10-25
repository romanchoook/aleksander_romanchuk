print("Задание_1: ")

s = "Python для автоматизации"
print(s.upper())
print(s.lower())

print("Задание_2: ")

msg = "абракадабра"
print(msg.count("ра"))
print(msg.count("а", 2))

print("Задание_3: ")

print(msg.find("ка"))
print(msg.rfind("а"))
print(msg.find("xyz")) # - вернется -1, так как в этой строке отсутствует подстрока xyz

print("Задание_4: ")
text = "Я изучаю Java"
print(text.replace("Java", "Python"))
print(text.replace(" ", ""))

print("Задание_5: ")
text = "Python"
stroka_5 = "12345"
print(text.isalpha())
print(stroka_5.isdigit())
stroka_5 = "123abc"
print(stroka_5.isdigit())

print("Задание_6: ")

code = "42"
print(code.rjust(5, "0"))
print(code.ljust(10, "*"))

print("Задание_7: ")

stroka_7 = "яблоко, груша, банан"
yabloko, grusha, banana = stroka_7.split(", ")
print(yabloko)
print(grusha)
print(banana)
stroka_7 = "Python;Java;C++"
python, java, c = stroka_7.split(";")
print(python)
print(java)
print(c)

print("Задание_8: ")

text_8 = ["Привет", "мир", "!"]
print(" ".join(text_8))
text_8_1 = ["apple", "banana", "cherry"]
print(", ".join(text_8_1))

print("Задание_9: ")

text_9 = " Python"
text_9_1 = "Python "
text_9_2 = " Python "
print(text_9.lstrip())
print(text_9_1.rstrip())
print(text_9_2.strip())

print("Задание_10: ")
text = "программирование"
text = text.capitalize()
print(text)
print(text.count("р"))
print(text.index("и"))
res = text[::-1]
print(res)