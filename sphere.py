from figure import Figure
from point import Point
from math import inf, sqrt
import numpy as np

class Sphere(Figure):
    def __init__(self, color, center, radius = 10):
        super().__init__(color)
        self.center = center
        self.radius = radius

    def intersectRay(self, ray_origin, ray_direction):
        b = 2 * np.dot(ray_direction, ray_origin - self.center)
        c = np.linalg.norm(ray_origin - self.center) ** 2 - self.radius ** 2

        discriminant = b*b - 4*c

        if discriminant > 0:
            t1 = (-b + sqrt(discriminant)) / 2
            t2 = (-b - sqrt(discriminant)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)
        return -1
