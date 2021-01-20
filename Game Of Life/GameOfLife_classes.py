import numpy as np
import random as rnd
import copy
import matplotlib.pyplot as plt
from matplotlib import animation, rc, cm
rc('animation', html='html5')

"""A program that simulates John Conway's game of life"""

class Board(object):
    def __init__(self, row, col, empty=False):
        '''
        Rows and columns established,
        grid is made either empty or not.
        '''
        self.row = row
        self.col = col

        if empty:
            self.grid = self._make_empty_grid()
        else:
            self.grid = self._make_random_grid()
        

    def _make_random_grid(self):
        '''
        Makes an array filled with random ones and 
        '''
        return np.random.randint(2, size=(self.row, self.col))


    def _make_empty_grid(self):
        '''
        Makes an array filled with zeros
        '''
        return np.zeros((self.row, self.col), dtype=int)


class Game(Board):
    '''Class does operation on the grids'''
    SIZE = 100  ##### Change SIZE here #####

    LIVE_MIN = 2 # minimum neighbours to keep living, def.2
    LIVE_MAX = 3 # maximum neighbours to keep living, def.3
    DEAD_ON = 3  # Number of neighbours to resurect,  def.3

    def __init__(self):
        '''
        Making 2 grids
        nr.1 is to check each cell.
        nr.2 is used to update the grid
        '''
        self.grid_1 = Board(Game.SIZE, Game.SIZE, empty=False).grid
        self.grid_2 = np.zeros_like(self.grid_1)

    def __str__(self):
        '''Returns grid_2 in string format'''
        string = ''
        for row in self.grid_2:
            for c in row:
                string += str(c)
            string += '\n'
        return string

    def _get_neighbours(self, r, c):
        '''
        Calculates number of live neighbours around a given cell [r,c]

        r -> row
        c -> column

        Example:
        # [1,2,3]   The code goes around the cell in row r and column c,
        # [4,5,6]   and counts the number of live neighbours
        # [7,8,9]   then it subtracts it-self
        '''
        self.total = 0 # Total neighbours

        for rr in [-1, 0, 1]: # row
            for cc in [-1, 0, 1]: # col

                if r+rr == -1 or c+cc == -1: # edges, 
                    continue
                elif r+rr == Game.SIZE or c+cc == Game.SIZE:
                    continue
                else:
                    self.total += self.grid_1[r+rr][c+cc]
        # Only count neighbours so we subtract the middle cell (r,c)
        self.total -= self.grid_1[r][c]


    def _update_table(self, r, c):
        '''
        Table is updated with Conway's Rules
        '''
        if self.grid_1[r][c]  == 1: 
            if self.total < Game.LIVE_MIN or self.total > Game.LIVE_MAX: 
                self.grid_2[r][c] = 0
            else:
                self.grid_2[r][c] = 1

        else: 
            if self.total == Game.DEAD_ON: 
                self.grid_2[r][c] = 1


    def cycle(self):
        '''
        Call method to cycle through game one time
        '''
        for r in range(Game.SIZE):
            for c in range(Game.SIZE):

                self._get_neighbours(r, c)
                self._update_table(r, c)

        self.grid_1 = copy.deepcopy(self.grid_2)
        #self.grid_1 = self.grid_2





grid = Game()

def updatefig(frame, *fargs):
    grid.cycle()
    im.set_array(grid.grid_1)
    return im,


fig, ax = plt.subplots()
ax.axis('off')
im = plt.imshow(grid.grid_1, interpolation = "nearest", animated=True)
anim = animation.FuncAnimation(fig, updatefig, frames=100, interval=200, blit=True)
plt.show()
anim

