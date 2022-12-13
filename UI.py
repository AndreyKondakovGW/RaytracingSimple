from tkinter import PhotoImage, Tk, Button, Scale, Entry,StringVar, Frame
from canvas import MyCanvas


class UI(Tk):
    def __init__(self, titel="Painter", width=0, height=0):
        super().__init__()

        if width == 0:
            self.win_width = self.winfo_screenwidth()
        else:
            self.win_width = width
        if height == 0:
            self.win_height = self.winfo_screenheight()
        else:
            self.win_height = height

        self.title(titel)

        self.canv = MyCanvas(self, width=self.win_width, height=self.win_height, bg="white")
        self.canv.grid(row=1, column=1)

    def run(self):
        self.mainloop()