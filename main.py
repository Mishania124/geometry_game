from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rec(self, rectangle):
        return rectangle.lowleft.x < self.x < rectangle.upright.x \
               and rectangle.lowleft.y < self.y < rectangle.upright.y

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2) + ((self.y - point.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)


def check_coord():
    global a1, b1, a2, b2
    if a1 > b1:
        a1, b1 = b1, a1
    if a2 > b2:
        a2, b2 = b2, a2
    if a1 == b1 or a1 == b1 - 1:
        b1 += 2
    if a2 == b2 or a2 == b2 - 1:
        b2 += 2


a1 = randint(0, 10)
a2 = randint(0, 10)
b1 = randint(0, 10)
b2 = randint(0, 10)

check_coord()
print(f'Point x={a1, a2},point y={b1, b2}')
q = int(input('Guess x: '))
w = int(input('Guess y: '))
print(Point(q, w).falls_in_rec(Rectangle(Point(a1, a2), Point(b1, b2))))
e = int(input('Guess rectangle area: '))
print(f'Rectangle area: {Rectangle(Point(a1, a2), Point(b1, b2)).area()}')
print(Rectangle(Point(a1, a2), Point(b1, b2)).area() == e)
