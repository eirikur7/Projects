import numpy as np

class ChessPieces(Chess):
    '''A class that hold the rules for each chess player'''
    '''
       a  b  c  d  e  f  g  h
    8  -  -  -  -  -  -  -  -
    7  -  -  -  -  -  -  -  -
    6  -  -  -  -  -  -  -  -
    5  -  -  -  -  -  -  -  -
    4  -  -  -  -  -  -  -  -
    3  -  -  -  -  -  -  -  -
    2  -  -  -  -  -  -  -  -
    1  -  -  -  -  -  -  -  -
    '''
    def __init__(self):
        ''' i '''
        # make a dictionary that holds the pixels for each piece

    def __str__(self):
        pass
    def available_squares(self, piece):
        '''Return which square are available to a piece'''
        if piece is 'pawn':
            self.__pawn()
        elif piece is 'rook':
            self.__rook()
        elif piece is 'bishop':
            self.__bishop()
        elif piece is 'knight':
            self.__knight()
        elif piece is 'queen':
            self.__queen()
        elif piece is 'king':
            self.__king()

    def __pawn():
        '''Find available squares for pawn'''
        