import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print(os.getcwd())
for i in range(1, 10):
    dir_name = 'dir_' + str(i)
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.mkdir(dir_path)
#  добавь удаление перед запуском