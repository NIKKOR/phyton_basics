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
