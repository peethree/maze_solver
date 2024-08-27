from window_class import Window
from maze_class import Maze


def main():    

    num_rows = 24
    num_cols = 24

    margin = 25

    win_x = 1200
    win_y = 900

    cell_size_x = (win_x - 2 * margin) / num_cols
    cell_size_y = (win_y - 2 * margin) / num_rows

    win = Window(win_x, win_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    maze.solve()

    win.wait_for_close()
          

if __name__ == "__main__":
    main()