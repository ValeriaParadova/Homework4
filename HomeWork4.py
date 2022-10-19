#Вычислить число c заданной точностью d
#Пример:
#- при d = 0.001, π = 3.141.    10^(-1) ≤ d ≤10^(-10)

import math
n = int(input('Введите количество цифр после запятой: '))
print('Число 𝜋: {:.50f}'.format(math.pi))
a = math.pi
b = round(a,n+1)*10**n
c = math.modf(b)
a = c[1] / 10**n
print('Число 𝜋 с заданной точностью:',a)


#Задайте натуральное число N. Напишите программу, 
#которая составит список простых множителей числа N.



def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number

def func_search(num):
    rezult = []

    for i in range(2, num):
        while num % i == 0:
            num /= i
            rezult.append(i)
    return rezult

num = InputNumbers("Введите натуральное число N: ")

print(f"Результат деления: {func_search(num)}")



#Задайте последовательность чисел. Напишите программу, 
#которая выведет список неповторяющихся элементов исходной последовательности.


a = [1, 2, 2, 3, 4, 6, 8, 8, 2, 9, 7, 4, 9]
i = a[0]
c = []
for i in a:
    if i in c:
       continue
    else:
       c.append(i)
print(c)


#Задана натуральная степень k. Сформировать случайным 
#образом список коэффициентов (значения от 0 до 100) 
#многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите коэффициент: '))
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))
if a != 0:
    first = (str(a) + "x^" + str(k) + " + ")
else:
    first = (str())
if b != 0:
    second = (str(b) + "x" + " + ")
else:
    second = (str())
if c != 0:
    third = (str(c) + " = 0")
else:
    third = (str())
print(f'{first}{second}{third}')


#Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов.

with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')