from game import Game, players
import ai

size = 3

if __name__ == "__main__":
    g = Game(size)

    while not g.end:
        if g.current_player == players['human']:
            print('human turn')
            success_put_chess = False
            while not success_put_chess:
                input_str = input('input(x,y): ')
                x, y = map(int, input_str.split(' '))
                success_put_chess = g.put_chess(x, y)
        else:
            print('AI turn')
            x, y = ai.ai_step(g.table)
            g.put_chess(x, y)
        
        print(str(g.table))
        
        winner = g.table.check_winner(x, y) 
        if winner:
            g.end = True
            print(f'winner is {winner}')
            
