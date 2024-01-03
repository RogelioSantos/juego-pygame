import pygame
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cazador vs Objetivo")

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

hunter_size = 50
target_size = 30

hunter_x = width // 2 - hunter_size // 2
hunter_y = height // 2 - hunter_size // 2

target_x = random.randint(0, width - target_size)
target_y = random.randint(0, height - target_size)

hunter_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    hunter_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * hunter_speed
    hunter_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * hunter_speed

    hunter_x = max(0, min(width - hunter_size, hunter_x))
    hunter_y = max(0, min(height - hunter_size, hunter_y))

    target_x += random.randint(-5, 5)
    target_y += random.randint(-5, 5)

    target_x = max(0, min(width - target_size, target_x))
    target_y = max(0, min(height - target_size, target_y))

    if (
        hunter_x < target_x + target_size
        and hunter_x + hunter_size > target_x
        and hunter_y < target_y + target_size
        and hunter_y + hunter_size > target_y
    ):
        target_x = random.randint(0, width - target_size)
        target_y = random.randint(0, height - target_size)

    screen.fill(white)

    pygame.draw.rect(screen, red, (hunter_x, hunter_y, hunter_size, hunter_size))
    pygame.draw.rect(screen, green, (target_x, target_y, target_size, target_size))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
