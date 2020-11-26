class game():
    tableMap = []
    mapsize = 0
    def __init__(self,size=10):
        self.tableMap = [0 for i in range(size*size)]
        self.mapsize = size
    def printRawTable(self):
        for target_list in self.tableMap:
            print(target_list)
            pass
    def getRawTable(self):
        return self.tableMap
    def placeChest(self,x,y,player):
        self.tableMap[(x-1)*self.mapsize+y] = player
        print(self.checkWin(x,y))
    #get which players current x,y
    #return 0,1,2
    def getPlayer(self,x,y):
        if(x>0 and x<=self.mapsize and y>0 and y<=self.mapsize):
            return self.tableMap[(x-1)*self.mapsize+y]
        else:
            return -1
            pass
    def checkWin(self,x,y):
        if(self.check(x,y,1,0,self.check(x,y,-1,0,1))>=5 or self.check(x,y,0,1,self.check(x,y,0,-1,1))>=5 or self.check(x,y,1,1,self.check(x,y,-1,-1,1))>=5 or self.check(x,y,-1,1,self.check(x,y,1,-1,1))>=5):
            return True
        else:
            return False
        
    def check(self,x,y,ax,ay,count):
        if(self.getPlayer(x,y)==self.getPlayer(x+ax,y+ay)):
            return self.check(x+ax,y+ay,ax,ay,count+1)
        else:
            return count

g = game(size=20)
g.placeChest(1,1,1)
g.placeChest(1,2,1)
g.placeChest(1,3,1)
g.placeChest(1,4,1)
g.placeChest(1,5,1)
print(g.getRawTable())
