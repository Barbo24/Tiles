import pygame
import lvl1lay
import hp
from random import *
import enemypos

pygame.init()
pygame.font.init()

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0, 0, 0)

playerposx = 64
playerposy = 64
playervelx = 16
playervely = 16
playerpos = (playerposx, playerposy)

dirUPx = playerposx
dirUPy = playerposy-16
dirDOWNx = playerposx
dirDOWNy = playerposy+16
dirRIGHTx = playerposx+16
dirRIGHTy = playerposy
dirLEFTx = playerposx-16
dirLEFTy = playerposy


win = pygame.display.set_mode((800,550))

pygame.display.flip()
pygame.display.set_caption('Tiles')
font = pygame.font.Font("square.ttf", 16)
fontcommodore = pygame.font.Font("commodore.ttf", 16)
fontgreek = pygame.font.SysFont("timesnewroman", 18)
player = fontcommodore.render('@', True, white, black)
wall = font.render('#', True, white, black)
entrance = fontgreek.render('Ω', True, white, black)
healthfull = font.render('[//////////]', True, white, black)
health9 = font.render('[///////// ]', True, white, black)
health8 = font.render('[////////  ]', True, white, black)
health7 = font.render('[///////   ]', True, white, black)
health6 = font.render('[//////    ]', True, white, black)
health5 = font.render('[/////     ]', True, white, black)
health4 = font.render('[////      ]', True, white, black)
health3 = font.render('[///       ]', True, white, black)
health2 = font.render('[//        ]', True, white, black)
health1 = font.render('[/         ]', True, white, black)
health0 = font.render('[          ]', True, white, black)
healthpos = (5, 490)
healthpercentagepos = (200, 488)
lvl1 = False
pygame.display.flip()

run = True
while run:
    win.fill((black))
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #DIRECTION BLOCKS
    dirUP = pygame.Rect(dirUPx, dirUPy, 16, 16)
    dirDOWN = pygame.Rect(dirDOWNx, dirDOWNy, 16, 16)
    dirRIGHT = pygame.Rect(dirRIGHTx, dirRIGHTy, 16, 16)
    dirLEFT = pygame.Rect(dirLEFTx, dirLEFTy, 16, 16)
	
	#WALLS IN EVERY LEVEL
    WRectLEFT = pygame.Rect(0, 0, 16, 480)
    WRectRIGHT = pygame.Rect(784, 0, 16, 480)
    WRectTOP = pygame.Rect(0, 0, 800, 16)
    WRectBOT = pygame.Rect(0, 464, 800, 16)
	
    keys = pygame.key.get_pressed()
	
	#HP
    hp.HPstr = str(hp.HPint)
    healthpercentage = fontcommodore.render(hp.HPstr + "HP", True, white, black)
    win.blit(healthpercentage, healthpercentagepos)

    if hp.HPint <= 100:
        win.blit(healthfull, healthpos)	
    if hp.HPint <= 90:
        win.blit(health9, healthpos)
    if hp.HPint <= 80:
        win.blit(health8, healthpos)
    if hp.HPint <= 70:
        win.blit(health7, healthpos)
    if hp.HPint <= 60:
        win.blit(health6, healthpos)
    if hp.HPint <= 50:
        win.blit(health5, healthpos)
    if hp.HPint <= 40:
        win.blit(health4, healthpos)
    if hp.HPint <= 30:
        win.blit(health3, healthpos)
    if hp.HPint <= 20:
        win.blit(health2, healthpos)
    if hp.HPint <= 10:
        win.blit(health1, healthpos)
    if hp.HPint <= 0:
        win.blit(health0, healthpos)
		
    #ENEMIES
    if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
        emovement = randint(1, 4) #1UP, 2DOWN, 3LEFT, 4RIGHT
        print(emovement)
    #RAT
    rat = fontcommodore.render('R', True, white, black)
    ratvel = 16
    ratdmg = randint(1, 3)
    rathitchance = (1, 2)
    rathitchancetoplayer = randint(1, 2)
    ratHP = 7
	

    ratUP = pygame.Rect(enemypos.ratposx, enemypos.ratposy-16, 16, 16)
    ratDOWN = pygame.Rect(enemypos.ratposx, enemypos.ratposy+16, 16, 16)
    ratRIGHT = pygame.Rect(enemypos.ratposx+16, enemypos.ratposy, 16, 16)
    ratLEFT = pygame.Rect(enemypos.ratposx-16, enemypos.ratposy, 16, 16)

    if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
        if emovement == 1:
            if ratUP.colliderect(WRectTOP):
                pass
            else:
                enemypos.ratposy -= ratvel
        if emovement == 2:
            if ratDOWN.colliderect(WRectBOT):
                pass
            else:
                enemypos.ratposy += ratvel
        if emovement == 3:
            if ratLEFT.colliderect(WRectLEFT):
                pass
            else: 
                enemypos.ratposx -= ratvel
        if emovement == 4:
            if ratRIGHT.colliderect(WRectRIGHT):
                pass
            else:
                enemypos.ratposx += ratvel
        enemypos.ratpos = (enemypos.ratposx, enemypos.ratposy)

    lvl1 = True

    #LVL1
    if lvl1:
        
        win.blit(entrance, lvl1lay.entrance1)
        
        win.blit(rat, enemypos.ratpos)
		
        win.blit(wall, lvl1lay.wallLEFT0)
        win.blit(wall, lvl1lay.wallLEFT1)
        win.blit(wall, lvl1lay.wallLEFT2)
        win.blit(wall, lvl1lay.wallLEFT3)
        win.blit(wall, lvl1lay.wallLEFT4)
        win.blit(wall, lvl1lay.wallLEFT5)
        win.blit(wall, lvl1lay.wallLEFT6)
        win.blit(wall, lvl1lay.wallLEFT7)
        win.blit(wall, lvl1lay.wallLEFT8)
        win.blit(wall, lvl1lay.wallLEFT9)
        win.blit(wall, lvl1lay.wallLEFT10)
        win.blit(wall, lvl1lay.wallLEFT11)
        win.blit(wall, lvl1lay.wallLEFT12)
        win.blit(wall, lvl1lay.wallLEFT13)
        win.blit(wall, lvl1lay.wallLEFT14)
        win.blit(wall, lvl1lay.wallLEFT15)
        win.blit(wall, lvl1lay.wallLEFT16)
        win.blit(wall, lvl1lay.wallLEFT17)
        win.blit(wall, lvl1lay.wallLEFT18)
        win.blit(wall, lvl1lay.wallLEFT19)
        win.blit(wall, lvl1lay.wallLEFT20)
        win.blit(wall, lvl1lay.wallLEFT21)
        win.blit(wall, lvl1lay.wallLEFT22)
        win.blit(wall, lvl1lay.wallLEFT23)
        win.blit(wall, lvl1lay.wallLEFT24)
        win.blit(wall, lvl1lay.wallLEFT25)
        win.blit(wall, lvl1lay.wallLEFT26)
        win.blit(wall, lvl1lay.wallLEFT27)
        win.blit(wall, lvl1lay.wallLEFT28)
        win.blit(wall, lvl1lay.wallLEFT29)
        win.blit(wall, lvl1lay.wallTOP0)
        win.blit(wall, lvl1lay.wallTOP1)
        win.blit(wall, lvl1lay.wallTOP2)
        win.blit(wall, lvl1lay.wallTOP3)
        win.blit(wall, lvl1lay.wallTOP4)
        win.blit(wall, lvl1lay.wallTOP5)
        win.blit(wall, lvl1lay.wallTOP6)
        win.blit(wall, lvl1lay.wallTOP7)
        win.blit(wall, lvl1lay.wallTOP8)
        win.blit(wall, lvl1lay.wallTOP9)
        win.blit(wall, lvl1lay.wallTOP10)
        win.blit(wall, lvl1lay.wallTOP11)
        win.blit(wall, lvl1lay.wallTOP12)
        win.blit(wall, lvl1lay.wallTOP13)
        win.blit(wall, lvl1lay.wallTOP14)
        win.blit(wall, lvl1lay.wallTOP15)
        win.blit(wall, lvl1lay.wallTOP16)
        win.blit(wall, lvl1lay.wallTOP17)
        win.blit(wall, lvl1lay.wallTOP18)
        win.blit(wall, lvl1lay.wallTOP19)
        win.blit(wall, lvl1lay.wallTOP20)
        win.blit(wall, lvl1lay.wallTOP21)
        win.blit(wall, lvl1lay.wallTOP22)
        win.blit(wall, lvl1lay.wallTOP23)
        win.blit(wall, lvl1lay.wallTOP24)
        win.blit(wall, lvl1lay.wallTOP25)
        win.blit(wall, lvl1lay.wallTOP26)
        win.blit(wall, lvl1lay.wallTOP27)
        win.blit(wall, lvl1lay.wallTOP28)
        win.blit(wall, lvl1lay.wallTOP29)
        win.blit(wall, lvl1lay.wallTOP30)
        win.blit(wall, lvl1lay.wallTOP31)
        win.blit(wall, lvl1lay.wallTOP32)
        win.blit(wall, lvl1lay.wallTOP33)
        win.blit(wall, lvl1lay.wallTOP34)
        win.blit(wall, lvl1lay.wallTOP35)
        win.blit(wall, lvl1lay.wallTOP36)
        win.blit(wall, lvl1lay.wallTOP37)
        win.blit(wall, lvl1lay.wallTOP38)
        win.blit(wall, lvl1lay.wallTOP39)
        win.blit(wall, lvl1lay.wallTOP40)
        win.blit(wall, lvl1lay.wallTOP41)
        win.blit(wall, lvl1lay.wallTOP42)
        win.blit(wall, lvl1lay.wallTOP43)
        win.blit(wall, lvl1lay.wallTOP44)
        win.blit(wall, lvl1lay.wallTOP45)
        win.blit(wall, lvl1lay.wallTOP46)
        win.blit(wall, lvl1lay.wallTOP47)
        win.blit(wall, lvl1lay.wallTOP48)
        win.blit(wall, lvl1lay.wallTOP49)
        win.blit(wall, lvl1lay.wallRIGHT0)
        win.blit(wall, lvl1lay.wallRIGHT1)
        win.blit(wall, lvl1lay.wallRIGHT2)
        win.blit(wall, lvl1lay.wallRIGHT3)
        win.blit(wall, lvl1lay.wallRIGHT4)
        win.blit(wall, lvl1lay.wallRIGHT5)
        win.blit(wall, lvl1lay.wallRIGHT6)
        win.blit(wall, lvl1lay.wallRIGHT7)
        win.blit(wall, lvl1lay.wallRIGHT8)
        win.blit(wall, lvl1lay.wallRIGHT9)
        win.blit(wall, lvl1lay.wallRIGHT10)
        win.blit(wall, lvl1lay.wallRIGHT11)
        win.blit(wall, lvl1lay.wallRIGHT12)
        win.blit(wall, lvl1lay.wallRIGHT13)
        win.blit(wall, lvl1lay.wallRIGHT14)
        win.blit(wall, lvl1lay.wallRIGHT15)
        win.blit(wall, lvl1lay.wallRIGHT16)
        win.blit(wall, lvl1lay.wallRIGHT17)
        win.blit(wall, lvl1lay.wallRIGHT18)
        win.blit(wall, lvl1lay.wallRIGHT19)
        win.blit(wall, lvl1lay.wallRIGHT20)
        win.blit(wall, lvl1lay.wallRIGHT21)
        win.blit(wall, lvl1lay.wallRIGHT22)
        win.blit(wall, lvl1lay.wallRIGHT23)
        win.blit(wall, lvl1lay.wallRIGHT24)
        win.blit(wall, lvl1lay.wallRIGHT25)
        win.blit(wall, lvl1lay.wallRIGHT26)
        win.blit(wall, lvl1lay.wallRIGHT27)
        win.blit(wall, lvl1lay.wallRIGHT28)
        win.blit(wall, lvl1lay.wallRIGHT29)
        win.blit(wall, lvl1lay.wallBOT0)
        win.blit(wall, lvl1lay.wallBOT1)
        win.blit(wall, lvl1lay.wallBOT2)
        win.blit(wall, lvl1lay.wallBOT3)
        win.blit(wall, lvl1lay.wallBOT4)
        win.blit(wall, lvl1lay.wallBOT5)
        win.blit(wall, lvl1lay.wallBOT6)
        win.blit(wall, lvl1lay.wallBOT7)
        win.blit(wall, lvl1lay.wallBOT8)
        win.blit(wall, lvl1lay.wallBOT9)
        win.blit(wall, lvl1lay.wallBOT10)
        win.blit(wall, lvl1lay.wallBOT11)
        win.blit(wall, lvl1lay.wallBOT12)
        win.blit(wall, lvl1lay.wallBOT13)
        win.blit(wall, lvl1lay.wallBOT14)
        win.blit(wall, lvl1lay.wallBOT15)
        win.blit(wall, lvl1lay.wallBOT16)
        win.blit(wall, lvl1lay.wallBOT17)
        win.blit(wall, lvl1lay.wallBOT18)
        win.blit(wall, lvl1lay.wallBOT19)
        win.blit(wall, lvl1lay.wallBOT20)
        win.blit(wall, lvl1lay.wallBOT21)
        win.blit(wall, lvl1lay.wallBOT22)
        win.blit(wall, lvl1lay.wallBOT23)
        win.blit(wall, lvl1lay.wallBOT24)
        win.blit(wall, lvl1lay.wallBOT25)
        win.blit(wall, lvl1lay.wallBOT26)
        win.blit(wall, lvl1lay.wallBOT27)
        win.blit(wall, lvl1lay.wallBOT28)
        win.blit(wall, lvl1lay.wallBOT29)
        win.blit(wall, lvl1lay.wallBOT30)
        win.blit(wall, lvl1lay.wallBOT31)
        win.blit(wall, lvl1lay.wallBOT32)
        win.blit(wall, lvl1lay.wallBOT33)
        win.blit(wall, lvl1lay.wallBOT34)
        win.blit(wall, lvl1lay.wallBOT35)
        win.blit(wall, lvl1lay.wallBOT36)
        win.blit(wall, lvl1lay.wallBOT37)
        win.blit(wall, lvl1lay.wallBOT38)
        win.blit(wall, lvl1lay.wallBOT39)
        win.blit(wall, lvl1lay.wallBOT40)
        win.blit(wall, lvl1lay.wallBOT41)
        win.blit(wall, lvl1lay.wallBOT42)
        win.blit(wall, lvl1lay.wallBOT43)
        win.blit(wall, lvl1lay.wallBOT44)
        win.blit(wall, lvl1lay.wallBOT45)
        win.blit(wall, lvl1lay.wallBOT46)
        win.blit(wall, lvl1lay.wallBOT47)
        win.blit(wall, lvl1lay.wallBOT48)
        win.blit(wall, lvl1lay.wallBOT49)	
    #END OF LVL1
	
    if dirLEFT.colliderect(WRectLEFT):
        if keys[pygame.K_a]:
            playerposx = playerposx
            dirRIGHTx = dirRIGHTx
            dirLEFTx = dirLEFTx
            dirUPx = dirUPx
            dirDOWNx = dirDOWNx
            print("you can't go there")
			
    elif keys[pygame.K_a]:
        playerposx -= playervelx
        dirLEFTx -= playervelx
        dirRIGHTx -= playervelx
        dirUPx -= playervelx
        dirDOWNx -= playervelx
        print("LEFT")
		
    if dirRIGHT.colliderect(WRectRIGHT):
        if keys[pygame.K_d]:
            playerposx = playerposx
            dirRIGHTx = dirRIGHTx
            dirLEFTx = dirLEFTx
            dirUPx = dirUPx
            dirDOWNx = dirDOWNx
            print("you can't go there")
		 	
    elif keys[pygame.K_d]:
        playerposx += playervelx
        dirRIGHTx += playervelx
        dirLEFTx += playervelx
        dirUPx += playervelx
        dirDOWNx += playervelx
        print("RIGHT")

    if dirUP.colliderect(WRectTOP):
        if keys[pygame.K_w]:
            playerposy = playerposy
            dirUPy = dirUPy
            dirDOWNy = dirDOWNy
            dirLEFTy = dirLEFTy
            dirRIGHTy = dirRIGHTy
            print("you can't go there")
	
    elif keys[pygame.K_w]:
        playerposy -= playervely
        dirUPy -= playervely
        dirDOWNy -= playervely
        dirLEFTy -= playervely
        dirRIGHTy -= playervely
        print("UP")

    if dirDOWN.colliderect(WRectBOT):
        if keys[pygame.K_s]:
            playerposy = playerposy
            dirDOWNy = dirDOWNy
            dirUPy = dirUPy
            dirLEFTy = dirLEFTy
            dirRIGHTy = dirRIGHTy
            print("you can't go there")
    elif keys[pygame.K_s]:
            playerposy += playervely
            dirDOWNy += playervely
            dirUPy += playervely
            dirLEFTy += playervely
            dirRIGHTy += playervely
            print("DOWN")
	
    win.blit(player, playerpos)
    playerpos = (playerposx, playerposy)

    pygame.display.update()	
pygame.quit()