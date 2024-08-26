from window_class import Window
from point_class import Point, Line
from cell_class import Cell
from maze_class import Maze


def main():    

    num_rows = 10
    num_cols = 8

    margin = 5

    win_x = 800
    win_y = 600

    cell_size_x = (win_x - 2 * margin) / num_cols
    cell_size_y = (win_y - 2 * margin) / num_rows

    win = Window(win_x, win_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    

    win.wait_for_close()
          

if __name__ == "__main__":
    main()