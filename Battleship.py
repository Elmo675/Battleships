import pygame
import time
pygame.init()
## VARIABLES

# Colors rgb
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (176,224,230)
green = (24,110,90)

# Size of rectangle
WIDTH = 30

# Margin 
MARGIN = 2

# Diffrence
DIFFRENCE = WIDTH-MARGIN

# Size of game field
SIZE = 10

# Exit module 
game_over = False

#Polish alphabet
ALPHABET = "ABCDEFGHIJKLMNOPRSTUWYZ"

##INITIALIZING

# Initialize player and enemy side
player_side = []
enemy_side  = []
for row in range(SIZE):
    # Add an empty array that will hold each cell
    # in this row
    player_side.append([])
    enemy_side.append([])
    for column in range(SIZE):
        player_side[row].append(0)
        enemy_side[row].append(0)
# Initialize display
dis = pygame.display.set_mode((SIZE*90, SIZE*50))
pygame.display.set_caption('Battleship')
# Initialize font style
mesg_style = pygame.font.SysFont(None, 50)
legend_style = pygame.font.SysFont("comicsansms", 15)

x = 0
y = 0
clock = pygame.time.Clock()


## FUNCTION

# Moving function
def move(player_side,enemy_side,x,y):
    pass

# Message function 
def message(msg,color):
    mesg = mesg_style.render(msg, True, color)
    dis.blit(mesg, [SIZE*35, SIZE*40])
    pygame.display.update()
    time.sleep(1)

def legend(side):
    if side==0: #for the left table
        delta=0
    else:       #for the right table moved with delta
        delta=WIDTH*(SIZE+2)
    text="     ".join(ALPHABET[:SIZE:]) #take exacly amount of Alphabet letters
    legend_top = legend_style.render(text,True,black)
    dis.blit(legend_top, [WIDTH*2+delta, WIDTH])
    for number in range(SIZE):
        legend_left=legend_style.render(str(number+1),True,black)
        dis.blit(legend_left,[WIDTH+delta,WIDTH*number+2*WIDTH])
    
## TEST SCENARIOS
#player_side[1][6] = 2
#player_side[1][5] = 1


##MAIN LOOP

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                move(player_side,enemy_side,x,y)
                message("HIT",red)
    # Fill background white
    dis.fill(white)

    # Enemy side drawning
    legend(0)
    for row in range(SIZE):
        for column in range(SIZE):
            color = blue
            if enemy_side[row][column]   == 1:
                color = black
            elif enemy_side[row][column] == 2:
                color = red
            pygame.draw.rect(dis, color, [(row+2)*WIDTH,(column+2)*WIDTH,DIFFRENCE,DIFFRENCE])  

    # Player side drawning
    legend(1)
    for row in range(SIZE):
        for column in range(SIZE):
            color = blue
            if player_side[row][column]   == 1:
                color = black
            elif player_side[row][column] == 2:
                color = red
            pygame.draw.rect(dis, color, [(row+SIZE+4)*WIDTH,(column+2)*WIDTH,DIFFRENCE,DIFFRENCE])

    # Drawning choosing rectangle
    for row in range(SIZE):
        for column in range(SIZE):
            if (row+2)*WIDTH <=x and ((row+2)*WIDTH+DIFFRENCE) >=x and (column+2)*WIDTH <=y and ((column+2)*WIDTH+DIFFRENCE) >=y:
                pygame.draw.rect(dis,green,[(row+2)*WIDTH,(column+2)*WIDTH,DIFFRENCE,DIFFRENCE])

    # Update screen 
    pygame.display.update()
    clock.tick(30)

    
#close game and quit program
pygame.quit()
quit()
