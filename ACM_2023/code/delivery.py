
carPos = [0,0]
locs = dict()
size = 0
def main():
    goingBack = False
    size = int(input())
    O = int(input())
    for i in range(O):
        x,y,price = map(int, input().split())
        if(x not in locs):
            locs[x] = dict()
        if(y not in locs[x]):
            locs[x][y] = price
    orderValue = 0
    while True:
        print(carPos)
        missingoutY = tallyVertical(goingBack)
        missingoutX = tallyHorizontal(goingBack)
        dir = 1
        if(goingBack):
            dir = -1
        if(missingoutX == -1 and missingoutY == -1):
            print("at end")
            if(goingBack):
                print(orderValue)
                return
            else:
                goingBack = True
                continue
        if(missingoutX > missingoutY):
            carPos[0]+=dir
        else:
            carPos[1]+=dir
        
        
        
def tallyVertical(goingBack):
    total = 0
    if(goingBack):
        if(carPos[1] == 0):
            return -1
        for i in range(carPos[1],size):
            total += GetAtBoardLoc(carPos[0],i)
    else:
        print(carPos[1])
        if(carPos[1] == size):
            return -1
        for i in range(size,carPos[1],-1):
            total += GetAtBoardLoc(carPos[0],i)
    return total

def tallyHorizontal(goingBack):
    total = 0

    if(goingBack):
        if(carPos[0] == 0):
            return -1
        for i in range(carPos[0],size):
            total += GetAtBoardLoc(i,carPos[1])
    else:
        if(carPos[0] == size):
            return -1
        for i in range(size,carPos[0],-1):
            total += GetAtBoardLoc(i,carPos[1])
    return total

def GetAtBoardLoc(x,y):
    if(x not in locs):  
        return 0
    if(y not in locs[x]):
        return 0
    return locs[x][y]

main()