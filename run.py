from game import Game
import ai

size = 3

if __name__ == "__main__":
    g = Game(size)
    g.print_2D_table()

    while True:
        if g.player == 1:
            success_put = False
            while not success_put:
                input_str = input('input (x y): ')
                x, y = list(map(int, input_str.split(' ')))
                success_put = g.chess(x, y)
            g.print_2D_table()
        else:
            print('ai step')
            x, y = ai.ai_step(g.tableTree)
            print(x , ' ' , y)
            s = g.chess(x, y)
            if not s:
                print('error')
                break
            g.print_2D_table()