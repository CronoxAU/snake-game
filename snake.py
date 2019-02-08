#Snake game based on the tutorial from https://www.youtube.com/watch?v=CD4qAhfFuLo

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
    
    def move(self, dirnx, dirny):
        pass
    
    def draw(self,surface,eyes=False):
        pass

class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass
    
    def reset(self, pos):
        pass
    
    def addCube(self):
        pass
    
    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):

    pass

def redrawWindow(surface):
    win.fill((0,0,0))
    drawGrid(surface)
    pygame.display.update()
    pass

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    width = 500
    rows = width/25
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0),(rows/2,rows/2))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
    pass



main()
