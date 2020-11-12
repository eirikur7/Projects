class TicTacToe:
    EMPTY = ' '
    PLAYER_1 = 'O'
    PLAYER_2 = 'X'

    # initializes _board
    def __init__(self, bot=False):
        '''User can pick 2player or play against bot'''
        E = TicTacToe.EMPTY
        self._board = [[E,E,E],[E,E,E],[E,E,E]]

    # Displays board
    def __str__(self):
        '''Display tic tac toe board'''
        table_tb = '\n -----------\n'
        table_md = '|\n|---|---|---|\n'

        string = table_tb
        for i, line in enumerate(self._board):
            for el in line:
                string += f'| {el} '
            if i in [0,1]:
                string += table_md
        string += '|' + table_tb
        return string


    def make_move(self, row, col , player):
        '''Insert value for player'''
        self._board[row][col] = player

    def get_move(self, player):
        while True: 
            move = list(input(f"It's {player} move --> "))

            # check if length matches
            if len(move) == 2:

                # check if values matches size of board
                if move[0] in '123' and move[1] in '123':
                    row, col = int(move[0])-1, int(move[1])-1

                    # check if cell is empty
                    if self.check_valid(row, col):
                        return row, col
                    
                    print('Cell is occupied')
                    continue
                print('Values chosen do not match criteria --> [1 ,2 ,3]')
                continue
            print('Input coordinates, f.x. --> 11 or 12 or 32.')
            continue


    def get_winner(self):
        for i in range(len(self._board)):
            if self._board[i][0] == self._board[i][1] == self._board[i][2] and self._board[i][0] != TicTacToe.EMPTY:
                return self._board[i][0]
            elif self._board[0][i] == self._board[1][i] == self._board[2][i] and self._board[0][i] != TicTacToe.EMPTY:
                return self._board[0][i]
        return False

    def check_valid(self, row, col):
        if self._board[row][col] == TicTacToe.EMPTY:
            return True
        else:
            return False

    def play(self):
        '''Starts game'''
        winner = False
        player = TicTacToe.PLAYER_2
        while winner == False:
            # Checks which players turn it is
            if player == TicTacToe.PLAYER_1:
                player = TicTacToe.PLAYER_2
            else:
                player = TicTacToe.PLAYER_1

            # Getting next move and updating board corresponding move.
            print(self.__str__())
            row, col = self.get_move(player)
            self.make_move(row, col, player)

            winner = self.get_winner()

        print(self.__str__())
        print(f'Congratulations -> {winner} <- is MVP!!')

    def __bot(self):
        '''Maybe add a bot later on'''



board = TicTacToe()
choice = 'y'
while choice is 'y':
    board = TicTacToe()
    board.play()
    choice = input('Want to play again, y/n: ')

# input -- play against computer or human

# computer
    # who starts
    # O starts

# human
    # O starts
