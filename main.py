
import pygame
import copy
import time
WINWIDTH = 800
WINHEIGHT = 800
WHITE = (200,200,200)
AQUA = (0,95,98)
pygame.init()
win = pygame.display.set_mode((WINWIDTH,WINHEIGHT))
pygame.display.set_caption("Conway's Game of Life")
run = True
size = 50
playback = False
playbackspeed = 0.22
grid = []
livecells = []
for i in range(0,size):
    grid.append([])
    for j in range(0,size):
        grid[i].append(0)
prev = copy.deepcopy(grid)
empty = copy.deepcopy(grid)
def play(x, y):
    global prev
    live = 0
    for dx in range(-1, 2):
        for dy in range(-1,2):
            if dx != 0 or dy != 0:
                if (x + dx > -1) and (x+dx < int(len(prev[0]))) and (y+dy > -1) and (y+dy < int(len(prev))):
                    if prev[y+dy][x+dx] == 1:
                        live += 1
                else:
                    grid[y][x] = 0
    if prev[y][x] == 1:
        if live == 2 or live == 3:
            grid[y][x] = 1
        else:
            grid[y][x] = 0
    elif prev[y][x] == 0:
        if live == 3:
            grid[y][x] = 1
def windowToBoardCoord(win_x, win_y):
    board_x = win_x // (WINWIDTH // size)
    board_y = win_y // (WINWIDTH // size)
    return board_x, board_y
def drawRect(color, row, column):
    pygame.draw.rect(win, (color),
                    (((column * (WINWIDTH) // size)), ((row * (WINWIDTH) // size))
                    , (WINWIDTH - 24) // size, (WINHEIGHT - 24) // size))
def bgupdategrid():
    for row in range(0,size):
        for column in range(0,size):
            CHOSENCOLOR = WHITE
            if prev[row][column] == 1:
                CHOSENCOLOR = AQUA
            else:
                CHOSENCOLOR = WHITE
            drawRect(CHOSENCOLOR, row, column)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            boardx, boardy = windowToBoardCoord(event.pos[0], event.pos[1])
            prev[boardy][boardx] = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if playback == False:
                    for i in range(0,size):
                        for j in range(0,size):
                            play(j, i)
                prev = copy.deepcopy(grid)
            elif event.key == pygame.K_SPACE:
                if playback == False:
                    playback = True
                else:
                    playback = False    
            elif event.key == pygame.K_UP:
                print("Up key pressed")
                if playbackspeed > 0.02:
                    playbackspeed -= 0.04
            elif event.key == pygame.K_DOWN:
                if playbackspeed < 0.30:
                    playbackspeed += 0.04
            elif event.key == pygame.K_TAB:
                playbackspeed = 0.1   
    if playback == True:
        for i in range(0,size):
            for j in range(0,size):
                play(j, i)
        time.sleep(playbackspeed)
        prev = copy.deepcopy(grid)
        if prev == empty:
            playback = False
    bgupdategrid()
    pygame.display.flip()