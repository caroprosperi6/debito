import pygame, sys
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
BEIGE = (235,235,235)

#PARAMETRI FINESTRA
screen_height = 400
screen_length = 800

#SETTAGGI BASE FINESTRA
WINDOW_SIZE = (screen_length, screen_height)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption("RUN")
screen.fill(WHITE)


#CLOCK PER TEMPORIZZARE IL PROGRAMMA 
clock = pygame.time.Clock()
fps = 60

#PARAMETRO GRAVITA' 
gravity = 0.6

#SFODNO CIELO 
cielo_image= pygame.image.load('cielo2.png')
pos_cielo_x = 0
pos_cielo_y = 0
cielo_image = pygame.transform.scale(cielo_image, (800, 400))


#IMMAGINE VITE
vite_image = pygame.image.load('cuore.png')
vite = 3
pos_vite_x = 650
pos_vite_y = 350
vite_image = pygame.transform.scale(vite_image, (50, 50))

#IMMAGINE PERSONAGGIO
personaggio_image = pygame.image.load('personaggio.png')
pos_personaggio_x = 20
pos_personaggio_y = 220
personaggio_image = pygame.transform.scale(personaggio_image, (150, 100))
velocità_salto = 8
velocità_discesa = 10
salti_max = 20
cont_salto = 0
cont_discesa = 0
first_time = True
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

        
    #movimento personaggio 
    keys = pygame.key.get_pressed()


    if keys[pygame.K_UP] and cont_salto < salti_max and first_time:
        cont_salto += 1
        pos_personaggio_y -= velocità_salto
        pygame.time.wait(5)
    elif cont_salto > 0:
        if first_time == True:
            cont_discesa = int(cont_salto * velocità_salto / velocità_discesa) 
            first_time  = False

        cont_discesa -= 1 

        if cont_discesa == 0:
            pos_personaggio_y = 220
            cont_salto = 0
            first_time = True
        elif cont_discesa > 0:
            pos_personaggio_y += velocità_discesa
        else: 
            print(" c'è un errore")
            
    

    #funzione che serve per rigenerare lo schermo ad ogni giro del ciclo 
    screen.fill(BLACK)
    # all_sprites_list.update()

    screen.blit(cielo_image, (pos_cielo_x, pos_cielo_y))
    screen.blit(personaggio_image, (pos_personaggio_x , pos_personaggio_y))
  

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