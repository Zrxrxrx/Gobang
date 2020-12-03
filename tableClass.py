class chess:
    xy = None
    Next = None
    rate = 0
    def __init__(self,xy,Next=[]):
        self.xy=xy
        self.Next=Next[:]
    def isIN(self,xy):
        return xy in self.Next
    def add(self,c):
        self.Next = []
        self.Next.append(c)
    @staticmethod
    def copy(root):
        newc = chess(root.xy)
        for temp in root.Next:
            newtemp = chess.copy(temp)
            newc.Next.append(newtemp)
        return newc

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
            self.currentChess.add(n)
            self.currentChess = n
    def getArray(self):
        tableMap = [0 for i in range(self.size*self.size)]
        i = 1
        c = self.firstChess
        if(c==None):
            return tableMap
        while(c.xy!=None):
            tableMap[c.xy] = 1 if i%2==1 else 2
            if(len(c.Next)>0):
                c = c.Next[0]
            else:
                c = chess(None)
            
            i+=1
        return tableMap