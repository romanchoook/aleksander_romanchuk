"""1. Напишите декоратор uppercase_decorator, который делает результат выполнения функции прописными буквами.
Пример вызова:
@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())  # "HELLO, WORLD!"""

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())

"""2. Создайте декоратор repeat(n), который выполняет функцию n раз.
Пример вызова:
@repeat(3)
def hello():
    print("Hello!")
hello()
Вывод:
Hello!
Hello!
Hello!"""

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for x in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def hello():
    print("Hello!")
hello()


"""3. Создайте декоратор cache, который кэширует результаты выполнения функции.
Если функция вызывается с теми же аргументами – возвращать сохраненный результат вместо нового вычисления.
Пример вызова:
@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (результат взят из кэша)"""

def cache(func):
    x = {}
    def wrapper(*args):
        if args in x:
            return x[args]
        result = func(*args)
        x[args] = result
        return result
    return wrapper

@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))
print(slow_add(2, 3))



"""4. Создайте декоратор с таймером timer(repeat), который выполняет функцию repeat раз и выводит среднее время выполнения.
Пример вызова:
@timer(3)
def slow_function():
    time.sleep(1)
slow_function()  # Среднее время выполнения: 1.0002 сек"""

import time
def timer(repeat):
    def decor(x):
        def wrapper(*args, **kwargs):
            total_time = 0
            for i in range(repeat):
                start = time.time()
                result = x(*args, **kwargs)
                end = time.time()
                total_time += (end - start)
            average_time = total_time / repeat
            print(f"Среднее время выполнения {average_time} секунд")
            return result
        return wrapper
    return decor


@timer(3)
def slow_function():
    time.sleep(1)
slow_function()