"""Example for class definitions."""
from datetime import datetime


# %% a absolute minimum class:


class MinimumClass:
    pass


my_instance = MinimumClass()
print(my_instance.__class__)  # <class '__main__.MinimumClass'>


# %% a simple working example of a class

class RectangleClass:
    width: int
    height: int

    def __init__(self, width: int, heigth: int):
        self.width = width
        self.heigth = heigth

    def set_height(self, height):
        self.heigth = height

    def calculate_area(self):
        return self.width * self.heigth


my_rectangle = RectangleClass(2, 4)
print(my_rectangle.calculate_area())  # 8


# %% another example of a class

class Dummy:
    """Here goes a onliner for the class

    Here goes the extended description
    """

    CONSTANT_VALUE = "3.1415926535"

    def __init__(self, necessary_param, optional_param=None):
        self.necessary_param = necessary_param

    def class_method(self):
        print(self.necessary_param)

    @staticmethod
    def static_method():  # no self if static
        print("static method")


# %% a simple working example of a class
class Vehicle:

    def __init__(self, build_dt):
        self._build_dt = build_dt

    def _close_circuits(self):
        ...

    def _inject_fuel(self):
        ...

    def _ignite_fuel_mixture(self):
        ...

    def start_engine(self):
        self._close_circuits()
        self._inject_fuel()
        self._ignite_fuel_mixture()
        ...

    @property
    def ago_of_car(self):
        return datetime.today() - self._build_dt


veh = Vehicle(datetime(2000, 1, 1))
help(veh)


# %% an extension of the recangle class
class Rectangle:

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def calculate_area(self):
        return self.width * self.heigth

    @staticmethod
    def circumference_from_dim(width, heigth):
        return 2 * width + 2 * heigth

    @classmethod
    def square_from_width(cls, width):
        return cls(width, width)


rectangle_1 = Rectangle(2, 4)
rectangle_2 = Rectangle(4, 8)
rectangle_3 = Rectangle(6, 3)
rectangle_4 = Rectangle(8, 8)

rectangle_1.calculate_area()  # 8
rectangle_2.calculate_area()  # 32
...

# Rectangle.calculate_area()  # wrong! not possible
# has to be called on instance not on class
print(my_rectangle.calculate_area())  # 8

rectangle_1.heigth = 10
rectangle_1.calculate_area()  # 20
rectangle_2.calculate_area()  # 32

square_1 = Rectangle.square_from_width(width=2)
square_1.calculate_area()  # 4


# %% anoter variant
class RectangleSpecial:
    rectangles_mutable = []
    rectangle_immutable = ()

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        rectangle_name = f"{width} by {heigth}"
        self.rectangles_mutable.append(rectangle_name)
        self.rectangle_immutable += (rectangle_name,)


rect_spec_1 = RectangleSpecial(2, 4)
rect_spec_2 = RectangleSpecial(8, 4)
rect_spec_3 = RectangleSpecial(10, 4)

rect_spec_3.rectangles_mutable
rect_spec_3.rectangle_immutable
