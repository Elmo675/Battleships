import pygame



#moving function
def move(player_side,enemy_side,x,y):
    pass

pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (176,224,230)

#Size of rectangle
WIDTH = 30

#Margin 
MARGIN = 2

#diffrence
DIFFRENCE = WIDTH-MARGIN

#Size of game field
SIZE = 8

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
dis = pygame.display.set_mode((SIZE*80, SIZE*50))
pygame.display.set_caption('Battleship')
 
game_over = False
 
x = 0
y = 0
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                move(player_side,enemy_side,x,y)

    #fill background white
    dis.fill(white)

    #player side drawning
    for row in range(SIZE):
        for column in range(SIZE):
            color = blue
            if player_side[row][column]   == 1:
                color = black
            elif player_side[row][column] == 2:
                color = red
            pygame.draw.rect(dis, color, [(row+2)*WIDTH,(column+2)*WIDTH,DIFFRENCE,DIFFRENCE])  

    #enemy side drawning
    for row in range(SIZE):
        for column in range(SIZE):
            color = blue
            if enemy_side[row][column]   == 1:
                color = black
            elif enemy_side[row][column] == 2:
                color = red
            pygame.draw.rect(dis, color, [(row+SIZE+4)*WIDTH,(column+2)*WIDTH,DIFFRENCE,DIFFRENCE])

    #drawning choosing rectangle
    for row in range(SIZE):
        for column in range(SIZE):
            if (row+2)*WIDTH <=x and ((row+2)*WIDTH+DIFFRENCE) >=x and (column+2)*WIDTH <=y and ((column+2)*WIDTH+DIFFRENCE) >=y:
                pygame.draw.rect(dis,black,[(row+2)*WIDTH,(column+2)*WIDTH,DIFFRENCE,DIFFRENCE])

    #update screen 
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
