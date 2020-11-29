import numpy as np
import random as rnd

'''Still a work in progress'''

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
        self.__MakeGrid()
        
    # Returns 9x9 grid
    def __MakeGrid_tilbuid(self):
        '''Temporary while I figure out how to make a sudoku board'''
        self.grid = np.array([[0,0,5,3,0,0,0,0,0],
        [8,0,0,0,0,0,0,2,0],
        [0,0,0,0,1,0,5,0,0],
        [4,0,0,0,0,5,3,0,0],
        [0,1,0,0,7,0,0,0,6],
        [0,0,3,2,0,0,0,8,0],
        [0,6,0,5,0,0,0,0,9],
        [0,0,4,0,0,0,0,3,0],
        [0,0,0,0,0,9,7,0,0]])

    def __MakeGrid_2(self):
        pass
        

    def __MakeGrid(self):
        '''Make a sudoku board with only one solution'''
        row = rnd.randrange(0,9)
        col = rnd.randrange(0,9)
        num = rnd.randrange(1,10)
        print(self.grid)
        if self.__possible(row, col, num):
            self.grid[row][col] = num

            self.solutions = []
            self.get_solutions()
            print(len(self.solutions))
            if len(self.solutions) == 0:
                self.grid[row][col] = 0
            elif len(self.solutions) > 1:
                self.__MakeGrid()
            else:
                return
        else:
            self.__MakeGrid()

    def intro(self):
        return "Input á formi '1 A1'\n þ.e. 'Tala xHnit_yHnit'\n--------LeikurByrjar--------\n"
        
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

    def __CoordinatesToIndexes(self, coordinates):
        '''Transform coordinates to indexes'''
        row = int(coordinates[1]) -1 
        col = Sudoku.MAP_ROWS[coordinates[0].upper()]
        return row, col

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
                        row, col = self.__CoordinatesToIndexes(coordinates)

                        if self.__possible(row, col, number):
                            return row, col, number

    def __column(self, c):
        '''Return the column of a matrix'''
        return [row[c] for row in self.grid]

    def __possible(self, r, c, num):
        '''Check if number is possible'''
        # checking the row
        if num not in self.grid[r]:
            # checking the column
            if num not in self.__column(c):

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
        '''Find how many solutions are available'''
        # Using djikstra algorithm and recursion.
        # Goes through the sudoku board and finds the solution, if more than one it quits.
        if len(self.solutions) <= 1:

            # go through the board number by number
            for r in range(9):
                for c in range(9):

                    # if cell is empty, then we give it a number
                    # if possible.
                    # Then we call the function again. 
                    if self.grid[r][c] == 0:
                        for num in range(1,10):
                            if self.__possible(r,c,num):
                                self.grid[r][c] = num
                                self.get_solutions()
                                self.grid[r][c] = 0
                            if len(self.solutions) > 1:
                                return
                        return
        # save the solution to a list
        self.solutions.append(self.grid.copy())

    def play(self):
        '''Play the game'''
        board = Sudoku()
        print(board.intro())
        while board.check_win() == False:
            print(board)
            row, col, number = board.get_move()
            board.update_board(row, col, number)

    def testing_make_grid(self):
        self.__MakeGrid()
        print(self.grid)

    def test(self):
        self.solutions = []
        self.get_solutions()
        print(self.solutions)


sudoku = Sudoku()
print(sudoku)
sudoku.test()

