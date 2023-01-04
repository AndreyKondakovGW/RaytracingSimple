from tkinter import Canvas, PhotoImage
import numpy as np
from PIL import Image, ImageTk

class MyCanvas(Canvas):
    def __init__(self, tk, width, height, bg="white"):
        super().__init__(tk, width=width, height=height, bg=bg)
        self.width = width
        self.height = height
        self.af_point = None
        self.init_pixels()
        self.show_image()

    def init_pixels(self):
        self.pixels = np.ones((self.height,self.width, 3))*255

    def show_image(self, state="normal"):
        self.image = ImageTk.PhotoImage(image=Image.fromarray(self.pixels.astype(np.uint8)))
        super().create_image((self.width / 2, self.height / 2), image=self.image, state=state)
    
    def clear(self):
        self.init_pixels()
        self.delete('all')

    def put_pixel(self, x, y, color=(0,0,0)):
        if x < 0 or x >= self.pixels.shape[1] or y < 0 or y >= self.pixels.shape[0]:
            return
        self.pixels[y][x] = color