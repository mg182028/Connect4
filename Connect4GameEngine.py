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
        
#       Returns:
#       (1) If the move is invalid:  it returns the boolean False
#       (2) If the move is valid, return 8x8 board and winner (0-no winner; 1- player 1; 2- player 2)       

        
# Assumptions:
# Ensure that column number spans 0 to 7 to match indexing of game board 2D list indexing
# Map player input to either a player piece of 1 or -1
# Code finds first empty row starting from "bottom" of board. I treat row 0 as bottom even though it's
# on the top in how it's declared in __init__(self) method above

        self.player = player
        self.column = column-1 #assumes input is 1-8, so this normalizes column to be zero-based
        if self.player == 1:
            playerPiece = 1
        else:
            playerPiece = -1
        self.row = 0
        valid = False
        for i in range (0,8):
            currentVal = abs(self.board[i][self.column])
            if currentVal < 0.5:
                self.row = i
                self.board[self.row][self.column] = playerPiece 
                valid = True
                break
        
        if valid == True:
            state = self.boardState(self.player, self.row, self.column)
            return state
        else:
            return valid
        
        #return state
    
    
    def boardState(self, player, row, column):
# If the move is valid:  this returns the board, whether there is a winner and who won
#    winner: 0-no winner; 1 -> player1 wins; 2 -> player2 wins 

        
# determine column and row ranges to check for winner relative to last player piece placed
#   determine number of iterations for horizonal and vertical winner tests
        minCol = max(column - 3, 0)
        maxCol = min(column + 3, 7)
        minRow = max(row - 3, 0)
        maxRow = min(row + 3, 7)
        
        numHorizIts = 0
        numVertIts = 0
        if (maxCol - minCol) >= 3:
            numHorizIts = (maxCol-minCol)-3 + 1
        if (maxRow - minRow) >= 3:
            numVertIts = (maxRow-minRow)-3 + 1 


#   Determine number of iterations for negative slope diagonal winner tests...  
        #row = 4
        #column = 4                  
        validStart = False
        validFinish = False
        count = 0
        while validStart == False:  
            rowStartNeg = row-3+count
            columnStartNeg = column-3+count
            if rowStartNeg >= 0 and columnStartNeg >= 0:
                validStart = True
            else:
                count = count + 1
        count = 0
        while validFinish == False:  
            rowFinishNeg = row+3-count
            columnFinishNeg = column+3-count
            if rowFinishNeg <= 7 and columnFinishNeg <= 7:
                validFinish = True
            else:
                count = count + 1
        numNegDiagIts = max(abs(rowFinishNeg - rowStartNeg)-3+1,0)

#   Determine number of iterations for positive slope diagonal winner tests...  


        validStart = False
        validFinish = False
        count = 0
        while validStart == False:  
            rowStartPos = row+3-count
            columnStartPos = column-3+count
            if rowStartPos <= 7 and columnStartPos >= 0:
                validStart = True
            else:
                count = count + 1
        count = 0        
        while validFinish == False:  
            rowFinishPos = row-3+count
            columnFinishPos = column+3-count
            if rowFinishPos >= 0 and columnFinishPos <= 7:
                validFinish = True
            else:
                count = count + 1    
        numPosDiagIts = max(abs(rowFinishPos - rowStartPos)-3+1,0)

        
        winner = 0

#Test horizontal for a win   ######## Horizontal test seems to work, but continues testing even after finding a win     
# Could it be nested while statements that flag off of whether winner is set to non-zero rather than break statements?
        if numHorizIts>0:
            for Its in range(0, numHorizIts):
                horiz_test = 0
                for horiz in range(minCol+Its, minCol+3+Its+1):
                    horiz_test = horiz_test + self.board[row][horiz]
                    if abs(horiz_test)>3:
                        winner = player
                        #print(row, column, " Horiz winner is player ", winner)  #Test code
                        break

##Test vertical for a win
        if winner == 0:           
            if numVertIts>0:
                for Its in range(0, numVertIts):
                    vert_test = 0
                    for vert in range(minRow+Its, minRow+3+Its+1):
                        vert_test = vert_test + self.board[vert][column]
                        if abs(vert_test)>3:
                            winner = player
                            #print(row, column," Vert winner is player ", winner)  # Test code
                            break

#Test Negative Diagonal for a win -- test is going out of bounds for both positive Diagonals
        if winner == 0:  
            if numNegDiagIts>0:
                for Its in range(0, numNegDiagIts):
                    NegDiag_test = 0
                    for negDiag in range(Its, Its+4):
                        tempNegRow = rowStartNeg+negDiag
                        tempNegCol = columnStartNeg+negDiag
                        #print(row, column, tempNegRow, tempNegCol, Its)
                        NegDiag_test = NegDiag_test + self.board[tempNegRow][tempNegCol]
                        if abs(NegDiag_test)>3:
                            winner = player
                            #print(row, column, " NegDiag winner is player ", winner)  #Test code
                            break

#Test Positive Diagonal for a win
        if winner == 0:  
            if numPosDiagIts>0:
                for Its in range(0, numPosDiagIts):
                    PosDiag_test = 0
                    for posDiag in range(Its, Its+4):
                        tempPosRow = rowStartPos-posDiag
                        tempPosCol = columnStartPos+posDiag
                        #print(row, column, tempPosRow, tempPosCol, Its)
                        PosDiag_test = PosDiag_test + self.board[tempPosRow][tempPosCol]
                        if abs(PosDiag_test)>3:
                            winner = player
                            #print(row, column," PosDiag winner is player ", winner)  # Test code
                            break


        
        return [self.board, winner]




