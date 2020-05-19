import random

board=[[1,2,3],[4,5,6],[7,8,9]]
RandomNumberList=random.sample(range(1, 10), 9)
FreeSquareList=[]
Xcount =0
Ocount=0
GameXStatus=[]
GameOStatus=[]
tempcomparion=0
global StatusGame
PlayAgain=""



def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    print("+-------+-------+-------+")      
    for i in range(3):
        print("|       |       |       |")
        print("|",end="")
        for j in range(3):
            print("  ",board[i][j], "  |",end="")
        print("")
        print("|       |       |       |")
        print("+-------+-------+-------+")
    return board   

def EnterMove(board):
    global Ocount
    GetFreeList=MakeListOfFreeFields(board)
    print("It's Your Turn, Check Available Fields", GetFreeList)
    TakeInputFromUser=input("Please Enter A Number From The Above Available Fields ")
    while TakeInputFromUser.isdigit()!=True:
        print("It's Your Turn, Check Available Fields", GetFreeList)
        TakeInputFromUser=input("Please Enter A Number From The Above Available Fields ")
    else:
        TakeInputFromUser = int(TakeInputFromUser)
    while TakeInputFromUser not in GetFreeList:
        print("Check Available Fields are", GetFreeList)
        TakeInputFromUser=int(input("Please Enter A Number From The Above Available Fields Only "))
    for i in range(3):
            for j in range(3):
                if board[i][j]==TakeInputFromUser:
                    board[i][j]="O"
 #                   tup= (i,j)
#                    GameOStatus.append(tup)
                    break
        
    DisplayBoard(board)
    StatusOfTheGame=VictoryFor(board, "O")
  #  print(StatusOfTheGame)
    if StatusOfTheGame=="O":
        print("you have the won Game")
        return board
    elif StatusOfTheGame==True:
        DrawMove(board)
    else:
        print("thank you")
    
        
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    FreeSquareList.clear()
    for i in range(3):
        for j in range(3):
            if board[i][j]!="X" and board[i][j]!="O":
                FreeSquareList.append(board[i][j])
    return FreeSquareList

def VictoryFor(board, sign):
 #   print("printing sign",sign)
    if board[0][0]==board[0][1]==board[0][2]==sign:
        print(sign," has won the game")
        return sign
    elif board[1][0]==board[1][1]==board[1][2]==sign:
        print(sign," has won the game")
        return sign
    elif board[2][0]==board[2][1]==board[2][2]==sign:
        print(sign," has won the game")
        return sign
    elif board[0][0]==board[1][0]==board[2][0]==sign:
        print(sign," has won the game")
        return sign
    elif board[0][1]==board[1][1]==board[2][1]==sign:
        print(sign," has won the game")
        return sign
    elif board[0][2]==board[1][2]==board[2][2]==sign:
        print(sign," has won the game")
        return sign
    elif board[0][0]==board[1][1]==board[2][2]==sign:
        print(sign," has won the game")
        return sign
    elif board[0][2]==board[1][1]==board[2][0]==sign:
        print(sign," has won the game")
        return sign
    elif len(MakeListOfFreeFields(board))>=1:
        return True
    else:    
        print("game is tie")
        
    
        
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove(board):
    global StatusOfTheGame
    global tempcomparion
    FreeSquareList=MakeListOfFreeFields(board)
#    print(RandomNumberList)
#    print(FreeSquareList)
#    print("RandomNumberList item checking in FreeSquareList")
    for item in RandomNumberList:
        if item in FreeSquareList:
#            print(item,"item is found in FreesqaureList, which means you can insert here",FreeSquareList)
            tempcomparion= item
            FreeSquareList.remove(item)
    #        print(FreeSquareList)
            break
    for i in range(3):
        for j in range(3):
            if board[i][j]==tempcomparion:
                board[i][j]="X"
 #               tup= (i,j)
 #               GameXStatus.append(tup)
                break
    
    DisplayBoard(board)
 #   print("length of GameXStatus here",len(GameXStatus))
    StatusOfTheGame=VictoryFor(board, "X")
  #  print(StatusOfTheGame)
    if StatusOfTheGame=="X":
        print("Computer won the won Game")
        return board
    elif StatusOfTheGame==True:
        EnterMove(board)
    else:
        print("Thank you")
    
    #
                                # the function draws the computer's move and updates the board
                                #
while True:
    board=DrawMove(board)
    PlayAgain=input("do you wish play again, y to continue and any other key to exit")
    if PlayAgain.upper()=="Y":
        board=[[1,2,3],[4,5,6],[7,8,9]]
        RandomNumberList=random.sample(range(1, 10), 9)
    else:
        print("Bye!")
        break
