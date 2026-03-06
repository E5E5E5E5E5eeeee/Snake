def affichage(snake, pastille, TAILLE):
    fill(50,250,150)
    score = 0
    if snake[-1] == pastille:
        score.append(5)
    textSize(TAILLE + 5)
    text("Score = {}".format(score), 20 , 20)
    for c in snake[:-1]:
        rect(c[0],c[1],TAILLE,TAILLE)
    ellipse(snake[-1][0]+ TAILLE/2, snake[-1][1] + TAILLE/2, TAILLE, TAILLE)
    fill(200, 50, 200)
    ellipse(pastille[0]+ TAILLE/2, pastille[1] + TAILLE/2, TAILLE, TAILLE)
    
def deplacement(snake, dx, dy):
    snake.pop(0)
    snake.append([snake[-1][0]+dx, snake[-1][1]+dy])
    
def collision(snake, TAILLE):
    if snake[-1][0] > width - 2*TAILLE or snake[-1][0] < TAILLE or snake[-1][1] > height - 2*TAILLE or snake[-1][1] < TAILLE :
        finjeu(TAILLE)
    for c in snake[:-1]:
        if snake[-1][0] == c[0] and snake[-1][1] == c[1]:
            finjeu(TAILLE)
        
def finjeu(TAILLE):
    fill(250, 50, 150)
    textSize(TAILLE + 2)
    text("Fin du jeu", width/4, height/2)
    noLoop()
