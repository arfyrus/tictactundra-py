import re

grid = [' '] * 9
players = {'X': 4, 'O': 4}
curr = 'X'

def label_grid():
    num = 1
    for i in range(9):
        if not grid[i] == 'X' and not grid[i] == 'O':
            grid[i] = str(num)
            num += 1

def index(x, y):
    return x + y * 3

def winner():
    for player, pieces in players.items():
        if pieces <= 0:
            return player

    return ''

def valid_move(cell):
    for i in range(9):
        if grid[i] == cell:
            return i

    return -1

def print_grid(winner = ' '):
    print(f"""
        +-----------+
        | {grid[0]} | {grid[1]} | {grid[2]} |
        +-----------+
        | {grid[3]} | {grid[4]} | {grid[5]} |
        +-----------+
        | {grid[6]} | {grid[7]} | {grid[8]} |
        +-----------+
        | X:{'!' if winner == 'X' else players['X']}   O:{'!' if winner == 'O' else players['O']} |
        +-----------+
    """)

while True:
    label_grid()

    # Print the grid
    print_grid()

    choice = input(f"{curr}'s move: ")
    move = valid_move(choice)
    if move < 0:
        print("Invalid move")
        continue

    grid[move] = curr
    players[curr] -= 1

    # Tundra
    ## Check horizontal rows
    for row in range(3):
        if grid[row*3] == grid[row*3 + 1] == grid[row*3 + 2] != ' ':
            players[curr] += 3
            grid[row*3] = grid[row*3 + 1] = grid[row*3 + 2] = ' '

    ## Check vertical columns 
    for col in range(3):
        if grid[col] == grid[col + 3] == grid[col + 6] != ' ':
            players[curr] += 3
            grid[col] = grid[col + 3] = grid[col + 6] = ' '

    ## Check diagonals
    if grid[0] == grid[4] == grid[8] != ' ':
        players[curr] += 3
        grid[0] = grid[4] = grid[8] = ' '

    if grid[2] == grid[4] == grid[6] != ' ':
        players[curr] += 3
        grid[2] = grid[4] = grid[6] = ' '

    if winner():
        print(f"{winner()} won!")
        break

    # Switch player
    curr = 'O' if curr == 'X' else 'X'

# Remove the labels:
for i in range(9):
    if not grid[i] == 'X' and not grid[i] == 'O':
        grid[i] = ' '

print_grid(curr)
