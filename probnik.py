# Pygame шаблон - скелет для нового проекта Pygameimport
from tabnanny import check
from turtle import width
import pygame
randomWIDTH = 360
HEIGHT = 480
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:   
# Держим цикл на правильной скорости    
    clock.tick(FPS)    

# Ввод процесса (события)    
for event in pygame.event.get():
    #check for closing window - удОли
    #это просто обработка кнопок, второй фор не нужен
    if event.type == pygame.QUIT:
        running = False    # Обновление
    # пример дальше :
    #  if event.type == pygame.KEYDOWN:
    #      print(pygame.key.name(event.key))

# Рендеринг    
screen.fill(BLACK)    

# После отрисовки всего, переворачиваем экран    
pygame.display.flip()
pygame.quit()
