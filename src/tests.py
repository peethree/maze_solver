import unittest

from maze_class import Maze
from window_class import Window

class TestMaze(unittest.TestCase):        
    def test_maze_creation(self):

        win_x = 800
        win_y = 600
        win = Window(win_x, win_y)

        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )



        win_x = 200 
        win_y = 200
        win = Window(win_x, win_y)

        num_cols = 2
        num_rows = 2
        maze = Maze(0, 0, num_rows, num_cols, 99, 99, win)
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )



        win_x = 1200
        win_y = 900
        win = Window(win_x, win_y)

        num_cols = 20
        num_rows = 3
        maze = Maze(0, 0, num_rows, num_cols, 50, 50, win)
        self.assertEqual(
            len(maze._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze._cells[0]),
            num_rows,
        )
        
    def test_entrance(self):
        win_x = 800
        win_y = 600
        win = Window(win_x, win_y)

        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10, win)

        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[-1][-1].has_bottom_wall)

    
    def test_break_walls_visit(self):
        win_x = 100
        win_y = 100
        win = Window(win_x, win_y)

        num_cols = 3
        num_rows = 4
        maze = Maze(0, 0, num_rows, num_cols, 10, 10, win)
                
        maze._break_walls_r(0, 0)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertTrue(maze._cells[i][j].visited)

  
        

if __name__ == "__main__":
    unittest.main()