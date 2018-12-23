#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 11:41:30 2018

@author: dad
"""

class GameBoardConnect4():
    def __init__(self):
# Initialize game board to be all zeros
        self.board = [ [ 0,  0,  0,  0,  0,  0,  0,  0 ], \
                     [   0,  0,  0,  0,  0,  0,  0,  0 ], \
                     [   0,  0,  0,  0,  0,  0,  0,  0 ], \
                     [   0,  0,  0,  0,  0,  0,  0,  0 ], \
                     [   0,  0,  0,  0,  0,  0,  0,  0 ], \
                     [   0,  0,  0,  0,  0,  0,  0,  0 ], \
                     [   0,  0,  0,  0,  0,  0,  0,  0 ], \
                     [   0,  0,  0,  0,  0,  0,  0,  0 ]]
    
    def playerAction(self, player, column):
#       Interface questions:
#       (1) column will come as 0 to 7 or as 1 to 8; need to make sure this code is consistent
#       (2) Need to convert player into either 1 or -1 depending on if player 1 or 2

# Ensure that column number spans 0 to 7 to match indexing of game board 2D list indexing
# Map player input to either a player piece of 1 or -1
# Code finds first empty row starting from "bottom" of board. I treat row 0 as bottom even though it's
# on the top in how it's declared in __init__(self)

        self.player = player
        self.column = column-1
        if player == 1:
            playerPiece = 1
        else:
            playerPiece = -1
        self.row = 0
        for i in range (0,8):
            currentVal = abs(self.board[i][self.column])
            if currentVal < 0.5:
                self.row = i
                self.board[self.row][self.column] = playerPiece 
                break
        return 
    
    
    def boardState(self):
# This returns the board. It can be used for drawing graphics or for debug
        return self.board




