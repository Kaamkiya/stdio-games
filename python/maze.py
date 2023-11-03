"""
Maze

This is a maze game
"""

playerx = playery = EXITX = EXITY = None
MAZE = WIDTH = HEIGHT = None

PLAYER = '@' # try changing this
WALL = '#'
EMPTY = ' '
EXIT = 'E'
BLOCK = chr(9608) # what the player sees as the wall: '█'

# to find emojis, go to https://unicode.org/emoji/charts/emoji-list.html
# then replace the U+ with 0x and put it in a chr function, like so:
# chr(0x26F3)

WIDTH, HEIGHT, MAZE, playerx, playery, EXITX, EXITY

with open('maze10x10.txt', 'r', encoding='UTF-8') as f:
    MAZE = f.read()
    HEIGHT = len(MAZE.split('\n'))
    WIDTH = len(list(MAZE.split('\n')))

MAZE = MAZE.split('\n')# split the MAZE into rows

for i in range(HEIGHT):
    MAZE[i] = list(MAZE[i])

playerx = 0
playery = 0

EXITX = 0
EXITY = 0

for i in range(HEIGHT):
    for j in range(WIDTH):
        if MAZE[i][j] == 'S':
            playerx = i
            playery = j

        if MAZE[i][j] == 'E':
            EXITX = i
            EXITY = j


def draw_maze():
    """Display the maze:"""
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x, y) == (playerx, playery):
                print(PLAYER, end='')
            elif (x, y) == (EXITX, EXITY):
                print('X', end='')
            elif MAZE[x][y] == WALL:
                print(BLOCK, end='')
            else:
                print(MAZE[x][y], end='')
        print()  # Print a newline after printing the row.

while True:
    try:
        draw_maze()

        print('Where would you like to go?')
        print('  W')
        print('A   D')
        print('  S')

        direction = input('> ').lower()

        if direction not in ('w', 'a', 's', 'd', 'quit'):
            print('That is not a valid direction.')
            continue

        if direction == 'a':
            if MAZE[playerx][playery-1] == '#':
                print('That spot is taken, sorry.')
                continue

            playery = playery - 1

        if direction == 'd':
            if MAZE[playerx][playery+1] == '#':
                print('That spot is taken, sorry.')
                continue

            playery = playery + 1

        if direction == 'w':
            if MAZE[playerx-1][playery] == '#':
                print('That spot is taken, sorry.')
                continue

            playerx = playerx - 1

        if direction == 's':
            if MAZE[playerx+1][playery] == '#':
                print('That spot is taken, sorry.')
                continue

            playerx = playerx + 1

        if direction == 'quit':
            break

        if (playerx, playery) == (EXITX, EXITY):
            draw_maze()
            break
    except KeyboardInterrupt:
        break

print('Thank you for playing!')
