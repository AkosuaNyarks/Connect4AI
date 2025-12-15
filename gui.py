import pygame
import sys
import random
from Board import *

pygame.init()
font = pygame.font.Font(None, 50) 

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

def confetti():
    colors = [red, yellow, blue, (255, 0, 255), (0, 255, 255), (255, 165, 0)]
    for i in range(50):
        x=random.randint(0,width)
        y=random.randint(0,height)
        color = random.choice(colors)
        size = random.randint(5, 15)
        pygame.draw.circle(screen, color, (x, y), size)


def display_winner(board, winner_text):
    for i in range(30):
        displayBoard(board)
        confetti()
        
        text = font.render(winner_text, True, white)
        text_rect = text.get_rect(center=(width//2, 50))
        
        pygame.draw.rect(screen, black, text_rect.inflate(20, 20))
        screen.blit(text, text_rect)
        
        pygame.display.update()
        pygame.time.wait(100)

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
                        display_winner(board, "Excellent! You won against the AI! So smart!")
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
                    display_winner(board, "AI wins! Too bad better luck next time!")
                    gameOver = True
                else:
                    turn = 0  # Back to human
        if not gameOver and len(getValidColumns(board)) == 0:
            display_winner(board, "It's a Draw! 🤝") 
            gameOver = True
    
    pygame.time.wait(3000)  

if __name__ == "__main__":
    main()


