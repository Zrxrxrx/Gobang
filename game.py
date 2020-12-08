from tableChess import Table

players = {
    'human': 'O',
    'ai': 'X'
}

class Game():
    table = None
    mapsize = 0
    current_player = players['human']
    end = False
    def __init__(self, player, size=10):
        size = int(size)
        self.mapsize = size
        self.table = Table(size)
        self.current_player = player

    def put_chess(self, x, y):
        if self.current_player == players['human']:
            if self.table.put_chess(x, y, players['human']):
                self.current_player = players['ai']
                return True
        else:
            if self.table.put_chess(x, y, players['ai']):
                self.current_player = players['human']
                return True
        
        return False



