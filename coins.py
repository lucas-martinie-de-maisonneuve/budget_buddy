import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
piece_img = pygame.image.load("assets/image/Accounts/accounts_coins.png",
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotation de pièce")

# Chargement de l'image de la pièce
)
piece_rect = piece_img.get_rect()

# Position initiale de la pièce
piece_x = (SCREEN_WIDTH - piece_rect.width) // 2
piece_y = (SCREEN_HEIGHT - piece_rect.height) // 2

# Vitesse de rotation de la pièce (en degrés par frame)
rotation_speed = 2

# Boucle principale
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    screen.fill((255, 255, 255))

    # Rotation de la pièce
    rotated_piece = pygame.transform.rotate(piece_img, rotation_speed)
    rotated_piece_rect = rotated_piece.get_rect(center=piece_rect.center)

    # Affichage de la pièce tournante
    screen.blit(rotated_piece, rotated_piece_rect.topleft)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Mise à jour de la rotation pour la prochaine frame
    rotation_speed += 1  # Augmente la vitesse de rotation

    # Limite de vitesse de la boucle
    clock.tick(60)
