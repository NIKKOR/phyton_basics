# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    list_after_point = list(str(number)[(str(number).index('.') + 1):])
    left_from_0 = 0
    for i in list_after_point:
        list_after_point[list_after_point.index(i)] = int(list_after_point[list_after_point.index(i)])
    if list_after_point[ndigits - 1] < 5:
        list_after_point[ndigits - 1] -= 1
    else:
        if list_after_point[ndigits - 1] == 9:
            for i in range(ndigits - 1, list_after_point.index(9) - 1, -1):
                if i == list_after_point.index(9):
                    left_from_0 = i - 1
                list_after_point[i] = 0
                if i == 0:
                    number = int(number) + 1
            list_after_point[left_from_0] += 1
        else:
            list_after_point[ndigits - 1] +=  1
    list_after_point[ndigits:] = []

    str_after_point = '.'
    for i in list_after_point:
        str_after_point += str(i)
    number = str(int(number)) + str_after_point
    answer = str(float(number)) + ' (' + str(number) + ')'
    return answer


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    first=list(str(ticket_number))[:3]
    first_sum=0
    second=list(str(ticket_number))[3:]
    second_sum=0
    print(first, second)
    if len(first) != 3 or len(second) != 3:
        return 'Your ticket number is invalid (not 6-numbered)'
    for i in range(0, 3):
        first_sum+=int(first[i])
        second_sum+=int(second[i])
    if first_sum == second_sum:
        return 'Your ticket is lucky'
    else:
        return 'Yor ticket is not lucky'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

