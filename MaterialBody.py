from MaterialPoint import Point
import numpy as np
class Body:
    def __init__(self, x: float = 10, y: float = -10, length: float = 1, points_number: int = 200):
        self.points_number = points_number
        self.length = length
        self.x = x
        self.y = y
        self.body_point = []

    def add_points_to_body(self) -> list[Point]:
        points = [Point(self.x, self.y), Point(self.x - self.length, self.y)]
        for i in range(self.points_number):
            x = np.random.uniform(0, -self.length) + self.x
            y= self.y
            points.append(Point(x, y))
        return points
