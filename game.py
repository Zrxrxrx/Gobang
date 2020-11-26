class game():
    tableMap = []
    mapsize = 0
    def __init__(self,size=10):
        self.tableMap = [0 for i in range(size*size)]
        self.mapsize = size
    #get which players current x,y
    #return 0,1,2
    def printRawTable(self):
        print("target_list")
        for target_list in self.tableMap:
            print(target_list)
            pass
    def printTable()

g = game(size=20)
g.printTable()
