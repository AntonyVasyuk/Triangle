import typing


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, dots: tuple[Point, Point]):
        self.dots = dots
        self.length = self.calc_length(self.dots)

    def calc_length(self, dots: tuple[Point, Point]):
        return ((dots[1].x - dots[0].x) ** 2 + (dots[1].y - dots[0].y) ** 2) ** 0.5


class Vector:
    def __init__(self, cords=(0, 0)):
        self.cords = cords
        
    def transform_segment_to_vector(self, s: Segment):
        self.calc_cords_by_two_points(*segment.dots)

    def calc_cords_by_two_points(self, p1 : Point, p2: Point):
        self.cords = (p2.x - p1.x, p2.y - p1.y)


class Line:
    def __init__(self, coefficients=(0, 0, 0)):
        self.coefficients = coefficients

    def calc_coefficients_by_two_points(self, p1: Point, p2: Point):
        self.coefficients = ((p2.y - p1.y), -(p2.x - p1.x), (p2.x * p1.y - p1.x * p2.y))

    def calc_coefficients_by_normal_and_point(self, n: Vector, p: Point):
        self.coefficients = (n.cords[0], n.cords[1], -(n.cords[0] * p.x + n.cords[1] * p.y))



p1, p2 = Point(-3, 2), Point(1, -2)
segment = Segment((p1, p2))
print(segment.length)