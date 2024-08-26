from cell_class import Cell
import time


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
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()

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
 
        # if i == 0:
        #     x1 = self.x1
        #     x2 = x1 + self.cell_size_x

        # if j == 0:
        #     y1 = self.y1
        #     y2 = y1 + self.cell_size_y

        if i > 0:
            x1 = self.x1 + i * self.cell_size_x
            x2 = x1 + self.cell_size_x

        if j > 0:
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