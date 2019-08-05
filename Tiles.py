import sys, pygame
import lvl1lay

pygame.init()
pygame.font.init()

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0, 0, 0)

playerposx = 260
playerposy = 256
playervelx = 13
playervely = 16
playerpos = (playerposx, playerposy)

dirUPx = playerposx
dirUPy = playerposy-16
dirDOWNx = playerposx
dirDOWNy = playerposy+16
dirRIGHTx = playerposx+13
dirRIGHTy = playerposy
dirLEFTx = playerposx-13
dirLEFTy = playerposy


win = pygame.display.set_mode((650,480))

pygame.display.flip()
pygame.display.set_caption('Tiles')
font = pygame.font.Font("commodore.ttf", 16)
player = font.render('@', True, white, black)
wall = font.render('#', True, white, black)
pygame.display.flip()

run = True
while run:
    win.fill((black))
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    dirUP = pygame.Rect(dirUPx, dirUPy, 13, 16)
    dirDOWN = pygame.Rect(dirDOWNx, dirDOWNy, 13, 16)
    dirRIGHT = pygame.Rect(dirRIGHTx, dirRIGHTy, 13, 16)
    dirLEFT = pygame.Rect(dirLEFTx, dirLEFTy, 13, 16)
    #Air = pygame.Rect(13, 16, 624, 448)
    Air = pygame.Rect(0, 0, 650, 480)
    WRect = pygame.Rect(0, 0, 13, 480)
    PRect = pygame.Rect(playerposx, playerposy, 13, 16)
			
    keys = pygame.key.get_pressed()
	
    if dirLEFT.colliderect(Air):
        if keys[pygame.K_a]:
            playerposx -= playervelx
            dirLEFTx -= playervelx
            dirRIGHTx -= playervelx
            dirUPx -= playervelx
            dirDOWNx -= playervelx
            print("LEFT")
    if dirRIGHT.colliderect(Air):
        if keys[pygame.K_d]:
            playerposx += playervelx
            dirRIGHTx += playervelx
            dirLEFTx += playervelx
            dirUPx += playervelx
            dirDOWNx += playervelx
            print("RIGHT")
    if dirUP.colliderect(Air):
        if keys[pygame.K_w]:
            playerposy -= playervely
            dirUPy -= playervely
            dirDOWNy -= playervely
            dirLEFTy -= playervely
            dirRIGHTy -= playervely
            print("UP")
    if dirDOWN.colliderect(Air):
        if keys[pygame.K_s]:
            playerposy += playervely
            dirDOWNy += playervely
            dirUPy += playervely
            dirLEFTy += playervely
            dirRIGHTy += playervely
            print("DOWN")
			

    #LVL1
    #pygame.draw.rect(win, green, WRect)
    pygame.draw.rect(win, green, PRect)
    pygame.draw.rect(win, blue, Air)
    win.blit(wall, lvl1lay.wall0)
    win.blit(wall, lvl1lay.wall1)
    win.blit(wall, lvl1lay.wall2)
    win.blit(wall, lvl1lay.wall3)
    win.blit(wall, lvl1lay.wall4)
    win.blit(wall, lvl1lay.wall5)
    win.blit(wall, lvl1lay.wall6)	
	#END OF LVL1
	
    pygame.draw.rect(win, white, dirUP)
    pygame.draw.rect(win, white, dirDOWN)
    pygame.draw.rect(win, white, dirRIGHT)
    pygame.draw.rect(win, white, dirLEFT)
    win.blit(player, playerpos)
    playerpos = (playerposx, playerposy)

    pygame.display.update()	
pygame.quit()