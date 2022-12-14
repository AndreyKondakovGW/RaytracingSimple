import sys
import os
os.path.realpath(__file__)
from UI import UI
from renderer import Renderer
from sphere import Sphere
import numpy as np
from material import Material

if __name__ == '__main__':
    ui = UI(height=300)
    red_material = Material(np.array([1,0,0]), np.array([1,0,0]), reflection=0.5)
    green_material = Material(np.array([0,1,0]), np.array([0,1,0]), reflection=0.5)
    blue_material = Material(np.array([0,0,1]), np.array([0,0,1]))
    scene = [
        Sphere(np.array([-0.2, 0, 2]), red_material, 0.7),
        Sphere(np.array([0.1, -0.3, 1]), green_material, 0.1),
        Sphere(np.array([-0.3, 0, 1]), blue_material, 0.15)]
    renderer = Renderer(ui.canv, scene)
    renderer.render()
    ui.run()


