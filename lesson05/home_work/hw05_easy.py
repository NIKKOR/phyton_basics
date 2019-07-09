import os
import task1


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def mkdir_1_9():
    for i in range(1, 10):
        dir_name='dir_' + str(i)
        dir_path=os.path.join(os.getcwd(), dir_name)
        os.mkdir(dir_path)


def rmdir_1_9():
    for i in range(1, 10):
        dir_name='dir_' + str(i)
        dir_path=os.path.join(os.getcwd(), dir_name)
        os.rmdir(dir_path)


mkdir_1_9()
rmdir_1_9()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def item_path(item):
    return os.path.join(os.getcwd(), item)


try:
    task1.mkdir_x_to_y(1, 9)

    dir_path_2=os.listdir(os.getcwd())
    print('\n{0:.^50}'.format('Папки текущей директории:') +
          '\n{0}{1:.>38}'.format('Имя папки:', 'Путь к папке:'))
    for i in dir_path_2:
        extra_path='({})'.format(item_path(i))
        if os.path.isdir(item_path(i)):
            print(i, '{:.>100}'.format(extra_path))
finally:
    task1.rmdir_x_to_y(1, 9)
