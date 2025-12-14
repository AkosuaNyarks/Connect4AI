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
pygame.display.set_caption("Let's Play Connect Four!")

print("")


def displayBoard(board):
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

    displayBoard(board)
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type==pygame.MOUSEBUTTONDOWN and turn ==0:
                posX= event.pos[0]
                col=int(posX//tileSize)

                if isValidMove(board,col):
                    row=dropPieces(board,col,1)
                    displayBoard(board)

                    if checkWin(board,row,col,1):
                        print(" You've Won against the Agent! You're so Smart!")
                        gameOver=True
                    else:
                        turn=1
                else:
                    print("Invalid Move")
        if turn == 1 and not gameOver:
                print("AI is thinking...")
                pygame.time.wait(500)  
            
                col = getBestMove(board, 6)
                row = dropPieces(board, col, 2)
                displayBoard(board)
                print(f"AI selected column:{col}")
            
                if checkWin(board, row, col, 2):
                    print("AI Wins!Better Luck")
                    gameOver = True
                else:
                    turn = 0  # Back to human
    
    pygame.time.wait(3000)  # Wait 3 seconds before closing

if __name__ == "__main__":
    main()


