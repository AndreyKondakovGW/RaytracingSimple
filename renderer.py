from point import Point
from math import inf
import numpy as np
def normalize(vector):
   return vector / np.linalg.norm(vector)
class Renderer:
    def __init__(self, canvas,  scene):
        self.canvas = canvas
        self.canvas_width = canvas.width
        self.canvas_height = canvas.height

        self.screne_width = 1#canvas.width
        self.screne_height = 1#canvas.height
        self.dist_to_screne = 1
        self.max_render_dist = 10000
        self.camera_pos = np.array([0,0,0])
        self.scene = scene

        self.background_color = (0,0,0)

    def canvas2viewport(self, x, y):
        return Point(x*self.screne_width/self.canvas_width, y*self.screne_height/self.canvas_height, self.dist_to_screne)

    def render(self):
        for i, y in enumerate(np.linspace(-self.screne_height / 2, self.screne_height / 2, self.canvas_height)):
            for j, x in enumerate(np.linspace(-self.screne_width / 2, self.screne_width / 2, self.canvas_width)):
                pixel = np.array([x, y, self.dist_to_screne])
                direction = normalize(pixel - self.camera_pos)
                color = self.traceRay(direction)

                self.canvas.put_pixel(j, self.canvas_height - i, color)
        self.canvas.show_image()


    def traceRay(self, direction):
        closest_t = self.max_render_dist
        for fig in self.scene:
            ts = fig.intersectRay(self.camera_pos, direction)
            if ts < closest_t and ts > 0:
                closest_t = ts
                closest_fig = fig

        if closest_t == self.max_render_dist or closest_t < self.dist_to_screne:
            return self.background_color
        return closest_fig.color