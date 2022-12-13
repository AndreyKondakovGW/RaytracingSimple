import sys
import os
os.path.realpath(__file__)
from UI import UI
from renderer import Renderer
from sphere import Sphere
from point import Point

if __name__ == '__main__':
    ui = UI(width=300, height=300)
    scene = [
        Sphere((255,0,0), Point(0,0,3), 1),
        Sphere((0,255,0), Point(2,0,4), 1),
        Sphere((0,0,255), Point(-2,2,5), 1)]
    renderer = Renderer(ui.canv, scene)
    renderer.render()
    ui.run()


