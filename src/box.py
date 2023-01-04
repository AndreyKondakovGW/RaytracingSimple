
from figure import Figure
from math import inf, sqrt
import numpy as np

def normalize(vector):
   return vector / np.linalg.norm(vector)
class Box(Figure):
    def __init__(self, center, material, size = 1):
        super().__init__(material)
        self.center = center
        self.size = size


    def intersectRay(self, ray_origin, ray_direction):
        tmin = -inf
        tmax = inf

        for i in range(3):
            if abs(ray_direction[i]) < 1e-5:
                if ray_origin[i] < self.center[i] - self.size / 2 or ray_origin[i] > self.center[i] + self.size / 2:
                    return None, -1
            else:
                t1 = (self.center[i] - self.size / 2 - ray_origin[i]) / ray_direction[i]
                t2 = (self.center[i] + self.size / 2 - ray_origin[i]) / ray_direction[i]

                if t1 > t2:
                    t1, t2 = t2, t1

                if t1 > tmin:
                    tmin = t1
                if t2 < tmax:
                    tmax = t2

                if tmin > tmax:
                    return None, -1

        return self, tmin

    def getNormal(self, point):
        normal = np.array([0, 0, 0])
        for i in range(3):
            if abs(point[i] - self.center[i] - self.size / 2) < 1e-5:
                normal[i] = 1
            elif abs(point[i] - self.center[i] + self.size / 2) < 1e-5:
                normal[i] = -1
        normal = normalize(normal)
        return normal