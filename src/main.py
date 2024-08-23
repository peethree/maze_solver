from window_class import Window
from point_class import Point, Line
from cell_class import Cell


def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)    

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)    

    c2 = Cell(win)
    c2.has_bottom_wall = False
    c2.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)
    c.draw_move(c2, undo=True)

    win.wait_for_close()
    
    
    


if __name__ == "__main__":
    main()