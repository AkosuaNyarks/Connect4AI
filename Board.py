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

def checkWinner(board,piece):
    for row in range(6):
        for col in range(7):
            if board[row][col]==piece:
                if checkWin(board,row,col,piece):
                    return True
    return False

def miniMax(board,depth,maximizingPlayer,alpha,beta):
   #-Draw
    if len(getValidColumns(board))==0:
       return 0
     #-depth
    if depth ==0:
       return evaluationPosition(board,2)
    
    if maximizingPlayer:
        maxScore=-float("inf")
        for col in getValidColumns(board):
            row=dropPieces(board,col,2)
            if checkWin(board,row,col,2):
                board[row][col] = 0 
                return 100
            
            score=miniMax(board,depth-1,False,alpha,beta)
            board[row][col]=0
            maxScore=max(maxScore,score)

            alpha=max(alpha,maxScore)
            if alpha >=beta:
                break
        return maxScore
    
    else:
        minScore = float('inf')
        for col in getValidColumns(board):
            row = dropPieces(board, col, 1)

            if checkWin(board,row,col,1):
                board[row][col] = 0 
                return -100
            score = miniMax(board, depth - 1, True,alpha,beta)
            board[row][col] = 0
            minScore = min(minScore, score)

            beta=min(beta,minScore)
            if alpha>=beta:
                break
        return minScore
    
def getBestMove(board,depth):
    validColumns=getValidColumns(board)
    bestScore=-float("inf")
    bestCol=validColumns[0]

    alpha=-float("inf")
    beta=float("inf")

    for col in validColumns:
        row=dropPieces(board,col,2)
        if checkWin(board,row,col,2):
            board[row][col]=0
            return col
        score=miniMax(board,depth-1,False,alpha,beta)
        board[row][col]=0
        if score>bestScore:
            bestScore=score
            bestCol=col
        alpha=max(alpha,bestScore)
    return bestCol


def evaluationConditions(section,piece):
    score=0
    opponentPiece = 1 if piece == 2 else 2
    
    aiPieceCount=section.count(piece)
    emptySlotCount=section.count(0)
    opponentPieceCount=section.count(opponentPiece)

    if aiPieceCount==4:
        score+=100
    elif aiPieceCount==3 and emptySlotCount==1:
        score+=50
    elif aiPieceCount==2 and emptySlotCount==2:
        score=score+10
    
    if opponentPieceCount==3 and emptySlotCount==1:
        score-=40
    elif opponentPieceCount==2 and emptySlotCount==2:
        score-=8
    return score



def evaluationPosition(board, piece):
    score=0
    #check for horizontal sections
    for row in range(0,6):
        for col in range(0,4):
            section=[board[row][col],board[row][col+1],board[row][col+2],board[row][col+3]]
            score=score+evaluationConditions(section,piece)
    #check for vertical section
    for col in range(7):
        for row in range(3):
            section=[board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]]
            score = score + evaluationConditions(section, piece)
    #positive diagonals
    for row in range(3,6):
        for col in range(0,4):
            section= [board[row][col], board[row-1][col+1], board[row-2][col+2], board[row-3][col+3]]
            score += evaluationConditions(section, piece)
    #negative diagonals
    for row in range(0,3): 
        for col in range(0,4):  
            section = [board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]]
            score += evaluationConditions(section, piece)


    return score


   
   


