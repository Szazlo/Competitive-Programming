board = dict()
OFFSET = 1000000
def main():
    count = int(input())

    lastTurn = "x"
    maxX = 0
    maxY = 0
    minX = OFFSET*2
    minY = OFFSET*2


    for i in range(count):
        color, x, y  = map(str, input().split())
        x = int(x)
        y = int(y)
        x+=OFFSET
        y+=OFFSET
        if(x > maxX):  
            maxX = x
        if(y > maxY):  
            maxY = y
        if(y<minY):
            minY = y
        if(x<minX):
            minX = x
        if(x not in board):
            board[x] = dict()
        if(y not in board[x]):
            board[x][y] = "x"
        board[x][y] = color
        lastTurn = color
    nowTurn = "x"
    if(lastTurn == "W"):
        nowTurn = "B"
    else:
        nowTurn = "W"
    for xcord in range(minX,maxX):
        for ycord in range(minY,maxY):
            # print("checking x:"+str(xcord-OFFSET) +" Y:"+str(ycord-OFFSET))
            if(xcord not in board):
                xcord+=1
                continue
            if(ycord not in board[xcord]):
                ycord+=1
                continue
            if(board[xcord][ycord] != nowTurn):
                ycord+=1
                continue
            result = Search(xcord,ycord)
            if result != 0:
                print(str(result[0]) +" "+str(result[1]))
                return
    print(0)

def GetAtBoardLoc(x,y):
    if(x not in board):  
        return "x"
    if(y not in board[x]):
        return "x"
    return board[x][y]

def Search(x,y):
    for xdir in range(-1,2):
        for ydir in range(-1,2):
            if(ydir != 0 and xdir != 0):
                result = SearchInDir(x,y,xdir,ydir)
                if(result != 0):
                   return result
    return 0

def SearchInDir(x,y,xdir,ydir):
    targetColor = board[x][y]
    fail = "none"
    for i in range(6):
        # print(str(i) + "checking line at:"+str(x+xdir*i-OFFSET) +" Y:"+str(y+ydir*i-OFFSET))
           
        colorAtLoc = GetAtBoardLoc(x+xdir*i,y+ydir*i)
        if(colorAtLoc != targetColor):
            if(colorAtLoc == "x"):
                # print("failed")
                if fail == "none":
                    fail = [(x+xdir*i) - OFFSET,(y+ydir*i)- OFFSET]
                else:
                    return 0
            else:
                return 0

    return fail

main()