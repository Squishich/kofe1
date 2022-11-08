from tkinter import *
import pygame
def start_click():
    W=10
    H =20
    TILE = 45
    GAME_RES = W*TILE, H*TILE 
    FPS = 60
    pygame.init()
    game_sc = pygame.display.set_mode(GAME_RES)
    clock = pygame.time.Clock()
    
    grid =[pygame.Rect(x*TILE, y*TILE,TILE,TILE)for x in range(w) for y in range(H)]

    while True:
        game_sc.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        [pygame.draw.rect(game_sc,(20,20,20),i_rect,1)for i_rect in grid]
        
        pygame.display.flip()
        clock.tick(FPS)

def click_pause():
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
root.geometry('312x10+{}+{}'.format(w, h))


start = Button(bg = 'gray',activebackground = 'green', text="Start", width=20, height=1, command = start_click).place(x = 0, y = 0)
pause = Button(bg = 'gray',activebackground='green' ,text="Pause", width=20, height=1,command = click_pause).place(x = 160, y = 0)


root.mainloop()