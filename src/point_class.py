from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):        
        self.x = x
        self.y = y


# takes 2 points as input
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="red"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)