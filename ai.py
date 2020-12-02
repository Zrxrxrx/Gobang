import tableClass
import random,math
def chessOne(t):
    copy = tableClass.chess.copy(t.firstChess)
    #a = copy
    x = random.randint(1,t.size)
    y = random.randint(1,t.size)
    while(t.getArray()[(x-1)*t.size+y-1]!=0):
        x = random.randint(1,t.size)
        y = random.randint(1,t.size)
    pre = createTree(copy,t.size,3)
    if(pre!=None):
        print("ai on")
        return pre
    print("random")
    return [x,y]
def createTree(tree,size,limit):
    current = tree
    root = tree
    xys = []
    while(current!=None):
        xys.append(current.xy)
        if(len(current.Next)>0):
            current = current.Next[0]
            root = current
        else:
            treeGroud(current,xys,limit,size*size)
            current = None
    Max = 0
    cur = None
    for v in root.Next:
        if(len(xys)%2==1 and v.rate<Max):
            cur = v
            Max = v.rate
        if(len(xys)%2==0 and v.rate>Max):
            cur = v
            Max = v.rate
    x = random.randint(1,size)
    y = random.randint(1,size)
    if(cur!=None):
        y = (cur.xy+1)%size
        x = math.ceil((cur.xy+1)/size)
        return [x,y]
    return None
def treeGroud(root,already,limit,size):
    if(limit==0):
        return 0
    for i in range(0,size):
        if(i not in already):
            newAlready = already[:]
            newAlready.append(i)
            nextChess = tableClass.chess(i)
            root.Next.append(nextChess)
            if(checkWin(already,i,size,3)):
                nextChess.rate += 1 if len(already)%2==1 else -1
            else:
                treeGroud(nextChess,newAlready,limit-1,size)
            for sonChess in nextChess.Next:
                nextChess.rate +=sonChess.rate

def checkWin(xys,xy,size,TO):
    table = [0 for a in range(size)]
    current = 1 if len(xys)%2==1 else 2
    k =1
    for v in xys:
        if(current==k):
            table[v] = 1
            pass
        k = 1 if k==2 else 2
    table[xy] = 1
    y = (xy+1)%size
    x = math.ceil((xy+1)/size)
    if(check(x,y,1,0,check(x,y,-1,0,1,table),table)>=TO or check(x,y,0,1,check(x,y,0,-1,1,table),table)>=TO or check(x,y,1,1,check(x,y,-1,-1,1,table),table)>=TO or check(x,y,-1,1,check(x,y,1,-1,1,table),table)>=TO):
        return True
    else:
        return False
def check(x,y,ax,ay,count,table):
    if(getPlayer(x,y,table)==getPlayer(x+ax,y+ay,table)):
        return check(x+ax,y+ay,ax,ay,count+1,table)
    else:
        return count
def getPlayer(x,y,table):
    size = int(math.pow(len(table),0.5))
    k = (x-1)*size+y-1
    print(x,y,k)
    if(x>0 and x<=size and y>0 and y<=size):
        return table[k]
    else:
        return 0
