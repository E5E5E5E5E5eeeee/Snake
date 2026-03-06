from fonction import *
from random import *

TAILLE = 20
snake = []
pastille = [0, 0]
dx = TAILLE
dy = 0
score = 0

def setup():
    global snake, dx, dy, score
    size(500, 500)
    frameRate(10)
    

    snake = [[100, 100], [120, 100], [140, 100]]
    dx = TAILLE
    dy = 0
    score = 0
    
    generer_pastille()

def draw():
    global snake, dx, dy, score
    background(18, 164, 217)
    
    deplacement(snake, dx, dy)
    

    if snake[-1][0] == pastille[0] and snake[-1][1] == pastille[1]:
        score += 5

        snake.insert(0, list(snake[0])) 
        generer_pastille()
        
    collision(snake, TAILLE)
    
    # On appelle l'affichage en lui donnant le score
    affichage(snake, pastille, TAILLE)

def keyPressed():
    global dx, dy
    # Modifie la direction avec les flèches du clavier
    # Les conditions (ex: dy == 0) empêchent le serpent de faire demi-tour sur lui-même
    if keyCode == UP and dy == 0:
        dx, dy = 0, -TAILLE
    elif keyCode == DOWN and dy == 0:
        dx, dy = 0, TAILLE
    elif keyCode == LEFT and dx == 0:
        dx, dy = -TAILLE, 0
    elif keyCode == RIGHT and dx == 0:
        dx, dy = TAILLE, 0

def generer_pastille():
    global pastille
    # Place la pastille sur la grille de manière aléatoire
    pastille[0] = randrange(TAILLE, width - TAILLE, TAILLE)
    pastille[1] = randrange(TAILLE, height - TAILLE, TAILLE)
