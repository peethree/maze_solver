from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # The constructor should take a width and height. This will be the size of the new window we create in pixels
        self.width = width
        self.height = height

        #  It should create a new root widget using Tk() and save it as a data member
        self.root = Tk()
        # Set the title property of the root widget
        self.root.title("maze_solver")
        # call the protocol method on the root widget, to connect close method to the "delete window" action.
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        #  Create a Canvas widget and save it as a data member.
        self.canvas = Canvas(self.root, width=width, height=height)
        # Pack the canvas widget so that it's ready to be drawn
        self.canvas.pack(fill=BOTH, expand=True)

        # Create a data member to represent that the window is "running", and set it to False
        self.is_running = False

    def redraw(self):
        # Each time this is called, the window will redraw itself.
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_running = True

        while self.is_running == True:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color="red"):
        line.draw(self.canvas, fill_color)

    
