import numpy as np

class NPPoint:
    def __init__(self, x, y, z=0):
        self.data = np.array([x, y, z, 1])
        self.x, self.y, self.z, _ = self.data

    def __add__(self, other):
        return NPPoint(*self.data + other.data)

    def __sub__(self, other):
        return NPPoint(*self.data - other.data)
    
    def normalize(self):
        return NPPoint(*self.data / np.linalg.norm(self.data))