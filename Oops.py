from math import pi


class Shape:

    def area(self, length=None, width=None, radius=None):
        print(radius)
        if length != None and width != None and radius != None:
            print(length * width)
        elif length != None and width != None:
            print(length * length)
        else:
            print(pi * radius * radius)


s = Shape()
s.area(radius=10)
