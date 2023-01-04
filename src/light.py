import numpy as np

def normalize(vector):
   return vector / np.linalg.norm(vector)

class Light:
    def __init__(self, position, ambient = np.array([1, 0, 0]), diffuse = np.array([0.5, 0.5, 0.5]), specular = np.array([0.5, 0.5, 0.5])):
        self.position = position
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular

    def count_illumination(self, point, normal, view_direction, material):
        light_direction = normalize(self.position - point)
        ambient = self.ambient * material.ambient
        diffuse = self.diffuse * material.diffuse * np.dot(normal, light_direction)
        H = normalize(light_direction + view_direction)
        specular = self.specular * material.specular * np.dot(normal, H) ** (material.shininess / 4)
        return np.clip(ambient + diffuse + specular, 0, 1)