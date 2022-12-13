from point import Point
from math import inf

class Renderer:
    def __init__(self, canvas,  scene):
        self.canvas = canvas
        self.canvas_width = canvas.width
        self.canvas_height = canvas.height

        self.scene_width = 1#canvas.width
        self.scene_height = 1#canvas.height
        self.dist_to_view = 1
        self.max_render_dist = 10000
        self.camera_pos = Point(0,0,0)
        self.scene = scene

        self.background_color = (0,0,0)

    def canvas2viewport(self, x, y):
        return Point(x*self.scene_width/self.canvas_width, y*self.scene_height/self.canvas_height, self.dist_to_view)

    def render(self):
        for x in range(-self.canvas_width // 2, self.canvas_width // 2):
            for y in range(-self.canvas_height // 2, self.canvas_height // 2):
                vp = self.canvas2viewport(x, y)
                color = self.traceRay(vp)
                self.canvas.put_pixel(x + self.canvas_width // 2, self.canvas_height // 2 - y, color)
        self.canvas.show_image()


    def traceRay(self, vp):
        closest_t = self.max_render_dist
        for fig in self.scene:
            ts = fig.intersectRay(self.camera_pos, vp)
            for t in ts:
                if t < closest_t and t > 0:
                    closest_t = t
                    closest_fig = fig

        if closest_t == self.max_render_dist or closest_t < self.dist_to_view:
            return self.background_color
        return closest_fig.color