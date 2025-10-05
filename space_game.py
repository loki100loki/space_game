import pygame
import time
import random
pygame.font.init()

# Initialize Pygame
pygame.init()

# Create the window
window = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("The Space")

# pygame background
bg = pygame.transform.scale(pygame.image.load("cosmos_bg.jpg"), (1000, 800))

# font
font = pygame.font.SysFont("comicsans", 30)

# player
player_WD = 40
player_HG = 60
player_vell = 5

# clock
clock = pygame.time.Clock()

# start time
start_time = time.time()


# draw function
def draw(player, elapsed_time):
    window.blit(bg, (0, 0))  # draw background first
    pygame.draw.rect(window, "red", player)  # draw player
    time_text = font.render(f"time: {round(elapsed_time)}s", 1, "white")  # timer
    window.blit(time_text, (10, 10))  # draw timer on top
    pygame.display.update()


# main game loop
def main():
    run = True

    player = pygame.Rect(200, 800 - player_HG, player_WD, player_HG)

    while run:
        clock.tick(60)  # FPS
        elapsed_time = time.time() - start_time  # update timer every frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # update screen
        draw(player, elapsed_time)

        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vell >= 0:
            player.x -= player_vell
        if keys[pygame.K_d] and player.x + player_vell + player_WD <= 1000:
            player.x += player_vell
        if keys[pygame.K_w] and player.y - player_vell >= 0:
            player.y -= player_vell
        if keys[pygame.K_s] and player.y + player_vell + player_HG <= 800:
            player.y += player_vell

    pygame.quit()


if __name__ == "__main__":
    main()
