from Board import *

if __name__=="__main__":
    board=createBoard()
    print("Board Created")
    printBoard(board)

    print("\n Dropping piece 1 in coulmn 3:")
    success=dropPieces(board,3,1)
    printBoard(board)

    print("\n Dropping piece 2 in coulmn 3:")
    success=dropPieces(board,3,2)
    printBoard(board)

    print("\n Checking for valid Moves:")
    valid=isValidMove(board,3)
    print(f"Column 3 valid: {valid}")

    print("\nFilling up column 3:")
    dropPieces(board, 3, 1)
    dropPieces(board, 3, 2)
    dropPieces(board, 3, 1)
    dropPieces(board, 3, 2)

    printBoard(board)

    valid = isValidMove(board, 3)
    print(f"Column 3 valid after filling: {valid}")

    print("\n Testing the Horizontal function")
    #creating a board with horizontal pieces
    horizontalTestBoard=createBoard()
    dropPieces(horizontalTestBoard, 0, 1)
    dropPieces(horizontalTestBoard, 1, 1)
    dropPieces(horizontalTestBoard, 2, 1)
    dropPieces(horizontalTestBoard, 3, 1)
    printBoard(horizontalTestBoard)
    
    horizontalWin = checkHorizontal(horizontalTestBoard, 5, 2, 1)
    print(f"Horizontal win detected: {horizontalWin}")

    print(f"Check from leftmost piece (5,0): {checkHorizontal(horizontalTestBoard, 5, 0, 1)}")
    print(f"Check from rightmost piece (5,3): {checkHorizontal(horizontalTestBoard, 5, 3, 1)}")
    print(f"Check with wrong piece (player 2): {checkHorizontal(horizontalTestBoard, 5, 0, 2)}")

    # Test no horizontal win (only 3 pieces)
    test_board2 = createBoard()
    dropPieces(test_board2, 0, 1)
    dropPieces(test_board2, 1, 1)
    dropPieces(test_board2, 2, 1)
    
    print(f"Only 3 in a row (should be False): {checkHorizontal(test_board2, 5, 1, 1)}")
    
    print("\nTesting Positive Diagonal Win (/):")
    diagonalPosTestBoard = createBoard()

    dropPieces(diagonalPosTestBoard, 0, 1)  
    dropPieces(diagonalPosTestBoard, 1, 2)
    dropPieces(diagonalPosTestBoard, 1, 1)
    dropPieces(diagonalPosTestBoard, 2, 2)
    dropPieces(diagonalPosTestBoard, 2, 2)
    dropPieces(diagonalPosTestBoard, 2, 1)
    dropPieces(diagonalPosTestBoard, 3, 2)
    dropPieces(diagonalPosTestBoard, 3, 2)
    dropPieces(diagonalPosTestBoard, 3, 2)
    dropPieces(diagonalPosTestBoard, 3, 1)
    printBoard(diagonalPosTestBoard)
    print(f"Positive diagonal win: {checkPositiveDiagonal(diagonalPosTestBoard,3,2,1)}")
    
    print("\nTesting Negative Diagonal Win (\\):")
    diagonalNegTestBoard = createBoard()
    dropPieces(diagonalNegTestBoard, 3, 1)  # Top left of diagonal
    dropPieces(diagonalNegTestBoard, 2, 2)
    dropPieces(diagonalNegTestBoard, 2, 1)
    dropPieces(diagonalNegTestBoard, 1, 2)
    dropPieces(diagonalNegTestBoard, 1, 2)
    dropPieces(diagonalNegTestBoard, 1, 1)
    dropPieces(diagonalNegTestBoard, 0, 2)
    dropPieces(diagonalNegTestBoard, 0, 2)
    dropPieces(diagonalNegTestBoard, 0, 2)
    dropPieces(diagonalNegTestBoard, 0, 1)
    printBoard(diagonalNegTestBoard)
    print(f"Negative diagonal win: {checkNegativeDiagonal(diagonalNegTestBoard, 3, 1, 1)}")

    