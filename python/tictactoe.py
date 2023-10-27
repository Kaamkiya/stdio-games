"""
Tic Tac Toe by Kaamkiya
"""

__version__ = '0.0.3'

turn = 'x' # the first player is always x

board = [
    [' ', ' ', ' '], # set up the board to a 2d, fully empty, list
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

def print_board(b):
    """Print a board b"""
    print()
    print('    0 1 2')
    print('0   '+b[0][0]+'|'+b[0][1]+'|'+b[0][2]) # top row
    print('    -+-+-')
    print('1   '+b[1][0]+'|'+b[1][1]+'|'+b[1][2]) # middle row
    print('    -+-+-')
    print('2   '+b[2][0]+'|'+b[2][1]+'|'+b[2][2]) # bottom row
    print()

def place(turn):
    """Get the place that the user wants to go
    and see if they can go there."""
    pos = input()
    try:
        if board[int(pos[0])][int(pos[1])] == ' ':
            board[int(pos[0])][int(pos[1])] = turn
        else: # if that spot is taken
            print('Must be Y-coordinate+X-coordinate. Eg, 02')
            place(turn)
    except:
        print('Must be Y-coordinate+X-coordinate. Eg, 02')
        place(turn) # if the user enters anything other than a number

def check_win(b):
    """Check if someone on a given board b has
    won the game"""
    for i in range(3):
        if b[i] == ['x', 'x', 'x']: # check for each row of the board if x won
            print('x wins!')
            return 'gameover'
        if b[i] == ['o', 'o', 'o']: # same for o
            print('o wins!')
            return 'gameover'

    x = 0
    o = 0
    for i in range(3):
        if b[i][0] == 'x':
            x += 1
        if b[i][0] == 'o': # scan throught columns to check for wins
            o += 1
        if x == 3:
            print('x wins!')
            return 'gameover'
        if o == 3:
            print('o wins!')
            return 'gameover'
    x = 0
    o = 0
    for i in range(3):
        if b[i][i] == 'x':
            x += 1
        if b[i][i] == 'o':
            o += 1
        if x == 3:
            print('x wins!')
            return 'gameover'
        if o == 3:
            print('o wins!')
            return 'gameover'
    x = 0
    o = 0
    for i in range(3):
        if b[i][2-i] == 'x': # check the diagonals
            x += 1
        if b[i][2-i] == 'o':
            o += 1
        if x == 3:
            print('x wins!')
            return 'gameover'
        if o == 3:
            print('o wins!')
            return 'gameover'
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if b[i][j] == 'x':
                x += 1

            if b[i][j] == 'o':
                o += 1

    x = 0
    for i in range(3):
        if ' ' not in b[i]:
            x += 1

    if x == 3:
        print('Tie')
        return 'gameover'


while True:
    print_board(board)
    print('%s\'s turn' %turn)
    place(turn)

    if turn=='x':
        turn = 'o'
    else:
        turn = 'x'

    if check_win(board) == 'gameover':
        print_board(board)
        break
