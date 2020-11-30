class chess:
    xy = None
    player = None
    Next = None
    def __init__(self,xy,player):
        self.xy=xy
        self.player=player

class table:
    size = None
    firstChess = None
    currentChess = None
    def __init__(self,size):
        self.size=size
    def chess(self,x,y,p):
        if(self.currentChess==None):
            self.currentChess = chess((x-1)*self.size+y-1,p)
            self.firstChess = self.currentChess
        else:
            n = chess((x-1)*self.size+y-1,p)
            self.currentChess.Next = n
            self.currentChess = n
    def getArray(self):
        tableMap = [0 for i in range(self.size*self.size)]
        c = self.firstChess
        while(c!=None):
            tableMap[c.xy] = c.player
            c = c.Next
        return tableMap