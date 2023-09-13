# The implementation of the Conway's Game of Life.
# The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
# The code written by Alexander Kilinkarov.

from copy import deepcopy
from random import choice
from math import sqrt


class Cell:
    def __init__(self, x, y, s, c=255):
        self.x = x
        self.y = y
        self.s = s
        self.c = c
        self.alive = False
    
    def show(self):
        if self.alive:
            fill(self.c)
        else:
            fill(90)
        
        ellipse(self.x, self.y, self.s, self.s)


def setup():
    # fullScreen()
    size(1000, 1000)
    frameRate(30)
    global cols, rows, game_plays, cells
    s = 20
    cols = width//s
    rows = height//s
    game_plays = False
    ellipseMode(CENTER)
    cells = [[Cell(s//2 + (col-1)*s, s//2 + (row-1)*s, s, c=color(0, 255, 0)) for col in range(cols+2)] for row in range(rows+2)]

    
def draw():
    global cells, cols, rows
    background(30)
    if game_plays:
        # game plays and cells change their state
        cells2 = deepcopy(cells)
        
        for row in range(1, len(cells2)-1):
            for col in range(1, len(cells2[row])-1):
                cells[row][col].show()
                
                # count neibours
                neibours_count = sum([i.alive for i in cells2[row-1][col-1:col+2]]) + cells2[row][col-1].alive + cells2[row][col+1].alive + \
                    sum([i.alive for i in cells2[row+1][col-1:col+2]])
            
                if neibours_count == 3 and not cells2[row][col].alive:
                    cells[row][col].alive = True
                elif cells2[row][col].alive and neibours_count not in (2, 3):
                    cells[row][col].alive = False
    else:
        # if game stopped only show the field
        for row in range(1, len(cells)-1):
            for col in range(1, len(cells[row])-1):
                cells[row][col].show()


# set cells to alive state with mouse click
def mousePressed():
    global cells
    for row in range(1, len(cells)-1):
        for col in range(1, len(cells[row])-1):
            deltaX = abs(mouseX - cells[row][col].x)
            deltaY = abs(mouseY - cells[row][col].y)
            if sqrt(deltaX**2 + deltaY**2) <= cells[row][col].s//2 and not cells[row][col].alive:
                cells[row][col].alive = True
    

def keyPressed():
    global game_plays, cells
     
    # start/pause the game
    if key == "1":
        game_plays = False if game_plays else True
    
    # set random values on the field
    elif key == "2":
        for row in range(1, len(cells)-1):
            for col in range(1, len(cells[row])-1):
                cells[row][col].alive = choice([True, False])
                
    # exit game. Doesn't work
    elif key == ESC:
        exit()
    

    
