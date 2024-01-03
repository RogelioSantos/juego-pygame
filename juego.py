import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cazador vs Objetivo")

# Colores
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Tamaño de los objetos
hunter_size = 50
target_size = 30

# Posición inicial del cazador
hunter_x = width // 2 - hunter_size // 2
hunter_y = height // 2 - hunter_size // 2

# Posición inicial del objetivo
target_x = random.randint(0, width - target_size)
target_y = random.randint(0, height - target_size)

# Velocidad del cazador
hunter_speed = 5

# Reloj para controlar la velocidad del bucle principal
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mover el cazador con las teclas de flecha
    keys = pygame.key.get_pressed()
    hunter_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * hunter_speed
    hunter_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * hunter_speed

    # Mantener al cazador dentro de la pantalla
    hunter_x = max(0, min(width - hunter_size, hunter_x))
    hunter_y = max(0, min(height - hunter_size, hunter_y))

    # Mover el objetivo aleatoriamente
    target_x += random.randint(-5, 5)
    target_y += random.randint(-5, 5)

    # Mantener al objetivo dentro de la pantalla
    target_x = max(0, min(width - target_size, target_x))
    target_y = max(0, min(height - target_size, target_y))

    # Colisiones
    if (
        hunter_x < target_x + target_size
        and hunter_x + hunter_size > target_x
        and hunter_y < target_y + target_size
        and hunter_y + hunter_size > target_y
    ):
        # Cazador atrapó al objetivo
        target_x = random.randint(0, width - target_size)
        target_y = random.randint(0, height - target_size)

    # Limpiar la pantalla
    screen.fill(white)

    # Dibujar el cazador y el objetivo
    pygame.draw.rect(screen, red, (hunter_x, hunter_y, hunter_size, hunter_size))
    pygame.draw.rect(screen, green, (target_x, target_y, target_size, target_size))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle principal
    clock.tick(30)

# Salir de Pygame
pygame.quit()

