import os
import item_path
import content_dir
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def current_dir():
    print('{2:.>100}\n{0:>100}\n{1:>100}'.format('Текущая директория: ', os.getcwd(), ''))


def goto_dir():

    dir_name = input('Введите имя папки для перехода: ')
    try:
        os.chdir(item_path.do(dir_name))
        current_dir()
    except Exception:
        'При смене директории возникла ошибка. Попробуйте ещё раз'


def content_all():
    dir_path_2=os.listdir(os.getcwd())
    print('\n{0:.^50}'.format('Содержимое текущей директории:') +
          '\n{0}{1:.>38}'.format('Имя:', 'Путь:'))
    for i in dir_path_2:
        extra_path='({})'.format(item_path.do(i))
        print(i, '{:.>100}'.format(extra_path))


def del_dir():
    dir_name = input('Введите имя папки для удаления: ')
    try:
        os.rmdir(item_path.do(dir_name))
        current_dir()
    except Exception:
        'При удалении папки возникла ошибка. Попробуйте ещё раз'


def mk_new_dir():
    dir_name = input('Введите имя новой папки: ')
    try:
        os.mkdir(item_path.do(dir_name))
        print('Папка {} успешно создана'.format(dir_name))
    except Exception:
        'При создании папки возникла ошибка. Попробуйте ещё раз'


def interface():
    current_dir()
    command = input('Введите команду: \n')
    current_dir()
    if command == 1:
        goto_dir()
    elif command == 2:
        content_all()
    elif command == 3:
        del_dir()
    elif command == 4:
        mk_new_dir()
    elif command == 5:
        return "exit"


print('{0:.^100}\n'
      'Доступные действия:\n'
      '1. Перейти в папку\n'
      '2. Просмотреть содержимое текущей папки\n'
      '3. Удалить папку\n'
      '4. Создать папку\n'
      '5. Выйти\n'
      '{1:.^100}\n'
      .format('Файловый менеджер', ''))

while interface() != 'exit':
    interface()
