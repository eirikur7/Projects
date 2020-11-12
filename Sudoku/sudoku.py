import numpy as np

class Sudoku:
    EMPTY = '·'
    MAP_ROWS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 
                'F':5, 'G':6, 'H':7, 'I':8, 'J':9}
    def __init__(self, difficulty=None):
        self.__MakeGrid()
    
    # Returns 9x9 grid
    def __MakeGrid(self):
        self.grid = np.array([[0,0,5,3,0,0,0,0,0],
        [8,0,0,0,0,0,0,2,0],
        [0,7,0,0,1,0,5,0,0],
        [4,0,0,0,0,5,3,0,0],
        [0,1,0,0,7,0,0,0,6],
        [0,0,3,2,0,0,0,8,0],
        [0,6,0,5,0,0,0,0,9],
        [0,0,4,0,0,0,0,3,0],
        [0,0,0,0,0,9,7,0,0]])

    def intro(self):
        string = '''Jaok þú vilt spile sudoku, flott hjá þér.
Stimplaðu inn númer og svo hnit til að setja inn númar --> 2 A3
Til þess að taka út númer þarftur aðeins að setja núll í staðinn --> 0 A3
--------LeikuByrjar--------\n'''
        return string
        
    # prints board
    def __str__(self):
        '''Returns sudoku board in a certain format'''
        table_top = ' |_A_B_C___D_E_F___G_H_I_|\n'
        table_bottom = ' |-----------------------|\n'
        table_md = ' |-------+-------+-------|\n'

        string = table_top
        for r in range(9):
            string += f'{r+1}| '
            for c in range(9):
                num = self.grid[r][c]
                if c in [3, 6]:
                    string += '| '
                if num == 0:
                    num = Sudoku.EMPTY

                string += f'{num} '
            string += '|\n'

            if r in [2, 5]:
                string += table_md

        string += table_bottom
        return string

    # in -> '5 A2'... out -> 5, 1, 1
    def _CoordinatesToRC(self, coordinates):
        '''Transform coordinates to indexes'''
        row = int(coordinates[1]) -1 
        col = Sudoku.MAP_ROWS[coordinates[0].upper()]
        return row, col

    # changes value in grid to specified
    def update_board(self, number=0, coordinates=0):
        '''Insert a number into grid or remove a number'''
        row , col = self._CoordinatesToRC(coordinates)
        self.grid[row][col] = number

    def check_win(self):
        '''
        Only check if grid has been filled in with 
        num: 1 --> 9, where the sum is 405
        '''
        if np.sum(self.grid) == 405:
            return True
        else:
            return False

    def get_move(self, a_string):
        '''Makes sure user enter move in right format'''
        while True:
            move = list(input(f'{a_string}'))
            if len(move) == 4:
                if move[0].isdigit() and move[-1].isdigit():
                    if move[2].upper() in Sudoku.MAP_ROWS.keys():
                        number = int(move[0])
                        cord = ''.join(move[2:])
                        return number, cord


play = True
while play:
    board = Sudoku()
    print(board.intro())
    while board.check_win() == False:
        print(board)
        number, coordinates = board.get_move('Enter move: ')
        board.update_board(number, coordinates)

    




# Make sudoku grid
    # make array 9x9
    # insert random numbers in grid
    # possibly make it difficulty based

# print grid

# user can insert a number
    # user inputs number along with coordinates
    # f.x. --> 5 A2

# user can remove a number

# print --> next play, (i)nsert or (r)emove
    # input i or r
    # then number and coordinates