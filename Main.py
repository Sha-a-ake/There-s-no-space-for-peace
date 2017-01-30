import pygame, sys, Gen, Func, random
from pygame.locals import *
from Const import *

def Draw():
    x = TileSize; y = TileSize
    for Line in MAP:
        x = 0
        y += TileSize
        for X in Line:
            x += TileSize
            if X[0] == 1: DISPLAY.blit(Tile, (x,y))
            elif X[0] == 2: DISPLAY.blit(WallHor, (x,y))
            elif X[0] == 3: DISPLAY.blit(WallVer, (x,y))
                
def DrawSquare(X1,Y1,X2,Y2):
    x = X1*24; y = Y1*24
    for Line in range(abs(X2-X1+1)):
        x = X1*24
        y += TileSize
        for X in range(abs(Y2-Y1+1)):
            x += TileSize
            DISP.blit(Tile, (x,y))
    
def DrawHumie():
    DISPLAY.blit(Humie,(HumieX*24,HumieY*24))

def RefreshMap():
    global MAP
    
pygame.init()
pygame.display.set_caption('I LIKE TO MOVE IT MOVE IT')

MAP = Gen.Create_Map(20,16)
#Draw(); 

DrawHumie()


t = 1
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Humie = HumieRight
                if MAP[HumieX+1][HumieY][2] == True:
                    HumieX += 1
                    
            if event.key == pygame.K_LEFT:
                Humie = HumieLeft
                if MAP[HumieX-1][HumieY][2] == True:
                    HumieX -= 1
                    
            if event.key == pygame.K_UP:
                Humie = HumieUp
                if MAP[HumieX][HumieY-1][2] == True:
                    HumieY -= 1
                    
            if event.key == pygame.K_DOWN:
                Humie = HumieDown
                if MAP[HumieX][HumieY+1][2] == True:
                    HumieY += 1
                    
                
            DISPLAY.fill(BLACK) 
            t += 1
            
            Draw() 
            DrawHumie()
            MAP[7][7] = [1,1,False,False,False]
            DISPLAY.blit(WallSpVer,(7*24,7*24))
            print(HumieX,HumieY-1)
            RefreshMap()
            
            
    pygame.display.update()
    FpsClock.tick(FPS)        
