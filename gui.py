import pygame
import sys
from Board import *

pygame.init()

rows=6
cols=7
tileSize=100
height=(rows+1)*tileSize
width=cols*tileSize
rad=int(tileSize/2 - 5)

black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
red= (255, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Connect Four Game")

print("")
pygame.quit()

def display_board(board):
    pieceColors={
        0: black,
        1: red,
        2:yellow
    }
    
    for row in range(rows):
        for col in range(cols):
            xPosition=col * tileSize
            yPosition=(row+1)*tileSize
            pygame.draw.rect(screen,blue,(xPosition,yPosition,tileSize,tileSize))
            Xcenter = int(xPosition + tileSize/2)
            yCenter = int(yPosition + tileSize/2)
            color = pieceColors[board[row][col]]
            pygame.draw.circle(screen, color, (Xcenter, yCenter), rad)
    
    pygame.display.update()

    def main():
        board = createBoard()
        gameOver = False
        turn = 0  

