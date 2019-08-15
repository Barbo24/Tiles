import pygame
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


win = pygame.display.set_mode((650,550))

pygame.display.flip()
pygame.display.set_caption('Tiles')
font = pygame.font.Font("commodore.ttf", 16)
player = font.render('@', True, white, black)
wall = font.render('#', True, white, black)
health = font.render('(//////////)', True, white, black)
healthpercentage0 = font.render( "0HP" , True, white, black)
healthpercentage1 = font.render( "1HP" , True, white, black)
healthpercentage2 = font.render( "2HP" , True, white, black)
healthpercentage3 = font.render( "3HP" , True, white, black)
healthpercentage4 = font.render( "4HP" , True, white, black)
healthpercentage5 = font.render( "5HP" , True, white, black)
healthpercentage6 = font.render( "6HP" , True, white, black)
healthpercentage7 = font.render( "7HP" , True, white, black)
healthpercentage8 = font.render( "8HP" , True, white, black)
healthpercentage9 = font.render( "9HP" , True, white, black)
healthpercentage10 = font.render( "10HP" , True, white, black)
healthpercentage11 = font.render( "11HP" , True, white, black)
healthpercentage12 = font.render( "12HP" , True, white, black)
healthpercentage13 = font.render( "13HP" , True, white, black)
healthpercentage14 = font.render( "14HP" , True, white, black)
healthpercentage15 = font.render( "15HP" , True, white, black)
healthpercentage16 = font.render( "16HP" , True, white, black)
healthpercentage17 = font.render( "17HP" , True, white, black)
healthpercentage18 = font.render( "18HP" , True, white, black)
healthpercentage19 = font.render( "19HP" , True, white, black)
healthpercentage20 = font.render( "20HP" , True, white, black)
healthpercentage21 = font.render( "21HP" , True, white, black)
healthpercentage22 = font.render( "22HP" , True, white, black)
healthpercentage23 = font.render( "23HP" , True, white, black)
healthpercentage24 = font.render( "24HP" , True, white, black)
healthpercentage25 = font.render( "25HP" , True, white, black)
healthpercentage26 = font.render( "26HP" , True, white, black)
healthpercentage27 = font.render( "27HP" , True, white, black)
healthpercentage28 = font.render( "28HP" , True, white, black)
healthpercentage29 = font.render( "29HP" , True, white, black)
healthpercentage30 = font.render( "30HP" , True, white, black)
healthpercentage31 = font.render( "31HP" , True, white, black)
healthpercentage32 = font.render( "32HP" , True, white, black)
healthpercentage33 = font.render( "33HP" , True, white, black)
healthpercentage34 = font.render( "34HP" , True, white, black)
healthpercentage35 = font.render( "35HP" , True, white, black)
healthpercentage36 = font.render( "36HP" , True, white, black)
healthpercentage37 = font.render( "37HP" , True, white, black)
healthpercentage38 = font.render( "38HP" , True, white, black)
healthpercentage39 = font.render( "39HP" , True, white, black)
healthpercentage40 = font.render( "40HP" , True, white, black)
healthpercentage41 = font.render( "41HP" , True, white, black)
healthpercentage42 = font.render( "42HP" , True, white, black)
healthpercentage43 = font.render( "43HP" , True, white, black)
healthpercentage44 = font.render( "44HP" , True, white, black)
healthpercentage45 = font.render( "45HP" , True, white, black)
healthpercentage46 = font.render( "46HP" , True, white, black)
healthpercentage47 = font.render( "47HP" , True, white, black)
healthpercentage48 = font.render( "48HP" , True, white, black)
healthpercentage49 = font.render( "49HP" , True, white, black)
healthpercentage50 = font.render( "50HP" , True, white, black)
healthpercentage51 = font.render( "51HP" , True, white, black)
healthpercentage52 = font.render( "52HP" , True, white, black)
healthpercentage53 = font.render( "53HP" , True, white, black)
healthpercentage54 = font.render( "54HP" , True, white, black)
healthpercentage55 = font.render( "55HP" , True, white, black)
healthpercentage56 = font.render( "56HP" , True, white, black)
healthpercentage57 = font.render( "57HP" , True, white, black)
healthpercentage58 = font.render( "58HP" , True, white, black)
healthpercentage59 = font.render( "59HP" , True, white, black)
healthpercentage60 = font.render( "60HP" , True, white, black)
healthpercentage61 = font.render( "61HP" , True, white, black)
healthpercentage62 = font.render( "62HP" , True, white, black)
healthpercentage63 = font.render( "63HP" , True, white, black)
healthpercentage64 = font.render( "64HP" , True, white, black)
healthpercentage65 = font.render( "65HP" , True, white, black)
healthpercentage66 = font.render( "66HP" , True, white, black)
healthpercentage67 = font.render( "67HP" , True, white, black)
healthpercentage68 = font.render( "68HP" , True, white, black)
healthpercentage69 = font.render( "69HP" , True, white, black)
healthpercentage70 = font.render( "70HP" , True, white, black)
healthpercentage71 = font.render( "71HP" , True, white, black)
healthpercentage72 = font.render( "72HP" , True, white, black)
healthpercentage73 = font.render( "73HP" , True, white, black)
healthpercentage74 = font.render( "74HP" , True, white, black)
healthpercentage75 = font.render( "75HP" , True, white, black)
healthpercentage76 = font.render( "76HP" , True, white, black)
healthpercentage77 = font.render( "77HP" , True, white, black)
healthpercentage78 = font.render( "78HP" , True, white, black)
healthpercentage79 = font.render( "79HP" , True, white, black)
healthpercentage80 = font.render( "80HP" , True, white, black)
healthpercentage81 = font.render( "81HP" , True, white, black)
healthpercentage82 = font.render( "82HP" , True, white, black)
healthpercentage83 = font.render( "83HP" , True, white, black)
healthpercentage84 = font.render( "84HP" , True, white, black)
healthpercentage85 = font.render( "85HP" , True, white, black)
healthpercentage86 = font.render( "86HP" , True, white, black)
healthpercentage87 = font.render( "87HP" , True, white, black)
healthpercentage88 = font.render( "88HP" , True, white, black)
healthpercentage89 = font.render( "89HP" , True, white, black)
healthpercentage90 = font.render( "90HP" , True, white, black)
healthpercentage91 = font.render( "91HP" , True, white, black)
healthpercentage92 = font.render( "92HP" , True, white, black)
healthpercentage93 = font.render( "93HP" , True, white, black)
healthpercentage94 = font.render( "94HP" , True, white, black)
healthpercentage95 = font.render( "95HP" , True, white, black)
healthpercentage96 = font.render( "96HP" , True, white, black)
healthpercentage97 = font.render( "97HP" , True, white, black)
healthpercentage98 = font.render( "98HP" , True, white, black)
healthpercentage99 = font.render( "99HP" , True, white, black)
healthpercentage100 = font.render( "100HP" , True, white, black)
WRectLEFT = pygame.Rect(0, 0, 13, 480)
WRectRIGHT = pygame.Rect(637, 0, 13, 480)
WRectTOP = pygame.Rect(0, 0, 650, 16)
WRectBOT = pygame.Rect(0, 464, 650, 16)
EntranceRect = pygame.Rect(0, 0, 0, 0)
healthpos = (5, 485)
healthpercentagepos = (165, 485)
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
			
    keys = pygame.key.get_pressed()
	
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
			
	#Direction blocks
    pygame.draw.rect(win, black, dirUP)
    pygame.draw.rect(win, black, dirDOWN)
    pygame.draw.rect(win, black, dirRIGHT)
    pygame.draw.rect(win, black, dirLEFT)
	
	#HP
    win.blit(health, healthpos)
    win.blit(healthpercentage100, healthpercentagepos)

    #LVL1
    pygame.draw.rect(win, green, WRectLEFT)
    pygame.draw.rect(win, green, WRectTOP)
    pygame.draw.rect(win, green, WRectRIGHT)
    pygame.draw.rect(win, green, WRectBOT)
	
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
	
    win.blit(player, playerpos)
    playerpos = (playerposx, playerposy)

    pygame.display.update()	
pygame.quit()