import numpy as np
import random as rnd

'''Still a work in progress'''

# Breyta input, það er gallað, 

    # leyfa leikmanni
    # að breyta gildum sem hann setti inn, 
    # en ekki breyta gildum sem voru í
    # upprunalega borðinu

    # Gera input aðeins þægilegra þetta format 
    # er leiðinlegt að díla við

    # koma með error messages í inputum

# Bæta við difficulty
    # t.d. dno

# Setja intro texta í txt skjal?


class Sudoku:
    EMPTY = '·'
    GET_MOVE = 'Enter move: '
    MAP_ROWS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 
                'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
    
    def __init__(self, difficulty=None):
        '''Sudoku board is made immidiataly'''
        self.grid = np.zeros([9,9], dtype=int)
        self.counter = 1
        self.solutions = []
        # self.grid = np.array([[0,5,3,2,7,6,1,8,9],
        #                     [7,9,1,3,8,4,2,6,5],
        #                     [6,2,8,1,9,5,7,4,3],
        #                     [8,3,5,9,6,2,4,7,1],
        #                     [2,1,7,4,3,8,9,5,6],
        #                     [9,4,6,7,5,1,3,2,8],
        #                     [1,8,2,6,4,9,5,3,7],
        #                     [3,6,4,5,1,7,8,9,2],
        #                     [5,7,9,8,2,3,6,1,4]])
        # self.get_solutions()
        self._make_grid() 

    def __str__(self):
        '''Returns sudoku board in a certain format'''
        table_top = ' |_A_B_C___D_E_F___G_H_I_|\n'
        table_bottom = ' |-----------------------|\n'
        table_mid = ' |-------+-------+-------|\n'

        string = table_top
        for r in range(9):
            # counter for rows
            string += f'{r+1}| '

            for c in range(9):
                # add the number
                num = self.grid[r][c]

                # Add other chars in certain positions
                if c in [3, 6]:
                    string += '| '
                if num == 0:
                    num = Sudoku.EMPTY
                string += f'{num} '

            string += '|\n'
            if r in [2, 5]:
                string += table_mid

        string += table_bottom
        return string

    def _make_grid(self):
        '''Make a sudoku board with only one solution'''
        # Random inputs
        row = rnd.randrange(0,9)
        col = rnd.randrange(0,9)
        num = rnd.randrange(1,10)

        # if random input is a legal input in the board
        if self._possible(row, col, num):

            # insert number into place
            self.grid[row][col] = num

            # find possible solutions to board
            self.solutions = []
            self.get_solutions()

            # if zero solutions then we backtrack
            if len(self.solutions) == 0:
                self.grid[row][col] = 0
                self._make_grid()

            # if more than one solution then we do another cycle
            elif len(self.solutions) > 1:
                self._make_grid()
            else:
                return
        else:
            self._make_grid() # if the random number was not valid 
                              # then we try again

    def _input_to_indexes(self, coordinates):
        '''Transform coordinates to indexes'''
        row = int(coordinates[1]) -1 
        col = Sudoku.MAP_ROWS[coordinates[0].upper()]
        return row, col

    def intro(self):
        return "\nInput on this format '1 A1'\n--------Game Starts--------\n"

    def update_board(self, row, col, number):
        '''Insert a number into grid or remove a number'''
        self.grid[row][col] = number

    def get_move(self):
        '''Makes sure user enter move in right format'''
        # This way is a work in progress
        while True:
            move = list(input(f'{Sudoku.GET_MOVE}'))

            if len(move) == 4:
                if move[0].isdigit() and move[-1].isdigit():
                    if move[2].upper() in Sudoku.MAP_ROWS.keys():

                        number = int(move[0])
                        coordinates = ''.join(move[2:])
                        row, col = self._input_to_indexes(coordinates)

                        if self._possible(row, col, number):
                            return row, col, number

    def _column(self, c):
        '''Return the column of a matrix'''
        return [row[c] for row in self.grid]

    def _possible(self, r, c, num):
        '''
        Check if number is possible
        
        r -> row
        c -> column
        num -> number to insert in row and column
        '''

        # check if cell is occupied
        if self.grid[r][c] == 0: 
            # checking the row
            if num not in self.grid[r]:
                # checking the column
                if num not in self._column(c):

                    # checking the cell
                    r_0 = (r//3)*3  # r_0 and c_0, will always be
                    c_0 = (c//3)*3  # the upper left number for any cell.

                    for i in [0,1,2]:
                        for j in [0,1,2]:
                            if self.grid[r_0+i][c_0+j] == num:
                                return False
                    return True
        return False

    def get_solutions(self, all_solutions=False):
        '''Find how many solutions are available using Using djikstra algorithm and recursion.
        
        all_solutions -> Gives user the ability to get all solutions,
                         making the default 2 solution speeds up program.
        '''
        # Goes through the sudoku board and finds the solution, if more than one it quits.
        if len(self.solutions) <= 1 or all_solutions:

            # go through the board number by number
            for r in range(9):
                for c in range(9):

                    # if cell is empty, then we give it a number
                        # Go through numbers 1-9
                            # if possible.
                                # Then we call the function again. 
                    if self.grid[r][c] == 0:
                        for num in range(1,10):
                            self.counter += 1
                            if self._possible(r,c,num):
                                self.grid[r][c] = num
                                self.get_solutions()
                                self.grid[r][c] = 0
                            if len(self.solutions) > 1 or all_solutions:
                                return
                        return
        # save the solution to a list
        self.solutions.append(self.grid.copy())

    def victory(self):
        '''Check if there is a vicory in any of the solutions'''
        for solution in self.solutions:
            if self.grid.all() == solution.all():
                return True
        return False

    def play_again(self):
        '''Gets a valid input if player wants to play again'''
        while True:
            again = input('Want to play again (y/n): ')
            if again.lower() in ['y', 'yes', 'yeah', 'já']:
                return True
            elif again.lower() in ['n', 'no', 'nah', 'hell no', 'nei']:
                return False

            print('Not valid\n')

    def play(self):
        '''Play the game'''
        print(self.counter)
        print(self.intro())
        print(self)
        while self.victory() == False:
            row, col, num = self.get_move()
            self.update_board(row, col, num)
            print(self)
        print('Congratulations you have won the game!!!')
        again = self.play_again()
        if again:
            self.__init__()
            self.play()

if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.play()