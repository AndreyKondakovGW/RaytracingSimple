from figure import Figure
from poly import Polygon
import numpy as np

class Octahedron(Figure):
    def __init__(self, material, center, sizes = np.array([1, 1, 1])):
        super().__init__(material)
        self.center = center
        self.size = sizes
        self.polygons = [
            Polygon(material, center + np.array([0, sizes[1] / 2, 0]),
             center + np.array([0, 0, -sizes[2] / 2]),
             center + np.array([-sizes[0] / 2, 0, 0])),
            Polygon(material, center + np.array([0, -sizes[1] / 2, 0]),
             center + np.array([-sizes[0] / 2, 0, 0]),
             center + np.array([0, 0, -sizes[2] / 2])),

            Polygon(material, center + np.array([0, sizes[1] / 2, 0]),
             center + np.array([sizes[0] / 2, 0, 0]),
             center + np.array([0, 0, -sizes[2] / 2])),
            Polygon(material, center + np.array([0, -sizes[1] / 2, 0]),
             center + np.array([0, 0, -sizes[2] / 2]),
             center + np.array([sizes[0] / 2, 0, 0])),

            Polygon(material, center + np.array([0, sizes[1] / 2, 0]),
             center + np.array([0, 0, sizes[2] / 2]),
             center + np.array([-sizes[0] / 2, 0, 0]),
             ),
            Polygon(material, center + np.array([0, -sizes[1] / 2, 0]),
             center + np.array([-sizes[0] / 2, 0, 0]),
             center + np.array([0, 0, sizes[2] / 2])),

            Polygon(material, center + np.array([0, sizes[1] / 2, 0]),
             center + np.array([sizes[2] / 2, 0, 0]),
             center + np.array([0, 0, sizes[0] / 2]),
             ),
            Polygon(material, center + np.array([0, -sizes[1] / 2, 0]),
             center + np.array([0, 0, sizes[0] / 2]),
             center + np.array([sizes[2] / 2, 0, 0])),
        ]

    def intersectRay(self, ray_origin, ray_direction):
        t_min = -1
        closest_polygon = None
        for polygon in self.polygons:
            _, t = polygon.intersectRay(ray_origin, ray_direction)
            if t != -1:
                if t_min == -1:
                    t_min = t
                    closest_polygon = polygon
                elif t < t_min:
                    t_min = t
                    closest_polygon = polygon
                    return closest_polygon, t_min
        return closest_polygon, t

    def getNormal(self, point):
        print('error')
        pass
