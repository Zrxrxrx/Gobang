class Table():
    table = []
    size = 0
    check_size = 3
    winner = None
    
    def __init__(self, size=10):
        self.table = []
        self.size = size
        for row in range(size):
            temp_row = []
            for col in range(size):
                temp_row.append(Chess())
            self.table.append(temp_row)
            

    def __str__(self):
        string = ''
        for row in self.table:
            for col in row:
                string += f'{col}\t'
            string += '\n'
        return string[:-1]
    
    def put_chess(self, x, y, player):
        x -= 1
        y -= 1
        r = self.table[x][y].put(player)
        # print(f'put chess: {r}')
        return r

    def get_chess(self, x, y):
        x -= 1
        y -= 1
        return self.table[x][y]

    def change_chess(self, x, y, string):
        self.table[x][y] = string


    def check_winner(self, x, y):
        tie = True
        for row in self.table:
            for chess in row:
                if chess.owner == '*':
                    tie = False
        

        chess = self.table[x-1][y-1]
        x -= 1
        y -= 1
        r1 = chess.check_neighbor(self, chess.check_neighbor(self, self.check_size, x, y, -1, 0), x, y, 1, 0)
        r3 = chess.check_neighbor(self, chess.check_neighbor(self, self.check_size, x, y, 0, -1), x, y, 0, 1)
        r5 = chess.check_neighbor(self, chess.check_neighbor(self, self.check_size, x, y, -1, 1), x, y, 1, -1)
        r6 = chess.check_neighbor(self, chess.check_neighbor(self, self.check_size, x, y, -1, -1), x, y, 1, 1)
        if r1==1 or r3==1 or  r5==1 or  r6==1:
            self.winner = chess.owner
            return chess.owner
        else:
            if tie:
                return 'tie'
            return None
    
    def available_points(self):
        result = []
        for x, row in enumerate(self.table):
            for y, chess in enumerate(row):
                if chess.owner != '*':
                    result.append((x, y))
        return result
    def getArray(self):
        result = []
        for x, row in enumerate(self.table):
            for y, chess in enumerate(row):
                if(chess.owner=='*'):
                    result.append(0)
                if(chess.owner=='O'):
                    result.append(1)
                if(chess.owner=='X'):
                    result.append(2)
        return result


class Chess():
    owner = '*'

    def __init__(self, player='*'):
        self.owner = player

    def __str__(self):
        return str(self.owner)

    def put(self, player):
        if self.owner != '*':
            return False
        else:
            self.owner = player
            return True

    def check_neighbor(self, table, check_size, x, y, offset_x, offset_y):
        temp_x = x + offset_x
        temp_y = y + offset_y
        # print(f'x={temp_x:2} y={temp_y:2} {check_size}')

        if temp_x < 0 or temp_y < 0 or temp_x >= table.size or temp_y >= table.size:
            # print('out')
            return check_size

        if table.table[temp_x][temp_y].owner == self.owner:
            # print('not same')
            return self.check_neighbor(table, check_size-1, temp_x, temp_y, offset_x, offset_y)
        else:
            return check_size
        
        
