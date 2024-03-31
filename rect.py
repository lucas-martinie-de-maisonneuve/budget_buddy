import pygame
import sys

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
width, height = 400, 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rectangle avec effet shadow")

# Définir les couleurs
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Position et taille du rectangle principal
rect_width, rect_height = 200, 100
rect_x, rect_y = 100, 100

# Position et taille de l'ombre
shadow_offset = 2

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    window.fill((255, 255, 255))

    # Dessiner l'ombre
    shadow_rect = pygame.Rect(rect_x + shadow_offset, rect_y + shadow_offset, rect_width, rect_height)
    pygame.draw.rect(window, DARK_GRAY, shadow_rect)

    # Dessiner le rectangle principal
    main_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
    pygame.draw.rect(window, GRAY, main_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter le nombre d'images par seconde
    pygame.time.Clock().tick(60)

# Quitter Pygame
pygame.quit()
sys.exit()
