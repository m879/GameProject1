import pygame
import random
import math
from pygame import mixer
x=pygame.init()
gamewindow=pygame.display.set_mode((1300,650))
pygame.display.set_caption("SHOOTING GAME:BY--MERAJ AHMED")
mixer.music.load("music.mp3")
mixer.music.play(-1)

backimg=pygame.image.load("mback.png")
backimgX=0
backimgY=20
#backimg2=pygame.image.load("meraj.png")

back1=pygame.image.load("meraj0.png")
img1X=0
img1Y=-55
img1X_change=-6
def img1(x,y):
    gamewindow.blit(back1,(x,y))
back2=pygame.image.load("meraj12.png")
img2X=1190
img2Y=0
img2X_change=-6
def img2(x,y):
    gamewindow.blit(back2,(x,y))
back3=pygame.image.load("meraj2.png")
img3X=2490
img3Y=10
img3X_change=-6
def img3(x,y):
    gamewindow.blit(back3,(x,y))
back4=pygame.image.load("meraj3.png")
img4X=3790
img4Y=-5
img4X_change=-6
def img4(x,y):
    gamewindow.blit(back4,(x,y))

birdimg=pygame.image.load("helicopter.png")
birdX=200
birdY=-50
birdX_change=4
def bird(x,y):
    gamewindow.blit(birdimg,(x,y))
bullimg=pygame.image.load("bullet4.png")
bullX=birdX+70   
bullY=birdY+95
bullY_change=8
bullX_change=4
def helibullet(x,y):
    gamewindow.blit(bullimg,(x,y))       

carimg=pygame.image.load("car.png")
carX=0
carY=220
carX_change=2
carY_change=0
def car(x,y):
    gamewindow.blit(carimg,(x,y))


overimg=pygame.image.load("over.png")
overX=1160
overY=0
def over(x,y):
    backimg.blit(overimg,(x,y))    

shooterimg=pygame.image.load("shooter.png")
shooterX=carX+40
shooterY=carY-80
shooterX_change=2
shooterY_change=0
def shooter(x,y):
    gamewindow.blit(shooterimg,(x,y))        

bulletimg=pygame.image.load("BULLET2.png")
bulletX=shooterX
bulletY=shooterY-1000
bulletX_change=60
bulletY_change=0
bullet_state="ready"
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    gamewindow.blit(bulletimg,(x+100,y+10))

 
#ENEMY
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=3
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("birdm.png"))
    enemyX.append(random.randint(400,1200))
    enemyY.append(random.randint(50,100))
    enemyX_change.append(4)
    enemyY_change.append(10)
def enemy(x,y,i):
    gamewindow.blit(enemyimg[i],(x,y)) 



def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<50:
        return True
    else:
        return False 


def overcollision(enemyX,enemyY,shooterX,shooterY):
    distance=math.sqrt((math.pow(enemyX-shooterX,2))+(math.pow(enemyY-shooterY,2)))
    if distance<50:
        return True
    else:
        return False 

def secondcollision(bullX,bullY,shooterX,shooterY):
    distance=math.sqrt((math.pow(bullX-shooterX,2))+(math.pow(bullY-shooterY,2)))
    if distance<50:
        return True
    else:
        return False         



#score
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=500
def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(0,0,0))
    gamewindow.blit(score,(x,y))

game_exit=False
while not game_exit:
    gamewindow.blit(backimg,(backimgX,backimgY))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit=True

        if event.type==pygame.KEYDOWN:    
            if event.key==pygame.K_UP:
                shooterY_change=-4
            if event.key==pygame.K_DOWN:
                shooterY_change=4 
            if event.key==pygame.K_LEFT:
                shooterX_change=-8
                carX_change=-8
            if event.key==pygame.K_RIGHT:
                shooterX_change=8     
                carX_change=8     

            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":   
                    bulletY=shooterY
                    fire_bullet(bulletX,bulletY)

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playerY_change=0          
                


    img1X+=img1X_change
    img1(img1X,img1Y)
    img2X+=img2X_change
    img2(img2X,img2Y)
    img3X+=img3X_change
    img3(img3X,img3Y)
    img4X+=img4X_change
    img4(img4X,img4Y)

    birdX+=birdX_change
    if birdX>=1200:
        birdX=0
    bird(birdX,birdY)

    carX+=carX_change
    shooterX+=shooterX_change
    shooterY+=shooterY_change
    if carX>=1200:
        carX=0
    if shooterX>=1200:
        shooterX=carX+40 
    if shooterY>=carY-80:
        shooterY_change=0
    if shooterY<=80:
        shooterY_change=0        
    car(carX,carY)
    shooter(shooterX,shooterY)

     #ENEMY MOVEMENT
    for i in range(num_of_enemies):
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]>=0:
            enemyX_change[i]=-6 
        if enemyX[i]<=0:
            enemyX[i]=1200
 
        #COLLISION
        collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=560
            bullet_state="ready"
            score_value+=10
            enemyX[i]=random.randint(700,1200)
            enemyY[i]=random.randint(50,100)
        
        collisions=overcollision(enemyX[i],enemyY[i],shooterX,shooterY)
        if collisions:
            game_exit=True
        
        enemy(enemyX[i],enemyY[i],i)

    seccollision=secondcollision(bullX,bullY,shooterX,shooterY)
    if seccollision:
        game_exit=True

    bullY+=bullY_change
    bullX+=bullX_change
    if bullY>=300:
        bullY=birdY+95
    if bullX>=1150:
        bullX=birdX+70 
    helibullet(bullX,bullY) 

    #BULLET MOVEMENT
    if bulletX>=1200:
        bulletX=shooterX
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletX+=bulletX_change


    show_score(textX,textY)
    over(overX,overY)
    pygame.display.update()        

pygame.quit()
quit()            
