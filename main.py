import pygame

import random

# pygame setup
pygame.init()
w =  1234
h = 678
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("GALAXY_SHOOTER")
player_img = pygame.image.load("fighter.png")
player_x = 250
player_y = 600

clock = pygame.time.Clock()
running = True
# Enemy
enemy_img = pygame.Surface((40, 30))
enemy_img.fill((255, 0, 0))
enemy_speed = 2
enemies = []
for _ in range(6):
    x = random.randint(0, w - 40)
    y = random.randint(50, 200)
    enemies.append([x, y])
# Bullet
bullet_img = pygame.Surface((5, 15))
bullet_img.fill((255, 255, 0))
bullet_speed = -7
bullets = []
# Score
score = 0
font = pygame.font.SysFont("Arial", 28)
speed = 10

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += speed
    if keys[pygame.K_SPACE]:
        bullet_x = player_x + player_img.get_width()
        bullet_y = player_y + player_img.get_height()
        bullets.append([bullet_x, bullet_y])

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    for bullet in bullets:
        bullet[1] -= speed
    screen.blit(player_img, (player_x,player_y))
    # Draw enemies
    for ex, ey in enemies:
        screen.blit(enemy_img, (ex, ey))
    # Draw bullets
    for bx, by in bullets:
        screen.blit(bullet_img, (bx, by))
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), (bullet[0], bullet[1], 10, 5))
    # Score text
    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
