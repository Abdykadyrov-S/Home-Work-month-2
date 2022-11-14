
class Figure:
    unit = "см"


    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass



class Circle(Figure):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__radius = radius

    def calculate_area(self):
        s = 3.14 * self.__radius
        return s

    def info(self):
        print(f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area()}{self.unit}")

    @property
    def radius(self):
        return self.__radius




class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        s = self.__side_a * self.__side_b / 2
        return s

    def info(self):
        print(f"side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, area: {self.calculate_area()}{self.unit}")


    @property
    def side_a(self):
        return self.__side_a




    @property
    def side_b(self):
        return self.__side_b



circle1 = Circle(radius=5)
circle2 = Circle(radius=7)
triangle1 = RightTriangle(side_a=4, side_b=7)
triangle2 = RightTriangle(side_a=8, side_b=5)
triangle3 = RightTriangle(side_a=15, side_b=6)

figure = [circle2, circle1, triangle1, triangle3, triangle2]

for figure in figure:
    figure.calculate_area()
    figure.info()