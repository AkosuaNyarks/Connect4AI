from Board import *

def playGame():
    board = createBoard()
    game_over = False
    turn = 0  # 0 = human, 1 = AI
    
    while not game_over:
        printBoard(board)
        # Human turn
        if turn == 0:
            col = int(input("Your turn (0-6): "))
            piece=1
            if isValidMove(board,col):
                row=dropPieces(board, col,piece)
                if checkWin(board,row,col,piece):
                    printBoard(board)
                    print("You Win")
                    game_over=True
            else:
                print("Invalid Move,try again")
                continue
        else:
            # AI's turn
            print("AI is thinking...")
            col=randomMoves(board)
            piece=2
            row=dropPieces(board, col,piece)
            print(f"AI selected column:{col},row:{row}")
                
            if checkWin(board,row,col,piece):
                printBoard(board)
                print("AI Wins")
                game_over=True
        

        turn = (turn + 1) % 2  # Switch turns

if __name__ == "__main__":
    playGame()