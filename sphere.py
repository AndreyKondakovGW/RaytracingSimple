from figure import Figure
from math import inf, sqrt
import numpy as np

def normalize(vector):
   return vector / np.linalg.norm(vector)
   
class Sphere(Figure):
    def __init__(self, center, material, radius = 10):
        super().__init__(material)
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
                return self, min(t1, t2)
        return None, -1
    
    def getNormal(self, point):
        return normalize(point - self.center)
