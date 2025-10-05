import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Create the window
window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("The Space")



#pygame background
bg = pygame.transform.scale(pygame.image.load("cosmos_bg.jpg"),(1000,800))

#pygame draw
def draw(player):
    window.blit(bg,(0,0))
    pygame.draw.rect(window,"red",player)
    pygame.display.update()


#player
player_WD = 40
player_HG = 60
player_vell = 1


clock = pygame.time.Clock()


# Main game loop
def main():
    run = True
    clock.tick(60)
    
    player = pygame.Rect(200, 800 - player_HG,player_HG,player_WD)





    while run:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        
        
        draw(player)
        
        keys = pygame.key.get_pressed()

        #moving function for player
        if keys[pygame.K_a] and player.x - player_vell >= 0:
            player.x -= player_vell
        if keys[pygame.K_d] and player.x + player_vell + player_WD <= 980:
            player.x += player_vell   
        if keys[pygame.K_w] and player.y - player_vell >= 0:
            player.y -= player_vell
        if keys[pygame.K_s] and player.y + player_vell + player_WD <= 800:
            player.y += player_vell


    pygame.quit()


if __name__ == "__main__":
    main()

    
