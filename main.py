from Board import *

def playGame():
    board = createBoard()
    gameOver = False
    turn = 0  # 0 = human, 1 = AI
    
    while not gameOver:
        printBoard(board)
        # Human turn
        if turn == 0:
            colInput = input("Your turn (0-6): ")

            if not colInput.isdigit():
                print("Please enter a valid number (0-6).")
                continue
            
            col=int(colInput)

            if col < 0 or col > 6:
                print("Invalid column! Please choose 0-6.")
                continue

            piece=1
            if isValidMove(board,col):
                row=dropPieces(board, col,piece)
                if checkWin(board,row,col,piece):
                    printBoard(board)
                    print("You Win")
                    gameOver=True
            else:
                print("column is full,try another column")
                continue
        else:
            # AI's turn
            print("AI is thinking...")
            col=getBestMove(board,6)
            piece=2
            row=dropPieces(board, col,piece)
            print(f"AI selected column:{col},row:{row}")
                
            if checkWin(board,row,col,piece):
                printBoard(board)
                print("AI Wins")
                gameOver=True 

        turn = (turn + 1) % 2  # Switch turns
        if not gameOver and len(getValidColumns(board))==0:
            printBoard(board)
            print("Draw")
            gameOver=True
        

if __name__ == "__main__":
    playGame()