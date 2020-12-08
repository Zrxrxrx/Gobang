from config import size, Ai_max_depth
from game import players
import math
import copy

class Node():

    def __init__(self, x, y, table, node_type, depth):
        # self.x = x
        # self.y = y
        self.node_type = node_type
        self.depth = depth
        self.table = copy.deepcopy(table)
        self.player = self.node_type_to_player()
        self.table.put_chess(x, y, self.player)
    
    # Min_Max alogthm
    def get_score(self):
        if self.depth >= Ai_max_depth:
            return self.evaluate()

        if self.node_type == 'max':
            best_score = -math.inf
            for x, y in self.table.available_points():
                next_node = Node(x, y, self.table, 'min', self.depth+1)
                tmp_score = next_node.get_score()
                best_score = max(best_score, tmp_score)
            return best_score
        elif self.node_type == 'min':
            best_score = math.inf
            for x, y in self.table.available_points():
                next_node = Node(x, y, self.table, 'max', self.depth+1)
                tmp_score = next_node.get_score()
                best_score = min(best_score, tmp_score)
            return best_score
        else:
            raise ValueError('Bad node type')

    def evaluate(self):
        score = 0

        return score
        
    def node_type_to_player(self):
        if self.node_type == 'max':
            return players['ai']
        elif self.node_type == 'min':
            return players['human']
        else:
            raise ValueError('Bad node type')