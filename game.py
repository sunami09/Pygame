import pygame
import random
import math
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,700))
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("spaceship.png")
bullet=pygame.image.load("bullet.png")
pygame.display.set_icon(icon)
playerimage=pygame.image.load("rocket.png")
playerX=370
playerY=600
xchange=0
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
status=font.render("Game Over",True,(255,0,0))
score_status=font.render("Your Score is "+str(score_value),True,(0,0,255))
textX=10
textY=10
mixer.music.load("background.wav")
mixer.music.play(-1)
game_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score():
    score=font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(textX,textY))
def game_over_text():
    score=font.render("Your Score is "+str(score_value),True,(0,255,0))
    Over_text=game_font.render("GAME OVER",True,(255,255,255))
    screen.blit(Over_text,(200,300))
    screen.blit(score,(220,400))
enemyimage=pygame.image.load("spaceinvaders.png")
enemyX=random.randint(80,700)
enemyY=100
exchange=1
eychange=40
enemyimage = []
enemyX = []
enemyY = []
eychange = []
exchange = []
num_of_enemies = 4
for i in range(num_of_enemies):
    enemyimage.append(pygame.image.load("spaceinvaders.png"))
    enemyX.append(random.randint(80,700))
    enemyY.append(100)
    exchange.append(3)
    eychange.append(40)
bulletX=20
bulletY=playerY+10
bychange=1 
bullet_stat="ready"
def player():
    screen.blit(playerimage,(round(playerX),round(playerY)))
def enemy(x,y,i):
    screen.blit(enemyimage[i],(round(x),round(y)))
def bullet1(x,y):
    global bullet_stat
    bullet_stat="fired"
    screen.blit(bullet,(round(x),round(y)))
def collision(enemyX,bulletX,enemyY,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance<33:
        return True
    else:
        return False
    
running=True
while running:
    screen.fill((6, 19, 24)) 
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                xchange=0.4 
            elif event.key==pygame.K_LEFT:
                xchange=-0.4
            elif event.key==pygame.K_SPACE:
                if bullet_stat=="ready":
                    bullet_sound=mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX=playerX
                    bullet1(bulletX+16,bulletY)
            
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                xchange=0
    playerX+=xchange
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    enemyX+=exchange
    for i in range(num_of_enemies):
        if enemyY[i]>500:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
        if enemyX[i]<=0:
            exchange[i]=0.3
            enemyY[i]+=eychange[i]
        elif enemyX[i]>=736:
            exchange[i]=-0.3
            enemyY[i]+=eychange[i]
        enemyX[i]+=exchange[i]
        collision1=collision(enemyX[i],bulletX,enemyY[i],bulletY)
        if collision1:
            explosion=mixer.Sound("explosion.wav")
            explosion.play()
            bulletY=playerY
            bullet_stat="ready"
            score_value+=1
            enemyX[i]=random.randint(80,700)
            enemyY[i]=random.randint(50,350)
        enemy(enemyX[i],enemyY[i],i)
    if bullet_stat == "fired":
        bullet1(bulletX+16,bulletY)
        bulletY-=bychange
    if bulletY<=0:
        bullet_stat="ready"
        bulletY=playerY+10
    player()
    show_score()
    pygame.display.update()
pygame.quit()
    
