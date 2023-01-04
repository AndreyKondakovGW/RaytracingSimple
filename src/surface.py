from figure import Figure
from math import inf, sqrt
import numpy as np

def normalize(vector):
   return vector / np.linalg.norm(vector)

class Surface(Figure):
    def __init__(self, material, position, normal):
        super().__init__(material)
        self.position = position
        self.normal = normalize(normal)

    def intersectRay(self, ray_origin, ray_direction):
        rdn = np.dot(ray_direction, self.normal)
        if abs(rdn) < 1e-5:
            return None, -1
        return self, np.dot(self.position - ray_origin, self.normal) / rdn


    def getNormal(self, point):
        return self.normal