# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# n = input('Введите число: ')
                        
# if float(n) < 0:                            
#     x = float(n) * (-1)
# sum = 0

# for i in str(n):
#     if i != '.':
#         sum += int(i)
# print(sum)


# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите число: "))
# a = 1
# print("[", end = " ")
# for i in range(n):
#     i+= 1
#     a = a * i
#     print(a, end = " ")
# print("]")



# Задача 3. Задайте список из n чисел последовательности $(1+\frac 1/n)^n$ и выведите на экран их сумму.

# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Введите число: "))
# a = {round((1+1/i)**i, 2) for i in range(1, n + 1 )}
# print(f'Последовательность: {a}\nСумма: {round(sum(a))}')


# Задача 4. Реализуйте алгоритм перемешивания списка.


# from random import randint
# import random
# list = []
# for i in range(10):
#     list.append(randint(0, 11))
# print(list)

# j = 0
# for i in range(len(list)-1, 0, -1):

#     j = random.randint(0, i + 1)
#     list[i], list[j] = list[j], list[i]
# print(list)

