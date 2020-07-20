import pygame
import time
import random
pygame.init()
## VARIABLES

# Colors rgb
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (176,224,230)
green = (24,110,90)
yellow = (255,255,51)

# Size of rectangle
WIDTH = 30

# Margin 
MARGIN = 2

# Diffrence
DIFFRENCE = WIDTH-MARGIN

# Size of game field
SIZE = 10

# Game xpeed
SPEED = 0.3

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
mesg_style   = pygame.font.SysFont(None, 50)
legend_style = pygame.font.SysFont("comicsansms", 15)

# Initialize cursor position
x = 0
y = 0

# Initialize clock
clock = pygame.time.Clock()


## FUNCTIONS

# Moving function
def move(player_side,enemy_side,x,y):
    shotX = -1
    shotY = -1
    for row in range(SIZE):
        for column in range(SIZE):
            if (row+2)*WIDTH <x and (row+3)*WIDTH >=x and (column+2)*WIDTH <y and (column+3)*WIDTH >=y:
                shotX=row
                shotY=column
                break
    if shotX == -1 or shotY == -1:
        message("SELECT A FIELD TO SHOOT")
        return False
    if enemy_side[shotX][shotY] == 1:
        enemy_side[shotX][shotY] = 2
        message("HIT")
        return True
    elif enemy_side[shotX][shotY] == 2 or enemy_side[shotX][shotY] == 3 :
        message("YOU SHOOT THIS FIELD BEFORE")
        return True
    elif enemy_side[shotX][shotY] == 0:
        enemy_side[shotX][shotY] = 3
        message("MISS")
        return True

# AI
    
def beginer_PC(player_side,enemy_side):
    beginer_x = random.randrange(SIZE -1)
    beginer_y = random.randrange(SIZE -1)
    if beginer_x == -1 or beginer_y == -1:
        message("ERROR")
        return False
    if player_side[beginer_x][beginer_y] == 1:
        player_side[beginer_x][beginer_y] = 2
        message("YOU HAVE BEEN HITED")
        return True
    elif player_side[beginer_x][beginer_y] == 2 or player_side[beginer_x][beginer_y] == 3:
        message("ENEMY MISSED STUPIDLY")
        return True
    elif player_side[beginer_x][beginer_y] == 0:
        player_side[beginer_x][beginer_y] = 3
        message("ENEMY MISS")
        return True

def advenced_PC(player_side,enemy_side):
    while True:
        advenced_x = random.randrange(SIZE -1)
        advenced_y = random.randrange(SIZE -1)
        if player_side[advenced_x][advenced_y] == 1:
            player_side[advenced_x][advenced_y] = 2
            message("YOU HAVE BEEN HITED")
            return True
        elif player_side[advenced_x][advenced_y] == 2 or player_side[advenced_x][advenced_y] == 3:
            continue
        elif player_side[advenced_x][advenced_y] == 0:
            player_side[advenced_x][advenced_y] = 3
            message("ENEMY MISS")
            return True




# Message function 
def message(msg):
    dis.fill(white)
    mesg = mesg_style.render(msg, True, red)
    dis.blit(mesg, [SIZE*30, SIZE*40])
    pygame.display.update()
    time.sleep(SPEED)
    
# Legend drawning function
def legend(side):
    if side==0: #for the left table
        delta=0
    else:       #for the right table 
        delta=WIDTH*(SIZE+2)
    text="     ".join(ALPHABET[:SIZE:]) #take exacly amount of Alphabet letters
    legend_top = legend_style.render(text,True,black)
    dis.blit(legend_top, [WIDTH*2+delta, WIDTH])
    for number in range(SIZE):
        legend_left=legend_style.render(str(number+1),True,black)
        dis.blit(legend_left,[WIDTH+delta,WIDTH*number+2*WIDTH])


def random_ship_settlement(table,ship_table):
    ## ships can not stick to each other ( but they can diagonally)
    ## ship table is a table which presents the number of ships
    ## for example:
    ## ship_table = [0,4,3,2,1,0,0] means:
    ## none  1 field ships
    ## four  2 field ships
    ## three 3 field ships
    ## two   4 field ships
    ## one   5 field ships
    ## none  6 field ships
    ## none  7 field ships
    counter = 0 # if after 1000 trys can not place new ship, exit with -1
    position = 6 # position in ship_table starting from the end of table 
    while True:
        if position == -1: # nothing more to check
            return table  # success
        elif ship_table[position] == 0:
            position -=1   # proceed
        elif counter == 1000:
            return [[-1]]  # fail
        else:
            row       = random.randrange(SIZE -1) # starting position 
            column    = random.randrange(SIZE -1)
            direction = random.randint(0,3)
            
            if table[row][column] == 1: # there is a ship in this coordinates
                counter +=1
                continue
            
            if   direction == 0 and row - position < 0: #ship out of board cant be set
                counter +=1
                continue 
            elif direction == 1 and column + position >= SIZE: #ship out of board cant be set
                counter +=1
                continue
            elif direction == 2 and row + position >= SIZE: #ship out of board cant be set
                counter +=1
                continue
            elif direction == 3 and column - position < 0: #ship out of board cant be set
                counter +=1
                continue
                            
            if not is_ship_allowed(row,column,position+1,direction,table): # stick to other ship cant add a new ship
                counter +=1
                continue
            else:
                for i in range(position+1): # add  ship
                    if direction == 0: # up
                        table[row-i][column] = 1
                    elif direction == 1: # right
                        table[row][column+i] = 1
                    elif direction == 2: # down
                        table[row+i][column] = 1
                    elif direction == 3: # left
                        table[row][column-i] = 1
                counter = 0
                ship_table[position] -= 1# success


def is_ship_allowed(row,column,lenght,direction,table):
    ##check if ship is allowed to be placed
    ##that means ship is not connected with other ship on table
    if direction == 0: #ship created toward up
        deltaY = -1
        deltaX = 0
    elif direction == 1: #ship created toward right
        deltaY = 0
        deltaX = 1      
    elif direction == 2: #ship created toward down
        deltaY = 1
        deltaX = 0       
    elif direction == 3: #ship created toward left
        deltaY = 0
        deltaX = -1       
    for iteration in range(lenght): 
        # check if there is a ship stick to position in 4 directions
        try:       
            if table[row-1][column] == 1 and row != 0: # for -1 element 
                return False
        except IndexError:
            pass
        try:
            if table[row+1][column] == 1:
                return False
        except IndexError:
            pass
        try:
            if table[row][column-1] == 1 and column != 0: # for -1 element
                return False
        except IndexError:
            pass
        try:
            if table[row][column+1] == 1:
                return False
        except IndexError:
            pass
        row    = row+deltaY
        column = column+deltaX
    return True

    
## TEST SCENARIOS

##player_side[1][-1] = 1
##player_side[1][0] = 1
##player_side[1][1] = 1
##player_side[1][2] = 1
##player_side[1][3] = 1
##player_side[1][4] = 2


end = False
counter = 0
while not end:
    try:
        player_side = random_ship_settlement(player_side,[0,0,0,0,0,0,5])
        enemy_side  = random_ship_settlement(enemy_side,[0,0,0,0,0,0,5])
    except IndexError :
        pass
    if player_side[0][0] == -1 or enemy_side[0][0] == -1: #fail, initialize again
        player_side = []
        enemy_side  = []
        print("NOT GOOD")
        for row in range(SIZE):
            # Add an empty array that will hold each cell
            # in this row
            player_side.append([])
            enemy_side.append([])
            for column in range(SIZE):
                player_side[row].append(0)
                enemy_side[row].append(0)
    else:
        end = True
    counter +=1
    if counter == 10000:break
if not end:
    quit()


        
##MAIN LOOP

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exit if x clicked
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN: # get mouse position
            x,y=pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # if space is clicked then perform a move
                if move(player_side,enemy_side,x,y)   == False: # if player did not selected the field, do not allow computer to move
                    continue
                if advenced_PC(player_side,enemy_side) == False:
                    print("i dont know what happened")
                    break
                #reset cursor position
                x=0
                y=0

    # Fill background white
    dis.fill(white)

    # Enemy side drawning
    legend(0)
    for row in range(SIZE):
        for column in range(SIZE):
            color = blue
            if enemy_side[row][column] == 2:
                color = red
            ############            
##            elif enemy_side[row][column]   == 1:
##                color = black
            ############
            elif enemy_side[row][column] == 3:
                color = yellow
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
            elif player_side[row][column] == 3:
                color = yellow
            pygame.draw.rect(dis, color, [(row+SIZE+4)*WIDTH,(column+2)*WIDTH,DIFFRENCE,DIFFRENCE])

    # Drawning player cursor position
    for row in range(SIZE):
        for column in range(SIZE):
            if (row+2)*WIDTH <x and (row+3)*WIDTH >=x and (column+2)*WIDTH <y and (column+3)*WIDTH >=y:
                pygame.draw.rect(dis,green,[(row+2)*WIDTH,(column+2)*WIDTH,DIFFRENCE,DIFFRENCE])
                print(row,column)
                break

    # Update screen 
    pygame.display.update()
    clock.tick(30)

    
#close game and quit program
pygame.quit()
quit()
