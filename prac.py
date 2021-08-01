import pygame

pygame.init()  # Initializing pygame

# Initializing variables
x = 0
y = 0
global box
box = 600/9
global grid
grid = [[[[0]*3 for _ in range(3)]for _ in range(3)]for _ in range(3)]
X = -1
Y = -1
running = True
turn = 0

# Initializing display
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption('Ultimate Tic-Tac Toe')
player1 = pygame.image.load('x.png')
player2 = pygame.image.load('o.png')


def update_game(x, y, turn):
    X = x // 3
    Y = y // 3
    x = x % 3
    y = y % 3
    if turn == 0:
        grid[X][Y][x][y] = 1
        turn = 1
    elif turn == 1:
        grid[X][Y][x][y] = 2
        turn = 0


# def draw_box(X, Y):

# GAME LOOP
while running:
    # White background and grid lines
    screen.fill((255, 255, 255))
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0),
                             (i * box, 0), (i * box, 9 * box), 4)
            pygame.draw.line(screen, (0, 0, 0),
                             (0, i * box), (9 * box, i * box), 4)
        else:
            pygame.draw.line(screen, (0, 0, 0),
                             (i * box, 0), (i * box, 9 * box), 2)
            pygame.draw.line(screen, (0, 0, 0),
                             (0, i * box), (9 * box, i * box), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = int(pos[0] // box)
            y = int(pos[1] // box)

            if x > 8 or y > 8 or grid[x // 3][y // 3] == 1 or grid[x // 3][y // 3] == 2:
                continue
            elif X == -1 and Y == -1:
                update_game(x, y, turn)

                X = x % 3
                Y = y % 3
                #draw_box(X, Y)

    pygame.display.update()
pygame.quit()
