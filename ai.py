import tableClass
import random,math, copy
from game import players

def ai_step(table):
    best_score = -math.inf
    best_move = None
    for x, row in enumerate(table.table, start=1):
        for y, chess in enumerate(row, start=1):
            if chess.owner != '*':
                continue
            print(f'AI: Start search {x} {y}')
            new_table = copy.deepcopy(table)
            new_table.put_chess(x, y, players['ai'])
            score = min_max(new_table, 0, False, x, y)
            print(score, x, y)
            if score > best_score:
                best_move = (x, y)
                best_score = score
    
    return best_move[0], best_move[1]


def min_max(table, depth, is_ai, x, y):
    score = {
        players['human']: -1,
        players['ai']: 1.1,
        'tie': 0
    }
    result = table.check_winner(x, y)
    if result:
        return score[result]
    
    if is_ai:
        best_score = -math.inf
        for x, row in enumerate(table.table, start=1):
            for y, chess in enumerate(row, start=1):
                if str(chess) != '*':
                    continue
                new_table = copy.deepcopy(table)
                new_table.put_chess(x, y, players['ai'])
                score = min_max(new_table, depth + 1, False, x, y)
                best_score = max(score, best_score)

        return best_score
    else:
        best_score = math.inf
        for x, row in enumerate(table.table, start=1):
            for y, chess in enumerate(row,start=1):
                if str(chess) != '*':
                    continue
                new_table = copy.deepcopy(table)
                new_table.put_chess(x, y, players['human'])
                score = min_max(new_table, depth + 1, True, x, y)
                best_score = min(score, best_score)

        return best_score
