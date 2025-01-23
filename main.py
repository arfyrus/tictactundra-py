import re

grid = [' '] * 9
pieces = {'X': 0, 'O': 0}
colours = {'X': '\x1b[1;35m', 'O': '\x1b[1;33m'}
curr = 'X'
GOAL_NUM = 4

def label_grid():
    num = 1
    for i in range(9):
        if not grid[i] == 'X' and not grid[i] == 'O':
            grid[i] = str(num)
            num += 1

def index(x, y):
    return x + y * 3

def winner():
    for player, piece in pieces.items():
        if piece >= GOAL_NUM:
            return player

    return ''

def valid_move(cell):
    for i in range(9):
        if grid[i] == cell:
            return i

    return -1

def print_grid(winner = ' '):
    for j in range(3):
        print("+-----------+")
        for i in range(3):
            if grid[index(i, j)] == 'X':
                print(f"| {colours['X']}X\x1b[0m ", end='')
            elif grid[index(i, j)] == 'O':
                print(f"| {colours['O']}O\x1b[0m ", end='')
            else:
                print(f"| \x1b[2m{grid[index(i, j)]}\x1b[0m ", end='')
            if i == 2:
                print("|")
    print("+-----------+")
    if winner == ' ':
        print(
            f"| {colours['X'] if curr == 'X' else ''}X:{'!' if winner == 'X' else (GOAL_NUM-pieces['X'])}\x1b[0m | {colours['O'] if curr == 'O' else ''}O:{'!' if winner == 'O' else (GOAL_NUM-pieces['O'])}\x1b[0m |"
        )
    else:
        print(f"|  {colours[winner]}{winner} wins!\x1b[0m  |")
    print("+-----------+")

#    print(f"""
#        +-----------+
#        | {grid[0]} | {grid[1]} | {grid[2]} |
#        +-----------+
#        | {grid[3]} | {grid[4]} | {grid[5]} |
#        +-----------+
#        | {grid[6]} | {grid[7]} | {grid[8]} |
#        +-----------+
#        | X:{'!' if winner == 'X' else players['X']}   O:{'!' if winner == 'O' else players['O']} |
#        +-----------+
#    """)

if __name__ == '__main__':
    while True:
        label_grid()

        print_grid()

        choice = input(f"[1~{9-pieces['X']-pieces['O']}]: ")
        if choice == 'q':
            break
        move = valid_move(choice)
        if move < 0:
            print("Invalid move")
            continue

        grid[move] = curr
        pieces[curr] += 1

        # Tundra
        ## Check horizontal rows
        for row in range(3):
            if grid[row*3] == grid[row*3 + 1] == grid[row*3 + 2] != ' ':
                pieces[curr] -= 3
                grid[row*3] = grid[row*3 + 1] = grid[row*3 + 2] = ' '

        ## Check vertical columns 
        for col in range(3):
            if grid[col] == grid[col + 3] == grid[col + 6] != ' ':
                pieces[curr] -= 3
                grid[col] = grid[col + 3] = grid[col + 6] = ' '

        ## Check diagonals
        if grid[0] == grid[4] == grid[8] != ' ':
            pieces[curr] -= 3
            grid[0] = grid[4] = grid[8] = ' '

        if grid[2] == grid[4] == grid[6] != ' ':
            pieces[curr] -= 3
            grid[2] = grid[4] = grid[6] = ' '

        if winner():
            break

        curr = 'O' if curr == 'X' else 'X'

    for i in range(9):
        if not grid[i] == 'X' and not grid[i] == 'O':
            grid[i] = ' '

    print_grid(curr)
