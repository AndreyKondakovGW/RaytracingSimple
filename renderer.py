from point import Point
from light import Light
import numpy as np
from multiprocessing import Pool

import asyncio
def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)
    return wrapped

def normalize(vector):
   return vector / np.linalg.norm(vector)

class RayCaster:
    def __init__(self, scene):
        self.scene = scene
        self.background_color = np.array([0,0,0])

        self.num_refraction = 5

        self.dist_to_screne = 1
        self.max_render_dist = 10000
        self.camera_pos = np.array([0,0,0])
        self.scene = scene

        self.lights = [
         #Light(np.array([0.3,0.1,2]), ambient = np.array([0.5,0.5,0.5])),
         Light(np.array([-0.4, -0.3, 0.49]), ambient = np.array([0.5,0.5,0.5]))]
    
    def count_pixel_color(self, d):
        i,j,x,y = d
        pixel = np.array([x, y, self.dist_to_screne])
        direction = normalize(pixel - self.camera_pos)
        color = self.traceRay(direction)
        #print(color)
        return (i,j,color)

    def traceRay(self, direction):
        color = np.zeros((3))
        reflection = 1
        origin = self.camera_pos
        for k in range(self.num_refraction):
            if k == 0:
                closest_fig, min_dist = self.get_closest_intersection(origin, direction, 1)
            else:
                closest_fig, min_dist = self.get_closest_intersection(origin, direction)
            if closest_fig is None:
                color += reflection * self.background_color
                return color

            intersection = origin + min_dist * direction
            illumination = np.zeros((3))
            for light in self.lights:
                if self.check_shadowed(intersection, closest_fig, light):
                    illumination += closest_fig.material.ambient
                    continue
                dist_to_light = np.linalg.norm(light.position - intersection)
                #модель Блинна-Фонга
                illumination += light.count_illumination(intersection, closest_fig.getNormal(intersection), -1* direction, closest_fig.material) / dist_to_light ** 2
                
            # отражение
            color += reflection * illumination
            reflection *= closest_fig.material.reflection
            if reflection < 0.0001:
                break

            # начальная точка и направление нового луча
            normal_to_surface = closest_fig.getNormal(intersection)
            shifted_point = intersection + 1e-5 * normal_to_surface
            origin = shifted_point
            direction = self.reflected(direction, normal_to_surface)
        return np.clip(color, 0, 1)

    def get_closest_intersection(self, start_pos, direction, min_dist_border = 0):
        min_dist = self.max_render_dist
        for fig in self.scene:
            f ,dist = fig.intersectRay(start_pos, direction)
            if dist < min_dist and dist > min_dist_border:
                min_dist = dist
                closest_fig = f
        if min_dist == self.max_render_dist or min_dist < 0:
            return None, self.max_render_dist
        return closest_fig, min_dist

    def reflected(self, vector, axis):
        return vector - 2 * np.dot(vector, axis) * axis

    def check_shadowed(self, int_point, fig, light):
        normal_to_surface = fig.getNormal(int_point)
        shifted_point = int_point + 1e-5 * normal_to_surface
        dir_to_light = normalize(light.position - shifted_point)
        _, min_distance = self.get_closest_intersection(shifted_point, dir_to_light)
        dist_to_light = np.linalg.norm(light.position - int_point)
        is_shadowed = min_distance < dist_to_light
        return is_shadowed

class Renderer:
    def __init__(self, canvas,  scene):
        self.canvas = canvas
        self.canvas_width = canvas.width
        self.canvas_height = canvas.height

        self.screne_height = 1
        self.screne_width = self.screne_height * self.canvas_width / self.canvas_height

        self.ray_caster = RayCaster(scene)

    def render(self):
        data = []
        for i, y in enumerate(np.linspace(-self.screne_height / 2, self.screne_height / 2, self.canvas_height)):
            for j, x in enumerate(np.linspace(-self.screne_width / 2, self.screne_width / 2, self.canvas_width)):
                data.append((i,j,x,y))
        agents = 10
        chunksize = 10
        with Pool(processes=agents) as pool:
            result = pool.map(self.ray_caster.count_pixel_color, data, chunksize)
        for i,j,color in result:
            self.canvas.put_pixel(j, self.canvas_height - i, color * 255)
        self.canvas.show_image()