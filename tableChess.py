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
        print(f'put chess: {r}')
        return r

    def get_chess(self, x, y):
        x -= 1
        y -= 1
        return self.table[x][y]

    def check_winner(self, x, y):
        chess = self.table[x-1][y-1]
        x -= 1
        y -= 1
        r1 = chess.check_neighbor(self, self.check_size, x, y, 1, 0)
        r2 = chess.check_neighbor(self, self.check_size, x, y, -1, 0)
        r3 = chess.check_neighbor(self, self.check_size, x, y, 0, 1)
        r4 = chess.check_neighbor(self, self.check_size, x, y, 0, -1)
        r5 = chess.check_neighbor(self, self.check_size, x, y, 1, -1)
        r6 = chess.check_neighbor(self, self.check_size, x, y, 1, 1)
        r7 = chess.check_neighbor(self, self.check_size, x, y, -1, 1)
        r8 = chess.check_neighbor(self, self.check_size, x, y, -1, -1)
        if r1 or r2 or r3 or r4 or r5 or r5 or r6 or r7 or r8:
            self.winner = chess.owner
            return chess.owner
        else:
            return None


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

        if check_size == 1:
            return True

        if temp_x < 0 or temp_y < 0 or temp_x >= table.size or temp_y >= table.size:
            # print('out')
            return False

        if table.table[temp_x][temp_y].owner != self.owner:
            # print('not same')
            return False
        
        return self.check_neighbor(table, check_size-1, temp_x, temp_y, offset_x, offset_y)
        
