import pygame
import sys
from typing import Tuple

#iniciar pygame
pygame.init()

# Pantalla de la aplicacion
width: int = 500
height: int = 800
surface: pygame.Surface = pygame.display.set_mode( (width, height), pygame.RESIZABLE )
title = pygame.display.set_caption("Este es el titulo")
# Colores
red: Tuple[int, int, int] = (255, 0, 0)
green: Tuple[int, int, int] = (0, 255, 0)
yellow: Tuple[int, int, int] = (255, 255, 0)
blue: Tuple[int, int, int] = (0, 0, 255)
black: Tuple[int, int, int] = (0, 0, 0)
white: Tuple[int, int, int] = (255, 255, 255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            surface = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            
    surface.fill(black)
    
    # Cara
    
    #Bola
    pygame.draw.circle(surface, yellow, (200, 300), 200)
    #Ojos
    pygame.draw.circle(surface, white, (150, 200), 40)
    pygame.draw.circle(surface, white, (250, 200), 40)
    #pupilas
    pygame.draw.circle(surface, black, (150, 200), 20)
    pygame.draw.circle(surface, black, (250, 200), 20)
    # boca
    pygame.draw.line(surface, black, (300, 360), (40, 360), 20)
    
    
    pygame.display.update()
