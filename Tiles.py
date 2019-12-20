import numpy
import json
import pygame
import seed
import forest_biome
import os.path

pygame.init()
pygame.font.init()

winx = 800
winy = 580

win = pygame.display.set_mode((winx,winy))
pygame.display.set_caption('Tiles')

#COLORS
white = (255, 255, 255) 
green = (11, 102, 35)
blue = (0, 0, 128) 
black = (0, 0, 0)
gray = (105, 105, 105)
background = black

#PLAYER
playerposx = winx/2-16
playerposy = winy/2-16
playervel = 1

#HUD
hudheight = 100
borderthicknes = 5

#FONTS
arial = pygame.font.SysFont("Arial", 16)
square = pygame.font.Font("fonts/square.ttf", 16)
commodore = pygame.font.Font("fonts/commodore.ttf", 16)
monofont = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 16)

#TILES
player = monofont.render('@', True, white, green)
tree = pygame.image.load("sprites/tree.png")

#HEALTH
HP = 100
healthfull = square.render('[//////////]', True, white, gray)
health9 = square.render('[///////// ]', True, white, gray)
health8 = square.render('[////////  ]', True, white, gray)
health7 = square.render('[///////   ]', True, white, gray)
health6 = square.render('[//////    ]', True, white, gray)
health5 = square.render('[/////     ]', True, white, gray)
health4 = square.render('[////      ]', True, white, gray)
health3 = square.render('[///       ]', True, white, gray)
health2 = square.render('[//        ]', True, white, gray)
health1 = square.render('[/         ]', True, white, gray)
health0 = square.render('[          ]', True, white, gray)
healthpercentage = commodore.render(str(HP) + "HP", True, white, gray)
healthposx = borderthicknes + 5
healthposy = winy - hudheight + borderthicknes + 10
healthpos = (healthposx, healthposy)
healthpercentagex = healthposx + 200
healthpercentagey = healthposy - 2
healthpercentagepos = (healthpercentagex, healthpercentagey)

#GENERATE
generation = True
if os.path.isfile('save.py'):
    save = open("save.py")
    trees2 = json.loads(save.read())
else:
    trees2 = forest_biome.generateTrees()
    save = open("save.py", "w")
    save.write(json.dumps(trees2))
    save.close()

run = True
while run:
    win.fill((background))
    pygame.time.delay(8)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
			
    keys = pygame.key.get_pressed()
	
    #MOVEMENT
    if keys[pygame.K_w]: playerposy -= playervel
    if keys[pygame.K_s]: playerposy += playervel
    if keys[pygame.K_a]: playerposx -= playervel
    if keys[pygame.K_d]: playerposx += playervel
    playerpos = (playerposx, playerposy)
	
    #HUD
    hud = pygame.Rect(0, winy - hudheight, winx, winy)
    hudborderup = pygame.Rect(0, winy - hudheight, winx, borderthicknes)
    hudborderleft = pygame.Rect(0, winy - hudheight, borderthicknes, hudheight)
    hudborderright = pygame.Rect(winx, winy - hudheight, - borderthicknes, hudheight)
    hudborderdown = pygame.Rect(0, winy, winx, - borderthicknes)
    pygame.draw.rect(win, gray, hud)
    pygame.draw.rect(win, black, hudborderup)
    pygame.draw.rect(win, black, hudborderleft)
    pygame.draw.rect(win, black, hudborderright)
    pygame.draw.rect(win, black, hudborderdown)
	
	#HP
    HP = HP
    win.blit(healthpercentage, healthpercentagepos)
    if HP <= 100:
        win.blit(healthfull, healthpos)	
    if HP <= 90:
        win.blit(health9, healthpos)
    if HP <= 80:
        win.blit(health8, healthpos)
    if HP <= 70:
        win.blit(health7, healthpos)
    if HP <= 60:
        win.blit(health6, healthpos)
    if HP <= 50:
        win.blit(health5, healthpos)
    if HP <= 40:
        win.blit(health4, healthpos)
    if HP <= 30:
        win.blit(health3, healthpos)
    if HP <= 20:
        win.blit(health2, healthpos)
    if HP <= 10:
        win.blit(health1, healthpos)
    if HP <= 0:
        win.blit(health0, healthpos)
		
    #BIOMES
    biome = numpy.random.random()
    #FOREST
    forest = False
    forestchance = 1
    if(biome <= forestchance):
        forest = True
        generate = True
    if(forest):
        background = green
        for treepos in trees2:
            win.blit(tree, treepos)

    #DRAWING PLAYER
    win.blit(player, playerpos)

    pygame.display.update()	
pygame.quit()