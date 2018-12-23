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

player = 0
sampleSize = 100
column = [random.randint(1,8) for i in range(sampleSize)]
#column = [1] * sampleSize
for i in range(0,sampleSize):
    #column = i%3+1
    if i > 10:
        player = 1
    else:
        player = 2
#    print(column[i], player)
    game.playerAction(player,column[i])

myboard = game.boardState()

for i in range(1,9):
    print(myboard[i-1][:])   
#print(game.boardState())