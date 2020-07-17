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

# Size of rectangle
WIDTH = 30

# Margin 
MARGIN = 2

# Diffrence
DIFFRENCE = WIDTH-MARGIN

# Size of game field
SIZE = 12

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
    pass

# Message function 
def message(msg):
    mesg = mesg_style.render(msg, True, red)
    dis.blit(mesg, [SIZE*35, SIZE*40])
    pygame.display.update()
    time.sleep(1)
    
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
    counter = 0 # if after 500 trys can not place new ship, start from begining
    position = 0 # position in ship_table
    result = table
    while True:
        if position == 7: # not longer ships than 7 field ship
            return result
        elif ship_table[position] == 0:
            position +=1
        elif counter == 10000:
            return [[-1]]
        else:
            row       = random.randint(0,SIZE -1) #starting position 
            column    = random.randint(0,SIZE -1)
            direction = random.randint(0,3)
            if result[row][column] == 1: #there is a ship in this coordinates
                counter +=1
                continue
            elif result[row][column] == 0 and position == 0 :
                if not is_ship_allowed(row,column,position+1,direction,result) : # stick to other ship cant add a new ship
                    counter +=1
                    continue
                else:
                    result[row][column] = 1
                    counter = 0 #ship added, counter reseted
                    ship_table[position] -= 1#success
            else:
                if   direction == 0: #top
                    if row - position <0: # out of board cant add ship 
                        counter +=1
                        continue
                    elif not is_ship_allowed(row,column,position+1,direction,result): # stick to other ship cant add a new ship
                        counter +=1
                        continue
                    else:
                        #result[row][column] = 1 #add ship begining  
                        for i in range(position+1): #add rest of ship
                            result[row-i][column] = 1
                        counter = 0
                        ship_table[position] -= 1#success

                elif direction == 1: #right
                    if column + position >=SIZE: # out of board cant add ship 
                        counter +=1
                        continue
                    elif not is_ship_allowed(row,column,position+1,direction,result): # stick to other ship cant add a new ship
                        counter +=1
                        continue
                    else:
                        #result[row][column] = 1 #add ship begining  
                        for i in range(position+1): #add rest of ship
                            result[row][column+i] = 1
                        counter = 0
                        ship_table[position] -= 1#success

                elif direction == 2: #down
                    if row + position >=SIZE: # out of board cant add ship 
                        counter +=1
                        continue
                    elif not is_ship_allowed(row,column,position+1,direction,result): # stick to other ship cant add a new ship
                        counter +=1
                        continue
                    else:
                        #result[row][column] = 1 #add ship begining  
                        for i in range(position+1): #add rest of ship
                            result[row+i][column] = 1
                        counter = 0
                        ship_table[position] -= 1#sucsess

                elif direction == 3: #left
                    if column - position <0: # out of board cant add ship 
                        counter +=1
                        continue
                    elif not is_ship_allowed(row,column,position+1,direction,result) : # stick to other ship cant add a new ship
                        counter +=1
                        continue
                    else:
                        #result[row][column] = 1 #add ship begining  
                        for i in range(position+1): #add rest of ship
                            result[row][column-i] = 1
                        counter = 0
                        ship_table[position] -= 1#success

def is_ship_allowed(row,column,lenght,direction,table):
    ##check if ship is allowed to be placed
    ##that means ship is not connected with other ship on table
    if direction == 0:
        deltaY = -1
        deltaX = 0
    elif direction == 1:
        deltaY = 0
        deltaX = 1      
    elif direction == 2:
        deltaY = 1
        deltaX = 0       
    elif direction == 3:
        deltaY = 0
        deltaX = -1       
    for iteration in range(lenght):
        try:
            if table[row-1][column] == 1:
                return False
        except IndexError:
            pass
        try:
            if table[row+1][column] == 1:
                return False
        except IndexError:
            pass
        try:
            if table[row][column-1] == 1:
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
backup = player_side
while not end: 
    player_side = random_ship_settlement(player_side,[5,4,3,2,1,0,0])
    if player_side[0][0]==-1:
        print("niestety")
        player_side = backup
    else:
        end = True
        
##MAIN LOOP

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exit if x clicked
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN: # get mouse position
            x,y=pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # if space is clicked then perform a move
                move(player_side,enemy_side,x,y)
                message("HIT")
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

    # Drawning player cursor position
    for row in range(SIZE):
        for column in range(SIZE):
            if (row+2)*WIDTH <=x and ((row+2)*WIDTH+DIFFRENCE) >=x and (column+2)*WIDTH <=y and ((column+2)*WIDTH+DIFFRENCE) >=y:
                pygame.draw.rect(dis,green,[(row+2)*WIDTH,(column+2)*WIDTH,DIFFRENCE,DIFFRENCE])
                print(row,column)
                break

    # Update screen 
    pygame.display.update()
    clock.tick(30)

    
#close game and quit program
pygame.quit()
quit()
