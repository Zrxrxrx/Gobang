import tableClass
import random
def chessOne(t):
    copy = tableClass.chess.copy(t.firstChess)
    #a = copy
    x = random.randint(1,t.size)
    y = random.randint(1,t.size)
    while(t.getArray()[(x-1)*t.size+y-1]!=0):
        x = random.randint(1,t.size)
        y = random.randint(1,t.size)
    createTree(copy,t.size,3)
    return [x,y]
def createTree(tree,size,limit):
    current = tree
    xys = []
    while(current!=None):
        xys.append(current.xy)
        if(len(current.Next)>0):
            current = current.Next[0]
        else:
            treeGroud(current,xys,limit,size*size)
            current = None
def treeGroud(root,already,limit,size):
    if(limit==0):
        return
    for i in range(0,size-1):
        if(i not in already):
            newAlready = already[:]
            newAlready.append(i)
            nextChess = tableClass.chess(i)
            root.Next.append(nextChess)
            treeGroud(nextChess,newAlready,limit-1,size)
        pass
