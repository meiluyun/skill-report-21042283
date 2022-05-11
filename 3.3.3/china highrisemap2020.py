import pygame, sys
import random
#this project shows in the distribution of the world's top 10 buildings in China in 2020

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
unit_width = screen_width / 5
unit_height = screen_height / 5
pygame.display.set_caption('china highrise 2020')

screen.fill((138,107,190))

backgroundmap1 = pygame.image.load('china.png')
w, h = backgroundmap1.get_size()
newbackground=pygame.transform.scale(backgroundmap1,(screen_width,screen_height))
screen.blit(newbackground,(0,0))

clock = pygame.time.Clock()

pygame.display.update()

rectangles = []
for i in range(5):
    row = []
    for j in range(5):
        r = pygame.Rect(i * (screen_width/5), j * (screen_height/5),
                        (screen_width/5), (screen_height/5))
        row.append(r)
    rectangles.append(row)



while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = event.pos

            if event.button == 1:
                if x > 3 * unit_width and x < 4 * unit_width and y > 1 * unit_width and y < 2 * unit_height:
                    unit_image = pygame.image.load('8.wuhan.jpg')
                    screen.blit(unit_image, [x, y])

                if x > 1 * unit_width and x < 2 * unit_width and y > 2 * unit_width and y < 3 * unit_height:
                    unit_image = pygame.image.load('4.guiyang.jpg')
                    screen.blit(unit_image, [x, y])

                if x > 1 * unit_width and x < 2 * unit_width and y > 3 * unit_width and y < 4 * unit_height:
                        unit_image = pygame.image.load('3.nanning.jpg')
                        screen.blit(unit_image, [x, y])

                if x > 2 * unit_width and x < 3 * unit_width and y > 4 * unit_width and y < 5 * unit_height:
                    unit_image = pygame.image.load('10.zhuhai.jpg')
                    screen.blit(unit_image, [x, y])

                if x > 3 * unit_width and x < 4 * unit_width and y > 3 * unit_width and y < 4 * unit_height:
                    unit_image = pygame.image.load('5.shenzhen.jpg')
                    screen.blit(unit_image, [x, y])

    pygame.display.update()
    clock.tick()




