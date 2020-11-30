class chess:
    xy = None
    Next = []
    def __init__(self,xy):
        self.xy=xy
    def isIN(self,xy):
        return xy in self.Next
    def insert(self,c):
        self.Next.append(c)

class table:
    size = None
    firstChess = None
    currentChess = None
    def __init__(self,size):
        self.size=size
    def chess(self,x,y):
        if(self.currentChess==None):
            self.currentChess = chess((x-1)*self.size+y-1)
            self.firstChess = self.currentChess
        else:
            n = chess((x-1)*self.size+y-1)
            self.currentChess.insert(n)
            self.currentChess = n
    def getArray(self):
        tableMap = [0 for i in range(self.size*self.size)]
        i = 1
        c = self.firstChess
        while(c!=None):
            tableMap[c.xy] = 1 if i%2==1 else 2
            c = c.Next[0] if len(c.Next)>0 else None
            i+=1
        return tableMap