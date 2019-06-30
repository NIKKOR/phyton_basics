# -*- coding: utf-8 -*-
import random
import math

def input_infinity_list(list_def: list, keyword: str):
    while True:
        list_def.append(input('Вводите элементы списка. Когда закончите, введите в поле ввода "EXIT"\n'))
        if list_def[-1] == keyword:  # проверка на ключевое слово EXIT
            list_def.pop()  # убираем EXIT из списка
            print('Ваш список: ', list_def)  # выводим данный список
            break  # выходим из бесконечного цикла (приходится так делать, ведь do-while в phyton нет(((
        elif not list_def[-1].isalpha():  # преобразуем строку в число для дальнейших математических операций
            # (введённые числа преобразуются в строку с помощью input)
            if float(list_def[-1]) % 1 == 0:
                list_def[-1] = int(float(list_def[-1]))
            else:
                list_def.pop()
                print('Можно вводить только целые числа')
        else:
            list_def.pop()
            print('Можно вводить только целые числа')

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list_input = []
list_inputSQRT = []

input_infinity_list(list_input, 'EXIT')
# думал, что так получится короче, но оказалось только сложнее:
'''
for i in list_input: 
    if list_input[list_input.index(i)] > 0:
        if math.sqrt(list_input[list_input.index(i)]) % 1 == 0:
            list_inputSQRT.append(int(math.sqrt(list_input[list_input.index(i)])))
            '''
#  пока писал это, подумал, как было бы удобно написать это на C++ с помощью for:
'''
i = 0
while i < len(list_input):  # 
    if list_input[i] > 0 and math.sqrt(list_input[i]) % 1 == 0:  # корни должны извлекаться только из
        # неотрицательных чисел и являться целыми числами
        list_inputSQRT.append(int(math.sqrt(list_input[i])))
    i += 1
'''
#  аналог цикла for из C++:

for i in range(0, (len(list_input))):
    if list_input[i] > 0 and math.sqrt(list_input[i]) % 1 == 0:  # корни должны извлекаться только из
        # неотрицательных чисел и являться целыми числами
        list_inputSQRT.append(int(math.sqrt(list_input[i])))
print("Ваш список с хорошими корнями: ", list_inputSQRT)
