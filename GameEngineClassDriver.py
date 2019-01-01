#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:20:30 2018

@author: dad
"""

##### Driver code for testing class
# This is a very basic driver that I modify as needed to check out 
# various behaviors


from Connect4GameEngine import GameBoardConnect4
import random


        
game = GameBoardConnect4()

player = 2
sampleSize = 64
column = [random.randint(1,8) for i in range(sampleSize)]
#column = [1] * sampleSize
for i in range(0,sampleSize):
    print("\n")
    myboard = game.playerAction(player,column[i])
    if myboard == False:
        print("Invalid Move")
        print(player,"\n")
#    print(column[i], player)
    else:
        #myboard = game.boardState()
        finalBoard = myboard[0]
        winner = myboard[1]
        #print(myboard[1])
        #print("\n")
        for i in range(1,9):
            pass
            print(finalBoard[i-1][:])  
        print("winner is ", winner)
        #print(game.boardState()
        player = player%2 + 1
        #print (player)