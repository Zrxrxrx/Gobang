from game import Game, players
import ai

size = 4

if __name__ == "__main__":
    g = Game(players['human'], size=3)

    while not g.end:
        if g.current_player == players['human']:
            print('Human turn')
            success_put_chess = False
            while not success_put_chess:
                input_str = input('input(x,y): ')
                x, y = map(int, input_str.split(' '))
                success_put_chess = g.put_chess(x, y)
        else:
            print('AI turn')
            x, y = ai.ai_step(g.table)
            d = g.put_chess(x, y)
            if d == False:
                print(x, y)
                print('AI error')
                break
        
        print(str(g.table))
        
        winner = g.table.check_winner(x, y)
        if winner:
            g.end = True
            if winner == 'tie':
                print('Tie')
            else:
                print(f'winner is {winner}')
            
