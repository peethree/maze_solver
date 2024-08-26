from cell_class import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed

        if self.seed is not None:
            self.seed = random.seed(seed)
        

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        self._cells = []

        # Each top-level list is a column of Cell objects. 
        # [[cell, cell, cell], [cell, cell, cell], [cell, cell, cell]]

        for i in range(self.num_cols):
            columns = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                columns.append(cell)
        
            self._cells.append(columns)

        # Once the matrix is populated it should call its _draw_cell() method on each Cell.
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)     
        

    def _draw_cell(self, i, j):
        # starting pos x/y + cell size -- i: horizontal, j: vertical
         
        x1 = self.x1 + i * self.cell_size_x
        x2 = x1 + self.cell_size_x
    
        y1 = self.y1 + j * self.cell_size_y
        y2 = y1 + self.cell_size_y
    
        # access the specific cell
        cell = self._cells[i][j]
        # draw it 
        cell.draw(x1, y1, x2, y2)

        # animate after drawing
        self._animate()


    def _animate(self):        
        self.win.redraw()   
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # The entrance to the maze will always be at the top of the top-left cell, 
        # the exit always at the bottom of the bottom-right cell.
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]

        entrance_cell.has_top_wall = False
        # first cell index
        self._draw_cell(0, 0)

        exit_cell.has_bottom_wall = False
        # last cell index
        self._draw_cell(len(self._cells) - 1, len(self._cells[-1]) - 1)

        
        
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]        

        #  Mark the current cell as visited
        current_cell.visited = True

        while True:
            # Create a new empty list to hold the i and j values you will need to visit
            coordinates = []
            # Check the cells that are directly adjacent to the current cell. 
            # Keep track of any that have not been visited as "possible directions" to move to
            
            # cell to the left
            if i > 0 and not self._cells[i - 1][j].visited:
                coordinates.append((i - 1, j))
            # cell to the right
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                coordinates.append((i + 1, j))
            # cell above
            if j > 0 and not self._cells[i][j - 1].visited:
                coordinates.append((i, j - 1))
            # cell down
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                coordinates.append((i, j + 1))

            # no more cells to visit
            if len(coordinates) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction = random.randrange(len(coordinates))
            next_coord = coordinates[direction]

            
    
            # remove left wall
            if next_coord[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            # remove right wall
            if next_coord[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False           
        
            # remove top wall
            if next_coord[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # remove bottom wall
            if next_coord[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_coord[0], next_coord[1])


