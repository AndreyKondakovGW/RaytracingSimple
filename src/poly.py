from figure import Figure
import numpy as np

class Polygon(Figure):
    def __init__(self, material, v0, v1, v2):
        super().__init__(material)
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

        self.normal = np.cross(self.v1 - self.v0, self.v2 - self.v0)

    def intersectRay(self, ray_origin, ray_direction):
        e1 = self.v1 - self.v0
        e2 = self.v2 - self.v0

        pvec = np.cross(ray_direction, e2)
        det = np.dot(e1, pvec)

        if det < 1e-8 and det > -1e-8:
            return None,-1

        inv_det = 1 / det
        tvec = ray_origin - self.v0
        u = np.dot(tvec, pvec) * inv_det

        if u < 0 or u > 1:
            return None, -1

        qvec = np.cross(tvec, e1)
        v = np.dot(ray_direction, qvec) * inv_det
        if v < 0 or u + v > 1:
            return None, -1

        return self, np.dot(e2, qvec) * inv_det

    def getNormal(self, point):
        return self.normal

    def isInside(self, point):
        a = np.dot(self.v1 - self.v0, point - self.v1)
        b = np.dot(self.v2 - self.v1, point - self.v2)
        c = np.dot(self.v0 - self.v2, point - self.v0)

        if a >= 0 and b >= 0 and c >= 0:
            return True
        
        if a <= 0 and b <= 0 and c <= 0:
            return True
        return False