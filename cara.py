import pygame
import sys

#iniciar pygame
pygame.init()

# Pantalla de la aplicacion
width = 500
height = 800
surface = pygame.display.set_mode( (width, height) )
title = pygame.display.set_caption("Este es el titulo")

# Colores
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
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
    # sonrrisa
    pygame.draw.line(surface, black, (300, 360), (40, 360), 20)
    
    
    pygame.display.update()
    
            
# https://admision.usmp.edu.pe/examenSimulacro/simulacroOrdinario.html
# simulacro de examen de admicion