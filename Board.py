# Initalizes the game Board
def createBoard():
    row, column = 6,7
    board = [[0 for j in range(column)] for i in range(row)]
    return board
    


def dropPieces(board, column,piece):
    currentRow=5
    while currentRow >=0:
        if board[currentRow][column]==0:
            board[currentRow][column]=piece
            return True
        else:
            currentRow=currentRow-1
    return False

def isValidMove(board, column):
    topRow=0
    if board[topRow][column]!=0:
        return False
    return True

def checkHorizontal(board,row,col,piece):
    count=1
    #check for piece on the right
    currentCol=col+1
    while currentCol<7 and board[row][currentCol]==piece:
        count+=1
        currentCol+=1

    #check for pieces on the left
    currentCol=col-1
    while currentCol>=0 and board[row][currentCol]==piece:
        count+=1
        currentCol-=1
    if count >=4:
        return True
    return False

def checkVertical(board,row,col,piece):
    count=1
    currentRow=row+1
    while currentRow<=5 and board[currentRow][col]==piece:
        count+=1
        currentRow+=1

    if count >=4:
        return True
    return False

def checkPositiveDiagonal(board,row,col,piece):
    count=1
    #check for upwards and right
    currentRow=row-1
    currentCol=col+1

    while currentRow>=0 and currentCol<7 and board[currentRow][currentCol]==piece:
        count+=1
        currentRow-=1
        currentCol+=1

    #check for downwards and left
    currentRow=row+1
    currentCol=col-1
    while currentRow<=5 and currentCol>=0 and board[currentRow][currentCol]==piece:
        count+=1
        currentRow+=1
        currentCol-=1

    if count >=4:
        return True
    return False

def checkNegativeDiagonal(board,row,col,piece):
    count=1
    #check for downward and right
    currentRow=row+1
    currentCol=col+1

    while currentRow<=5  and currentCol<7 and board[currentRow][currentCol]==piece:
        count+=1
        currentRow+=1
        currentCol-=1

    #check for upwards and left
    currentRow=row-1
    currentCol=col-1

    while currentRow>=0 and currentCol>=0 and board[currentRow][currentCol]==piece:
        count+=1
        currentRow-=1
        currentCol-=1
    
    if count >=4:
        return True
    return False


if __name__=="__main__":
    board=createBoard()
    print("Board Created")
    for row in board:
        print (row)

    print("\n Dropping piece 1 in coulmn 3:")
    success=dropPieces(board,3,1)
    for row in board:
        print(row)

    print("\n Dropping piece 2 in coulmn 3:")
    success=dropPieces(board,3,2)
    for row in board:
        print(row)

    print("\n Checking for valid Moves:")
    valid=isValidMove(board,3)
    print(f"Column 3 valid: {valid}")

    print("\nFilling up column 3:")
    dropPieces(board, 3, 1)
    dropPieces(board, 3, 2)
    dropPieces(board, 3, 1)
    dropPieces(board, 3, 2)

    for row in board:
        print(row)

    valid = isValidMove(board, 3)
    print(f"Column 3 valid after filling: {valid}")