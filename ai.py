import tableClass
import random,math
from other import convert_to_1D, convert_to_2D
import copy
from game import players
def chessOne(t):
    #a = copy
    x = random.randint(1,t.size)
    y = random.randint(1,t.size)
    while(t.getArray()[(x-1)*t.size+y-1]!=0):
        x = random.randint(1,t.size)
        y = random.randint(1,t.size)
    
    if(t.firstChess!=None):
        copy = tableClass.chess.copy(t.firstChess)
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
            treeGrow(current,xys,limit,size)
            current = None
    Max = 0
    cur = None
    rates = []
    for v in root.Next:
        temp1 = abs(v.rate)
        if(temp1>Max):#len(xys)%2==1 and 
            cur = v
            Max = temp1
        # if(len(xys)%2==0 and v.rate<Max):
        #     cur = v
        #     Max = v.rate
        rates.append({"xy":v.xy,"rate":v.rate})
    x = random.randint(1,size)
    y = random.randint(1,size)
    if(cur!=None):
        y = (cur.xy)%size+1
        x = math.ceil((cur.xy+1)/size)
        return [x,y,rates]
    return None
def treeGrow(root,already,limit,size):
    if(limit==0):
        return 0
    for i in range(0,size*size):
        if(limit==3):
            print(i)
        if(i not in already):
            newAlready = already[:]
            newAlready.append(i)
            nextChess = tableClass.chess(i)
            root.Next.append(nextChess)
            x = 1
            for xi in range(size*size,size*size-len(already)-1):
                x  = x*xi
            if(checkWin(already,i,size,3)):
                if(len(already)%2==1):
                    nextChess.rate += (1/x)
                else:
                    nextChess.rate -= (1/x)
                    #nextChess.rate += 1/limit
            else:
                treeGrow(nextChess,newAlready,limit-1,size)
            for sonChess in nextChess.Next:
                nextChess.rate +=sonChess.rate

# def select_empty_chess(table):
#     rest = filter(lambda c: c == 0, table)
#     return list(rest)


def ai_step(table):
    best_score = -math.inf
    best_move = None
    # print(select_empty_chess(table.getArray()))
    for x, row in enumerate(table.table, start=1):
        for y, chess in enumerate(row, start=1):
            if chess.owner != '*':
                continue
            print(f'AI: Start search {x} {y}')
            new_table = copy.deepcopy(table)
            # print('%d, %d', x, y)
            new_table.put_chess(x, y, players['ai'])
            score = min_max(new_table, 0, False, x, y)
            print(score, x, y)
            if score > best_score:
                best_move = (x, y)
                best_score = score
    
    return best_move[0], best_move[1]


def min_max(table, depth, is_ai, x, y):
    score = {
        players['human']: -1,
        players['ai']: 1.1,
        'tie': 0
    }
    # print(table)
    # print(depth)
    result = table.check_winner(x, y)
    if result:
        return score[result]
    
    if is_ai:
        best_score = -math.inf
        for x, row in enumerate(table.table, start=1):
            for y, chess in enumerate(row, start=1):
                if str(chess) != '*':
                    continue
                new_table = copy.deepcopy(table)
                new_table.put_chess(x, y, players['ai'])
                score = min_max(new_table, depth + 1, False, x, y)
                best_score = max(score, best_score)

        return best_score
    else:
        best_score = math.inf
        for x, row in enumerate(table.table, start=1):
            for y, chess in enumerate(row,start=1):
                if str(chess) != '*':
                    continue
                new_table = copy.deepcopy(table)
                new_table.put_chess(x, y, players['human'])
                score = min_max(new_table, depth + 1, True, x, y)
                best_score = min(score, best_score)

        return best_score



# def get_win_rate(point, table, depth, is_self):
#     if depth == 0:
#         return 0
    
#     candidate_points = select_empty_chess(table)
    
#     # table is full
#     if not candidate_points:
#         return 0
    
#     # set chess to new table
#     new_table = table.copy()
#     new_table.set_chess(p)

#     if checkWin(new_table) and 

#     for p in candidate_points:
#         new_table = table.copy()
#         new_table.set_chess(p)

#     return 0

def checkWin(xys,xy,size,TO):
    table = [0 for a in range(size*size)]
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
    if(getPlayer(x,y,table)!=0 and getPlayer(x,y,table)==getPlayer(x+ax,y+ay,table)):
        return check(x+ax,y+ay,ax,ay,count+1,table)
    else:
        return count
def getPlayer(x,y,table):
    size = int(math.pow(len(table),0.5))
    k = (x-1)*size+y-1
    if(x>0 and x<=size and y>0 and y<=size):
        return table[k]
    else:
        return 0

def evaluate(table, x, y):
    score = 0
    for row in table.table:
        for chess in row:
            pass


    return score