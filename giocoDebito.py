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