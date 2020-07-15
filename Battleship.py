import pygame
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
dis = pygame.display.set_mode((450, 450))
pygame.display.set_caption('Battleship')
 
game_over = False
 
x1 = 450
y1 = 450
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1,y1=pygame.mouse.get_pos()
    dis.fill(white)
    for x in range(8):
        for y in range(8):
            pygame.draw.rect(dis, red, [(x+1)*30,(y+1)*30,25,25])
    for x in range(8):
        for y in range(8):
            if (x+1)*30 <=x1 and ((x+1)*30+25) >=x1 and (y+1)*30 <=y1 and ((y+1)*30+25) >=y1:
                pygame.draw.rect(dis,black,[(x+1)*30,(y+1)*30,25,25])
#    print(x1,y1)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
