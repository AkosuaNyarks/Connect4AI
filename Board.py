# Initalizes the game Board
import random


def createBoard():
    row, column = 6,7
    board = [[0 for j in range(column)] for i in range(row)]
    return board
    


def dropPieces(board, column,piece):
    currentRow=5
    while currentRow >=0:
        if board[currentRow][column]==0:
            board[currentRow][column]=piece
            return currentRow
        else:
            currentRow=currentRow-1
    return None

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
        currentCol+=1

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

def checkWin(board,row,col,piece):
    if checkNegativeDiagonal(board,row,col,piece) or checkHorizontal(board,row,col,piece) or checkPositiveDiagonal(board,row,col,piece) or checkVertical(board,row,col,piece):
        return True
    return False

def getValidColumns(board):
    validColumns=[]
    for cols in range(7):
        if isValidMove(board,cols):
            validColumns.append(cols)
    return validColumns

def printBoard(board):
    print("0 1 2 3 4 5 6")
    for row in board:
        print(row)

def randomMoves(board):
    validColumns=getValidColumns(board)
    randomCol=random.choice(validColumns)
    return randomCol

def Minimax(board,depth,AI):
   #Bases Cases
   #-Draw
   if len(getValidColumns(board))==0:
       return 0
   
   #-depth
   if depth ==0:
       return 0
   
   


