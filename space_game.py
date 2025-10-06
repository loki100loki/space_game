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

# danger
rock_add = 2000
rock_width = 10
rock_heigh = 20

# clock
clock = pygame.time.Clock()

# start time
start_time = time.time()


# draw function
def draw(player, elapsed_time, rocks, admin_mode):
    window.blit(bg, (0, 0))  # draw background first
    pygame.draw.rect(window, "red", player)  # draw player
    for rock in rocks:
        pygame.draw.rect(window, "white", rock)
    time_text = font.render(f"time: {round(elapsed_time)}s", 1, "white")  # timer
    window.blit(time_text, (10, 10))  # draw timer on top

    # show admin mode message
    if admin_mode:
        admin_mode_text = font.render("Admin Mode: ENABLED", 1, "yellow")
        immortal_message = font.render("You are IMMORTAL", 1, "yellow")
        window.blit(admin_mode_text, (10, 40))
        window.blit(immortal_message, (10, 70))

    pygame.display.update()


# main game loop
def main():
    run = True
    player = pygame.Rect(200, 800 - player_HG, player_WD, player_HG)

    rocks = []
    rock_count = 0
    rock_add = 2000
    hit = False
    admin_mode = False

    while run:
        rock_count += clock.tick(60)

        if rock_count > rock_add:
            for _ in range(3):
                rock_x = random.randint(0, 1000 - rock_width)
                rock = pygame.Rect(rock_x, -rock_heigh, rock_width, rock_heigh)
                rocks.append(rock)

            rock_add = max(200, rock_add - 50)
            rock_count = 0

        elapsed_time = time.time() - start_time  # update timer every frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

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

        # enable/disable admin mode (hold L+X)
        admin_mode = keys[pygame.K_l] and keys[pygame.K_x]

        # move rocks
        for rock in rocks[:]:
            rock.y += 5  # constant fall speed
            if rock.y > 800:
                rocks.remove(rock)
            elif rock.colliderect(player):
                if not admin_mode:  # only die if not immortal
                    rocks.remove(rock)
                    hit = True
                    break

        # draw everything (with admin mode text if active)
        draw(player, elapsed_time, rocks, admin_mode)

        # game lose screen
        if hit and not admin_mode:
            lost_text = font.render("You Lose!", 1, "white")
            window.blit(lost_text, (1000/2 - lost_text.get_width()/2,
                                    800/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            run = False  # exit after showing message

    pygame.quit()


if __name__ == "__main__":
    main()
