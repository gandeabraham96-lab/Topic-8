class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# A square is a special case of a rectangle because its
# length and width are always equal. However, it is implemented
# separately here to keep the Square class simple and focused
# on its single side attribute.

from shapes_package.square import Square

square = Square(5)

print("Side:", square.side)
print("Area:", square.area())