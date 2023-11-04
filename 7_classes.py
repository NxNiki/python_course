
# use pascal naming convention for class definition
class Point:
    # class attributes (shared by all the instances)
    default_color = "red"

    # constructor: called automatically by python interpreter
    def __init__(self, x=0, y=0):
        # instance attributes:
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point {self.x}, {self.y}")

    # class method decorator:
    @classmethod
    def zero(cls):
        return cls(0, 0)

    # magic methods:
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)



    # we don't need to define __lt__ as python automatically figure it out.i


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))

point = Point(1, 2)
print(point.x)
point.draw()

# class vs instance attributes:
# as objects in python are dynamic, we can add attributes after it is created:
point.z = 10
point = Point(1, 2)
Point.default_color = "yellow"
print(point.default_color)
print(Point.default_color)

# class vs instance methods:
# factor objects
point = Point.zero()

# magic methods:
print(str(point))

# comparing objects:
point = Point(1, 2)
other = Point(1, 2)
print(point == other)
print(point < other)
print(point > other)

# arithmetic operations:
print(point + other)

