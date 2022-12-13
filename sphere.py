from figure import Figure
from point import Point
from math import inf, sqrt

class Sphere(Figure):
    def __init__(self, color, center, radius = 10):
        super().__init__(color)
        self.center = center
        self.radius = radius

    def intersectRay(self, camera, direction):
        c = self.center
        r = self.radius
        o = camera
        d = direction
        oc = o - c

        k1 = d.dot(d)
        k2 = 2*d.dot(oc)
        k3 = oc.dot(oc) - r*r

        discriminant = k2*k2 - 4*k1*k3
        if discriminant < 0:
            return [-1]

        t1 = (-k2 + sqrt(discriminant)) / (2*k1)
        t2 = (-k2 - sqrt(discriminant)) / (2*k1)
        return [t1, t2]
