import pygame
import lvl1lay
import hp

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
player = font.render('@', True, white, black)
wall = font.render('#', True, white, black)
rat = font.render('R', True, white, black)
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
WRectLEFT = pygame.Rect(0, 0, 16, 480)
WRectRIGHT = pygame.Rect(784, 0, 16, 480)
WRectTOP = pygame.Rect(0, 0, 800, 16)
WRectBOT = pygame.Rect(0, 464, 800, 16)
healthpos = (5, 490)
healthpercentagepos = (200, 488)
pygame.display.flip()


run = True
while run:
    win.fill((black))
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    dirUP = pygame.Rect(dirUPx, dirUPy, 16, 16)
    dirDOWN = pygame.Rect(dirDOWNx, dirDOWNy, 16, 16)
    dirRIGHT = pygame.Rect(dirRIGHTx, dirRIGHTy, 16, 16)
    dirLEFT = pygame.Rect(dirLEFTx, dirLEFTy, 16, 16)
			
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
    if hp.HPint == 0:
        hp.HPstr = "0"
    if hp.HPint == 1:
        hp.HPstr = "1"
    if hp.HPint == 2:
        hp.HPstr = "2"
    if hp.HPint == 3:
        hp.HPstr = "3"
    if hp.HPint == 4:
        hp.HPstr = "4"
    if hp.HPint == 5:
        hp.HPstr = "5"
    if hp.HPint == 6:
        hp.HPstr = "6"
    if hp.HPint == 7:
        hp.HPstr = "7"
    if hp.HPint == 8:
        hp.HPstr = "8"
    if hp.HPint == 9:
        hp.HPstr = "9"
    if hp.HPint == 10:
        hp.HPstr = "10"
    if hp.HPint == 11:
        hp.HPstr = "11"
    if hp.HPint == 12:
        hp.HPstr = "12"
    if hp.HPint == 13:
        hp.HPstr = "13"
    if hp.HPint == 14:
        hp.HPstr = "14"
    if hp.HPint == 15:
        hp.HPstr = "15"
    if hp.HPint == 16:
        hp.HPstr = "16"
    if hp.HPint == 17:
        hp.HPstr = "17"
    if hp.HPint == 18:
        hp.HPstr = "18"
    if hp.HPint == 19:
        hp.HPstr = "19"
    if hp.HPint == 20:
        hp.HPstr = "20"
    if hp.HPint == 21:
        hp.HPstr = "21"
    if hp.HPint == 22:
        hp.HPstr = "22"
    if hp.HPint == 23:
        hp.HPstr = "23"
    if hp.HPint == 24:
        hp.HPstr = "24"
    if hp.HPint == 25:
        hp.HPstr = "25"
    if hp.HPint == 26:
        hp.HPstr = "26"
    if hp.HPint == 27:
        hp.HPstr = "27"
    if hp.HPint == 28:
        hp.HPstr = "28"
    if hp.HPint == 29:
        hp.HPstr = "29"
    if hp.HPint == 30:
        hp.HPstr = "30"
    if hp.HPint == 31:
        hp.HPstr = "31"
    if hp.HPint == 32:
        hp.HPstr = "32"
    if hp.HPint == 33:
        hp.HPstr = "33"
    if hp.HPint == 34:
        hp.HPstr = "34"
    if hp.HPint == 35:
        hp.HPstr = "35"
    if hp.HPint == 36:
        hp.HPstr = "36"
    if hp.HPint == 37:
        hp.HPstr = "37"
    if hp.HPint == 38:
        hp.HPstr = "38"
    if hp.HPint == 39:
        hp.HPstr = "39"
    if hp.HPint == 40:
        hp.HPstr = "40"
    if hp.HPint == 41:
        hp.HPstr = "41"
    if hp.HPint == 42:
        hp.HPstr = "42"
    if hp.HPint == 43:
        hp.HPstr = "43"
    if hp.HPint == 44:
        hp.HPstr = "44"
    if hp.HPint == 45:
        hp.HPstr = "45"
    if hp.HPint == 46:
        hp.HPstr = "46"
    if hp.HPint == 47:
        hp.HPstr = "47"
    if hp.HPint == 48:
        hp.HPstr = "48"
    if hp.HPint == 49:
        hp.HPstr = "49"
    if hp.HPint == 50:
        hp.HPstr = "50"
    if hp.HPint == 51:
        hp.HPstr = "51"
    if hp.HPint == 52:
        hp.HPstr = "52"
    if hp.HPint == 53:
        hp.HPstr = "53"
    if hp.HPint == 54:
        hp.HPstr = "54"
    if hp.HPint == 55:
        hp.HPstr = "55"
    if hp.HPint == 56:
        hp.HPstr = "56"
    if hp.HPint == 57:
        hp.HPstr = "57"
    if hp.HPint == 58:
        hp.HPstr = "58"
    if hp.HPint == 59:
        hp.HPstr = "59"
    if hp.HPint == 60:
        hp.HPstr = "60"
    if hp.HPint == 61:
        hp.HPstr = "61"
    if hp.HPint == 62:
        hp.HPstr = "62"
    if hp.HPint == 63:
        hp.HPstr = "63"
    if hp.HPint == 64:
        hp.HPstr = "64"
    if hp.HPint == 65:
        hp.HPstr = "65"
    if hp.HPint == 66:
        hp.HPstr = "66"
    if hp.HPint == 67:
        hp.HPstr = "67"
    if hp.HPint == 68:
        hp.HPstr = "68"
    if hp.HPint == 69:
        hp.HPstr = "69"
    if hp.HPint == 70:
        hp.HPstr = "70"
    if hp.HPint == 71:
        hp.HPstr = "71"
    if hp.HPint == 72:
        hp.HPstr = "72"
    if hp.HPint == 73:
        hp.HPstr = "73"
    if hp.HPint == 74:
        hp.HPstr = "74"
    if hp.HPint == 75:
        hp.HPstr = "75"
    if hp.HPint == 76:
        hp.HPstr = "76"
    if hp.HPint == 77:
        hp.HPstr = "77"
    if hp.HPint == 78:
        hp.HPstr = "78"
    if hp.HPint == 79:
        hp.HPstr = "79"
    if hp.HPint == 80:
        hp.HPstr = "80"
    if hp.HPint == 81:
        hp.HPstr = "81"
    if hp.HPint == 82:
        hp.HPstr = "82"
    if hp.HPint == 83:
        hp.HPstr = "83"
    if hp.HPint == 84:
        hp.HPstr = "84"
    if hp.HPint == 85:
        hp.HPstr = "85"
    if hp.HPint == 86:
        hp.HPstr = "86"
    if hp.HPint == 87:
        hp.HPstr = "87"
    if hp.HPint == 88:
        hp.HPstr = "88"
    if hp.HPint == 89:
        hp.HPstr = "89"
    if hp.HPint == 90:
        hp.HPstr = "90"
    if hp.HPint == 91:
        hp.HPstr = "91"
    if hp.HPint == 92:
        hp.HPstr = "92"
    if hp.HPint == 93:
        hp.HPstr = "93"
    if hp.HPint == 94:
        hp.HPstr = "94"
    if hp.HPint == 95:
        hp.HPstr = "95"
    if hp.HPint == 96:
        hp.HPstr = "96"
    if hp.HPint == 97:
        hp.HPstr = "97"
    if hp.HPint == 98:
        hp.HPstr = "98"
    if hp.HPint == 99:
        hp.HPstr = "99"
    if hp.HPint == 100:
        hp.HPstr = "100"

    if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
        hp.HPint -= 1
        print(hp.HPint)

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

    #LVL1
    pygame.draw.rect(win, green, WRectLEFT)
    pygame.draw.rect(win, green, WRectTOP)
    pygame.draw.rect(win, green, WRectRIGHT)
    pygame.draw.rect(win, green, WRectBOT)
	
    win.blit(entrance, lvl1lay.entrance1)
	
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