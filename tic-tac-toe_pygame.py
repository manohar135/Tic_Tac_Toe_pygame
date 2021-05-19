import pygame
import time
import sys
from pygame.locals import *

pygame.init()
CLOCK = pygame.time.Clock()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

draw = None
winner = None
turn = 'O'

cell = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

My_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + 100))
pygame.display.set_caption('Tic-Tac-Toe')

x_img = pygame.image.load('img\X.png')
y_img = pygame.image.load("img\O.png")

X_img = pygame.transform.scale(x_img, (120, 120))
O_img = pygame.transform.scale(y_img, (120, 120))


def Draw_board():

    ver_line_1 = pygame.Rect(SCREEN_WIDTH/3, 10, 10, (SCREEN_HEIGHT - 20))
    pygame.draw.rect(My_screen, (255, 255, 255), ver_line_1)

    ver_line_2 = pygame.Rect(SCREEN_WIDTH*(2/3), 10, 10, (SCREEN_HEIGHT - 20))
    pygame.draw.rect(My_screen, (255, 255, 255), ver_line_2)

    hor_line_1 = pygame.Rect(10, (SCREEN_HEIGHT)/3, (SCREEN_WIDTH - 20), 10)
    pygame.draw.rect(My_screen, (255, 255, 255), hor_line_1)

    hor_line_1 = pygame.Rect(10, (SCREEN_HEIGHT)*(2/3),
                             (SCREEN_WIDTH - 20), 10)
    pygame.draw.rect(My_screen, (255, 255, 255), hor_line_1)

    draw_status()

def draw_status():
    global draw, winner

    if winner is None:
        message = turn + "'s Turn"
    else:
        message = winner + " WON!!"
    if draw:
        message = "Game Draw !"

    font = pygame.font.Font(None, 50)
    text = font.render(message, 1, (50, 50, 50))

    My_screen.fill((100, 100, 100), (0, 500, 500, 100))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, 600-50))
    My_screen.blit(text, text_rect)

    pygame.display.update()

# Logic for checking the winner 
def check_winner():
    global winner, cell, draw

    for row in range(0, 3):
        if ((cell[row][0] == cell[row][1] == cell[row][2]) and (cell[row][0] is not None)):
            winner = cell[row][0]
            # for stright line when winner is checked in row
            pygame.draw.line(My_screen, (255, 0, 0),                         
            (0, SCREEN_HEIGHT*(2*(row + 1) - 1)/6),
             (SCREEN_WIDTH, SCREEN_HEIGHT*(2*(row + 1) - 1)/6),
              4)
            break
    
    for col in range(0, 3):
        if ((cell[0][col] == cell[1][col] == cell[2][col]) and (cell[0][col] is not None)):
            winner = cell[0][col]
            # for stright line when winner is checked in colomn
            pygame.draw.line(My_screen,  (255, 0, 0),                         
            (SCREEN_WIDTH*(2*(col + 1) - 1)/6, 0),
             (SCREEN_WIDTH*(2*(col + 1) - 1)/6, SCREEN_HEIGHT),
              4)
            break

    if ((cell[0][0] == cell[1][1] == cell[2][2]) and (cell[0][0] is not None)):
        winner = cell[0][0]
        pygame.draw.line(My_screen,  (255, 0, 0),                         
            (0, 0),(SCREEN_WIDTH, SCREEN_HEIGHT),
              4)
            
    if ((cell[0][2] == cell[1][1] == cell[2][0]) and (cell[0][2] is not None)):
        winner = cell[0][2]
        pygame.draw.line(My_screen,  (255, 0, 0),                         
            (SCREEN_WIDTH, 0), (0, SCREEN_HEIGHT),
              4)

    draw_verify = []
    for row in cell:
        draw_verify.append(all(row))
    if all(draw_verify):
        draw = True
    draw_status()


# Displaying O and X on to the Screen
def display_OX(row, col):
    global cell, turn

    # Positions for row
    if row == 1:
        pos_x = 30

    if row == 2:
        pos_x = SCREEN_WIDTH / 3 + 30

    if row == 3:
        pos_x = SCREEN_WIDTH * 2/3 + 30
    
    # Positions for colomn
    if col == 1:
        pos_y = 30

    if col == 2:
        pos_y = SCREEN_HEIGHT / 3 + 30

    if col == 3:
        pos_y = SCREEN_HEIGHT * 2/3 + 30

    cell[row-1][col-1] = turn

    # Here the img is drawn on the given position
    if turn == 'X':
        My_screen.blit(X_img, (pos_y, pos_x))
        turn = 'O'
    else:
        My_screen.blit(O_img, (pos_y, pos_x))
        turn = 'X'
    pygame.display.update()

# Defining The position when the mouse is clicked
def mouse_click():
    x, y = pygame.mouse.get_pos()
    
    if x < SCREEN_WIDTH / 3:
        col = 1
    elif x < SCREEN_WIDTH * 2/3:
        col = 2
    elif x < SCREEN_WIDTH:
        col = 3
    else:
        col = None

    if y < SCREEN_HEIGHT / 3:
        row = 1
    elif y < SCREEN_HEIGHT * 2/3:
        row = 2
    elif y < SCREEN_HEIGHT:
        row = 3
    else:
        row = None

    # To display on mouse click
    if row and col and cell[row - 1][col - 1] is None:
        global turn
        display_OX(row, col)
        check_winner()

def reset_game():
    global cell, winner, turn, draw, My_screen
    turn = 'X'
    My_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + 100))
    Draw_board()
    draw = None
    winner = None
    cell = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
        ]

def To_reset():
    if winner or draw is not None:
        time.sleep(2)

        font = pygame.font.Font(None, 50)
        text = font.render("Press R to reset", 1, (0, 250, 255))

        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        My_screen.blit(text, text_rect)



My_screen.fill((30, 30, 30))
Draw_board()

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_click()
            To_reset()
        if event.type == KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()



    CLOCK.tick(60)
    pygame.display.update()

    
