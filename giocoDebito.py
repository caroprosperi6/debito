import pygame, sys
from pygame.locals import *




BLACK = (0,0,0)
WHITE = (255,255,255)
BEIGE = (235,235,235)

#PARAMETRI FINESTRAs
screen_height = 600
screen_length = 600

#SETTAGGI BASE FINESTRA
WINDOW_SIZE = (screen_length, screen_height)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption("RUN")
screen.fill(WHITE)

#PUNTEGGIO
punteggio_alto = 0

#CLOCK PER TEMPORIZZARE IL PROGRAMMA 
clock = pygame.time.Clock()
fps = 60

#PARAMETRO GRAVITA' 
gravity = 0.6

#SFONDO SCHERMO

#IMMAGINE VITE
vite_image = pygame.image.load('cuore.png')
vite = 3
pos_vite_x = 450
pos_vite_y = 560
vite_image = pygame.transform.scale(vite_image, (50, 50))

#IMMAGINE PERSONAGGIO


#IMMAGINE GAME OVER
game_over = pygame.image.load('gameover.png')
pos_over_x = 150
pos_over_y = 120
game_over = pygame.transform.scale(game_over, (300, 300))


#CICLIO FONDAMENTALE
while True:
    
    mouse = pygame.mouse.get_pos()
    #CICLIO PER CHIUDERE IL PROGRAMMA QUANDO L'UTENTE VUOLE CHIUDERE LA FINESTRA 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #funzione che serve per rigenerare lo schermo ad ogni giro del ciclo 
    screen.fill(BLACK)
    # all_sprites_list.update()




    if vite == 3:
        screen.blit(vite_image, (pos_vite_x, pos_vite_y))
        screen.blit(vite_image, (pos_vite_x+ 40, pos_vite_y))
        screen.blit(vite_image, (pos_vite_x+ 80 , pos_vite_y))
        
    elif vite == 2:
        screen.blit(vite_image, (pos_vite_x, pos_vite_y))
        screen.blit(vite_image, (pos_vite_x+ 40, pos_vite_y))       
             
    elif vite == 1:
        screen.blit(vite_image, (pos_vite_x, pos_vite_y))
        
    if vite == 0:
        screen.blit(game_over, (pos_over_x, pos_over_y))
        pygame.display.flip()
        pygame.time.wait(3000)
        vite = 3 


    pygame.display.flip()
    
    # aspetto il prossimo frame
    clock.tick(fps)