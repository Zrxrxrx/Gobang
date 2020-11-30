class chess():
    x = None
    y = None
    table = None

    def __init__(self, table, x, y):
        self.x = x
        self.y = y
        self.table = table
    def getKey(self,x,y):
        return (x-1)*self.mapsize+y-1
    def getPlayer(self):
        return self.table[self.getKey(self.x,self.y)]
    def getDirect(self,x,y):
        return self.table[self.getKey(self.x+x,self.y+y)]
    def getDirectChess(self,x,y):
        return chess(self.table,self.x+x,self.y+y)

class treeMap():
    def __init__(self,x,y):
        