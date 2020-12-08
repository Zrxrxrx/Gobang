from config import size, Ai_max_depth
import math
import copy

class Node():

    def __init__(self, x, y, table, node_type, depth):
        self.x = x
        self.y = y
        self.node_type = node_type
        self.depth = depth
        self.table = copy.deepcopy(table)
    
    def get_score(self, depth):
        if depth >= Ai_max_depth:
            return 0

        if self.node_type == 'max':
            best_score = -math.inf
            pass # TODO
            return best_score
        elif self.node_type == 'min':
            best_score = math.inf
            pass # TODO
            return best_score
        else:
            raise ValueError('Bad node type')
        