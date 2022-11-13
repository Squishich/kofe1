from tkinter import *
from tkinter import ttk
from copy import deepcopy
from random import choice, randrange 
import pygame
score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3:700, 4:1500}

def start_click():
    W=10
    H =20
    TILE = 32
    GAME_RES = W*TILE, H*TILE 
    FPS = 60
    pygame.init()
    game_sc = pygame.display.set_mode(GAME_RES)
    clock = pygame.time.Clock()
    
    grid =[pygame.Rect(x*TILE, y*TILE,TILE,TILE)for x in range(w) for y in range(H)]

    figures_pos = [[(-1,0),(-2,0),(0,0),(1,0)],
                    [(0,-1),(-1,-1),(-1,0),(0,0)],
                    [(-1,0),(-1,1),(0,0),(0,-1)],
                    [(0,0),(-1,0),(0,1),(-1,-1)],
                    [(0,0),(0,-1),(0,1),(-1,-1)],
                    [(0,0),(0,-1),(0,1),(-1,-1)],
                    [(0,0),(0,-1),(0,1),(-1,0)]]
    figures = [[pygame.Rect(x+W//2,y+1,1,1) for x,y in fig_pos] for fig_pos in figures_pos]
    figure_rect = pygame.Rect(0,0,TILE -2,TILE-2)
    
    field = [[0 for i in range(W)]for i in range (H)]

    anim_count, anim_speed, anim_limit =0,60,2000
    figure = deepcopy(choice(figures))

    global score, lines 
    global scores 

    def check_borders():
        if figure[i].x< 0 or figure[i].x>W -1:
            return False
        elif figure[i].y> H -1 or field[figure[i].y][figure[i].x]:
            return False 
        return True



    while True:
        dx, rotate = 0, FALSE
        dx = 0
        game_sc.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                elif event.key == pygame.K_DOWN:
                    anim_limit = 100
                elif event.key == pygame.K_UP:
                    rotate = TRUE
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].x +=dx
            if not check_borders():
                figure = deepcopy(figure_old)
                break
        
        anim_count += anim_speed
        if anim_count>anim_limit:
            anim_count = 0
            figure_old = deepcopy(figure)
            for i in range(4):
                figure[i].y +=1
                if not check_borders():
                    for i in range(4):
                        field[figure_old[i].y][figure_old[i].x] = pygame.Color('white')
                    figure = deepcopy(choice(figures))
                    anim_limit =2000
                    break

        center = figure [0]
        figure_old = deepcopy(figure)
        if rotate:
            for i in range(4):
                x=figure[i].y - center.y 
                y=figure[i].x - center.x
                figure[i].x =center.x - x
                figure[i].y =center.y + y
                if not check_borders():
                    figure = deepcopy(figure_old)
                    break
        
        line,lines  = H-1, 1
        for row in range(H-1,-1,-1):
            count = 0
            for i in range(W):  
                if field[row][i]:
                    count+=1
                field[line][i] = field[row][i]
            if count< W:
                line -=1
            else:
                anim_speed+= 3
                lines +=1
        
        score+=scores[lines]

        [pygame.draw.rect(game_sc,(27,27,27),i_rect,1)for i_rect in grid]
        
        for i in range(4):
            figure_rect.x = figure[i].x * TILE
            figure_rect.y = figure[i].y * TILE
            pygame.draw.rect(game_sc,pygame.Color('white'), figure_rect)

        for y, raw in enumerate(field):
            for x, col in enumerate(raw):
                if col:
                    figure_rect.x, figure_rect.y = x * TILE, y * TILE
                    pygame.draw.rect(game_sc, col, figure_rect)
                    
        pygame.display.flip()
        clock.tick(FPS)

def click_restart():
    breakpoint

root = Tk()

root.title("CaняСкриптер")


mainmenu = Menu(root)
root.config(menu=mainmenu)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2 # середина экрана
h = h//2
w = w - 672 # смещение от середины
h = h - 380
root.geometry('312x50+{}+{}'.format(w, h))

start = Button(bg = 'gray',activebackground = 'green', text="Start", width=20, height=1, command = start_click).place(x = 0, y = 0)
pause = Button(bg = 'gray',activebackground='green' ,text="Restart", width=20, height=1,command = click_restart).place(x = 160, y = 0)
label = ttk.Label(text="НАБРАННЫЕ ОЧКИ:",font=("Arial", 12))
label.place(x =0, y= 35)
label = ttk.Label(text=score,font=("Arial", 12))
label.place(x=240, y=35)




root.mainloop()