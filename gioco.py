import pygame, sys
from pygame.locals import *
from personaggio import Personaggio
from ostacolo import Ostacolo

BLACK = (0,0,0)
WHITE = (255,255,255)
BEIGE = (235,235,235)
pygame.init()


#PARAMETRI FINESTRA
screen_height = 400
screen_length = 900

#SETTAGGI BASE FINESTRA
WINDOW_SIZE = (screen_length, screen_height)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption("RUN")
screen.fill(WHITE)


#CLOCK PER TEMPORIZZARE IL PROGRAMMA 
clock = pygame.time.Clock()
fps = 120


#SFODNO CIELO 
cielo_image= pygame.image.load('cielo2.png')
pos_cielo_x = 0
pos_cielo_y = 0
cielo_image = pygame.transform.scale(cielo_image, (screen_length, screen_height))


#IMMAGINE VITE
vite_image = pygame.image.load('cuore.png')
vite = 3
pos_vite_x = 650
pos_vite_y = 350
vite_image = pygame.transform.scale(vite_image, (50, 50))

#IMMAGINE PERSONAGGIO
pos_personaggio_x = 20
pos_personaggio_y = 220
personaggio = Personaggio(150, 100, 'personaggio.png', pos_personaggio_x, pos_personaggio_y)
velocità_salto = 6
velocità_discesa = 5
salti_max = 40
cont_salto = 0
cont_discesa = 0
first_time = True


#IMMAGINE OSTACOLO 
ostacolo_lenght = 100
ostacolo_height = 90
pos_ostacolo_y  = 215

ostacolo  = Ostacolo(ostacolo_lenght, ostacolo_height, 'cactus.png', 300, pos_ostacolo_y)
ostacolo2 = Ostacolo(ostacolo_lenght, ostacolo_height, 'cactus.png', 600, pos_ostacolo_y)
ostacolo3 = Ostacolo(ostacolo_lenght, ostacolo_height, 'cactus.png', 900, pos_ostacolo_y)
ostacolo4 = Ostacolo(ostacolo_lenght, ostacolo_height, 'cactus.png', 960, pos_ostacolo_y)

velocità_ostacolo = 4
pos_ostacolo_rigenerato = 1000


#IMMAGINE GAME OVER
game_over = pygame.image.load('gameover.png')
pos_over_x = 100
pos_over_y = 30
game_over = pygame.transform.scale(game_over, (700, 400))


invulnerabilità = 80


# Posizione e dimensioni del rettangolo
rectangle_x = 430
rectangle_y = 10
rectangle_width = 900
rectangle_height = 90

punteggio = 0 
pause = False 

#oggetto font per stampare punteggio 
font = pygame.font.Font(None, 36)

bonus = False

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
    if pause == True:
        screen.blit(game_over, (pos_over_x, pos_over_y))
        pygame.display.flip()
    #if che fa ricominciare partita 
    if keys[pygame.K_SPACE] and pause == True:
        pause = False
        velocità_salto = 6
        velocità_ostacolo = 4
        punteggio = 0 
    if pause == True:
        screen.blit(game_over, (pos_over_x, pos_over_y))
        pygame.display.flip()

    if keys[pygame.K_UP] and cont_salto < salti_max and first_time:
        cont_salto += 1
        personaggio.rect.y -= velocità_salto
        pygame.time.wait(5)

    elif cont_salto > 0:
        if first_time == True:
            cont_discesa = int(cont_salto * velocità_salto / velocità_discesa) 
            first_time  = False

        cont_discesa -= 1 

        if cont_discesa <= 0:
            personaggio.rect.y = 220
            cont_salto = 0
            first_time = True
        elif cont_discesa > 0:
            personaggio.rect.y += velocità_discesa
       
            
    if ostacolo.rect.x < -120:
        ostacolo.rect.x = pos_ostacolo_rigenerato
    else: 
        ostacolo.rect.x -= velocità_ostacolo
    
    if ostacolo2.rect.x < -120:
        ostacolo2.rect.x = pos_ostacolo_rigenerato
    else: 
        ostacolo2.rect.x -= velocità_ostacolo 
    
    if ostacolo3.rect.x < -120:
        ostacolo3.rect.x = pos_ostacolo_rigenerato
    else: 
        ostacolo3.rect.x -= velocità_ostacolo 
    
    if ostacolo4.rect.x < -120:
        ostacolo4.rect.x = pos_ostacolo_rigenerato
    else: 
        ostacolo4.rect.x -= velocità_ostacolo 

    
    
  

    #funzione che serve per rigenerare lo schermo ad ogni giro del ciclo 
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, WHITE, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))

    screen.blit(cielo_image, (pos_cielo_x, pos_cielo_y))

    if (pygame.sprite.collide_mask(personaggio, ostacolo) or pygame.sprite.collide_mask(personaggio, ostacolo2) or pygame.sprite.collide_mask(personaggio, ostacolo3) or pygame.sprite.collide_mask(personaggio, ostacolo4)) and invulnerabilità == 80:
        vite -= 1  
        invulnerabilità = 0
    
    if invulnerabilità < 80:
        invulnerabilità += 1


    personaggio.draw(screen)
    ostacolo.draw(screen)
    ostacolo2.draw(screen)
    ostacolo3.draw(screen)
    ostacolo4.draw(screen)

  

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
        # screen.fill(BLACK)
        screen.blit(game_over, (pos_over_x, pos_over_y))
        pygame.display.flip()
        pause = True
        velocità_ostacolo = 0
        velocità_salto = 0           
        vite = 3 
        ostacolo.rect.x  = 300
        ostacolo2.rect.x =  600
        ostacolo3.rect.x =  900
        ostacolo4.rect.x = 960

       
  
    #DISPLAY PUNTEGGIO
    if pause == False:
        punteggio += 1
        if bonus == True:
            punteggio += 1 
            bonus_surface = font.render('Bonus!', True, (0,0,0))
            aggiunta = len(str(punteggio))
            screen.blit(bonus_surface, (60 + aggiunta*5 ,10))

    if punteggio % 1000 == 0:
        bonus = True 
    if punteggio % 1000 == 500:
        bonus = False
    
    
    
    punteggio_surface = font.render(str(punteggio), True, (0,0,0))
    screen.blit(punteggio_surface, (10,10))

    if pause == False:
        pygame.display.flip()
    
    # aspetto il prossimo frame
    clock.tick(fps)