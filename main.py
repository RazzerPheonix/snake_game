import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка на Python")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Начальное положение змейки (список координат [x, y])
# Голова находится на первом месте в списке
snake = [[100, 100], [80, 100], [60, 100]]
snake_dir = [CELL_SIZE, 0]  # Изначально движемся вправо (по оси X)

# Начальная позиция еды
food = [300, 300]

# Кол-во очков
score = 0

running = True
while running:
    # 1. Обработка событий (нажатия клавиш)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Меняем направление движения, исключая разворот на 180 градусов в обратную сторону
            if event.key == pygame.K_UP and snake_dir[1] == 0:
                snake_dir = [0, -CELL_SIZE]
            elif event.key == pygame.K_DOWN and snake_dir[1] == 0:
                snake_dir = [0, CELL_SIZE]
            elif event.key == pygame.K_LEFT and snake_dir[0] == 0:
                snake_dir = [-CELL_SIZE, 0]
            elif event.key == pygame.K_RIGHT and snake_dir[0] == 0:
                snake_dir = [CELL_SIZE, 0]

    

pygame.quit()
sys.exit()