from window_class import Window
from point_class import Point, Line

def main():
    win = Window(800, 600)

    line = Line(Point(500, 100), Point(700, 400))
    win.draw_line(line, "red")    


    win.wait_for_close()
    
    


if __name__ == "__main__":
    main()