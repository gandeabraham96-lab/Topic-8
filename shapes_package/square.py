class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# A square is a special case of a rectangle because its
# length and width are always equal. However, the Square
# class is implemented separately to keep it simple and
# focused on its single side attribute.