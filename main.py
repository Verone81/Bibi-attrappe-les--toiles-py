import pygame
from random import randint

pygame.init()

largeur_fenetre = 400
hauteur_fenetre = 600

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption('Bibi attrape les etoiles ')

bibi = pygame.image.load('bibi.png')

couleur_bleu_nuit = pygame.Color(19, 41, 75)

left = False
right = False
x = 0

etoile = pygame.image.load("etoile1.png")

# Définir la position des étoiles
positions_etoiles = []
for i in range(10):
    positions_etoiles.append((randint(0, 368), randint(0, 200)))

vitesse_bibi = 0.5

running = True

while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                left = True
                right = False
            elif event.key == pygame.K_RIGHT:
                right = True
                left = False

    # Nettoyer la fenêtre
    fenetre.fill(couleur_bleu_nuit)

    # Déplacer Bibi
    if left and 200 + x > 0:
        x -= vitesse_bibi
    elif right and 200 + x < largeur_fenetre - 128:
        x += vitesse_bibi

    # Blit les étoiles
    for i, position in enumerate(positions_etoiles):
        fenetre.blit(etoile, position)

    # Blit Bibi
    fenetre.blit(bibi, (200 + x, hauteur_fenetre - 128, 128, 128))

    pygame.display.update()

pygame.quit()


    