import numpy as np

class Material:
    def __init__(self, ambient, diffuse, specular = np.array([1, 1, 1]), shininess = 100, reflection = 0, transparency = 0):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
        self.reflection = reflection