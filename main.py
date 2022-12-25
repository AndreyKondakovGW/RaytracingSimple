import sys
import os
os.path.realpath(__file__)
from UI import UI
from renderer import Renderer
from sphere import Sphere
from surface import Surface
import numpy as np
from material import Material
from box import Box
from octahedron import Octahedron
from poly import Polygon


if __name__ == '__main__':
    ui = UI(height=400)
    red_material = Material(np.array([0.1,0,0]), np.array([0.8,0,0]), reflection=0.5)
    green_material = Material(np.array([0,0.1,0]), np.array([0,0.8,0]), reflection = 0.9)
    blue_material = Material(np.array([0,0,0.1]), np.array([0,0,0.8]), reflection = 0.01)
    violet_material = Material(np.array([0.1,0,0.1]), np.array([0,0,0.8]), reflection = 0.4)
    glass_material = Material(np.array([0,0,0]), np.array([0,0,0]), reflection=1)

    right_wall = Surface(blue_material, np.array([1, 0, 0]), np.array([-1, 0, 0]))
    left_wall = Surface(blue_material, np.array([-1, 0, 0]), np.array([1, 0, 0]))
    top_wall = Surface(blue_material, np.array([0, 1, 0]), np.array([0, -1, 0]))
    bottom_wall = Surface(blue_material, np.array([0, -1, 0]), np.array([0, 1, 0]))
    back_wall = Surface(blue_material, np.array([0, 0, 3]), np.array([0, 0, -1]))
    front_wall = Surface(blue_material, np.array([0, 0, 0.5]), np.array([0, 0, 1]))
    scene = [
        Sphere(np.array([0.3, -0.3, 3]), red_material, 0.5),
        Sphere(np.array([-0.4, -0.4, 1.3]), violet_material, 0.1),
        Box(np.array([-0.3, -0.3, 1.5]), glass_material, 0.4),
        # Octahedron(glass_material,np.array([0, 0, 2]), np.array([1, 1, 1])),
        right_wall,
        left_wall,
        top_wall,
        bottom_wall,
        back_wall,
        front_wall]

    renderer = Renderer(ui.canv, scene)
    renderer.render()
    ui.run()


