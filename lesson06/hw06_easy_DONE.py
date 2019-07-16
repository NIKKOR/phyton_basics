# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    def __init__(self,
                 x1, y1,
                 x2, y2,
                 x3, y3):
        """
        определяем длину сторон с помощью формул векторов
        """
        self.ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.bc = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        self.ac = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    def p(self):
        """
        определяем периметр
        """
        return self.ab + self.bc + self.ac

    def s(self):
        """
        определяем площадь с помощью формулы Герона
        """
        return round(math.sqrt(self.p()/2 * (self.p()/2 - self.ab) * (self.p()/2 - self.bc) * (self.p()/2 - self.ac)), 2)

    def h(self, side):
        """
        определяем длину высоты, опущенной на сторону side (второй параметр; примеры: ab, bc, ac)
        """
        return round((2 * self.s()) / side, 2)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trap:
    def __init__(self,
                 x1, y1,
                 x2, y2,
                 x3, y3,
                 x4, y4):
        self.a=[x1, y1]
        self.b=[x2, y2]
        self.c=[x3, y3]
        self.d=[x4, y4]
        """
        считаем длину сторон
        """
        self.ab=math.sqrt((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2)
        self.bc=math.sqrt((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2)
        self.cd=math.sqrt((self.c[0] - self.d[0]) ** 2 + (self.c[1] - self.d[1]) ** 2)
        self.ad=math.sqrt((self.a[0] - self.d[0]) ** 2 + (self.a[1] - self.d[1]) ** 2)

    def p(self):
        return self.ab + self.bc + self.cd + self.ad

    def isosceles(self):
        if self.ab == self.cd or self.bc == self.ad:
            print('Трапеция равнобедренная')
        else:
            print('Трапеция не равнобедренная')

    def parallels(self):
        """
        определяем основания для расчёта площади
        """
        if self.ab == self.cd:
            return [self.bc, self.ad]
        elif self.bc == self.ad:
            return [self.ab, self.cd]
        else:
            print('Трапеция не равнобедренная')

    def h(self):
        """
        определяем высоту
        """
        if self.parallels() == [self.bc, self.ad]:
            if self.b[1] > self.a[1]:
                return self.b[1] - self.a[1]
            else:
                return self.a[1] - self.b[1]
        elif self.parallels() == [self.ab, self.cd]:
            if self.b[1] > self.d[1]:
                return self.b[1] - self.d[1]
            else:
                return self.d[1] - self.b[1]

    def s(self):
        return 0.5 * (self.parallels()[0] + self.parallels()[1]) * self.h()



