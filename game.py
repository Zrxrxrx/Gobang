import tableClass
class Game():
    tableMap = []
    mapsize = 0
    player = 1
    tableTree = None
    def __init__(self,size=10):
        size = int(size)
        self.tableMap = [0 for i in range(size*size)]
        self.mapsize = size
        self.tableTree = tableClass.table(size)
    def printRawTable(self):
        for target_list in self.tableMap:
            print(target_list)
            pass
    def getRawTable(self):
        return self.tableMap

    def print_2D_table(self):
        print('=' * 30)
        for i, chess in enumerate(self.tableMap, start=1):
            print(chess, end='\t')
            if i % self.mapsize == 0:
                print('\n', end='')

    def chess(self,x,y):
        if(self.getPlayer(x,y)!=0):
            return False
        self.tableTree.chess(x,y)
        self.tableMap = self.tableTree.getArray()
        #self.tableMap[(x-1)*self.mapsize+y-1] = self.player
        if(self.player==1):
            self.player=2
        else:
            self.player=1
        return True
    #get which players current x,y
    #return 0,1,2
    def getPlayer(self,x,y):
        if(x>0 and x<=self.mapsize and y>0 and y<=self.mapsize):
            return self.tableMap[(x-1)*self.mapsize+y-1]
        else:
            return -1
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

#g = game()
# g.chess(1,1,1)
# g.chess(1,2,1)
# g.chess(1,3,1)
# g.chess(1,4,1)
# g.chess(1,5,1)
# print(g.getRawTable())
