import numpy
import json
import pygame
import forest_biome
import os.path
import random
import player_pos
import seed

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

#HUD
hudheight = 100
borderthicknes = 5

#FONTS
arial = pygame.font.SysFont("Arial", 16)
square = pygame.font.Font("fonts/square.ttf", 16)
commodore = pygame.font.Font("fonts/commodore.ttf", 16)
monofont = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 16)

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

#SPAWN POSITION
if os.path.isfile("saves/playerpos.json"):
    playerposf = open("saves/playerpos.json")
    playerpos = json.loads(playerposf.read())
    playerposx = playerpos[0]
    playerposy = playerpos[1]
else:
    playerposx = player_pos.spawnpos("x")
    playerposy = player_pos.spawnpos("y")
    playerpos = [playerposx, playerposy]
    playerposf = open("saves/playerpos.json", "w")
    playerposf.write(json.dumps(playerpos))
    playerposf.close()

generation = True
findplayerspawn = True

run = True
while run:
    win.fill((background))
    pygame.time.delay(8)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    #TILES
    player = monofont.render('@', True, white, background)
    tree = pygame.image.load("sprites/tree.png")
    
    #SPAWN POSITION - AFTER DEATH
    if(findplayerspawn):
        pass
    playerpos = [playerposx, playerposy]
    playerposf = open("saves/playerpos.json", "w")
    playerposf.write(json.dumps(playerpos))
    playerpos = (playerposx, playerposy)
    
    #PLAYER CONSTANTS
    playervelUP = 1
    playervelDOWN = 1
    playervelLEFT = 1
    playervelRIGHT = 1
    
    #DRAWING PLAYER
    win.blit(player, playerpos)
    
    #PLAYER HITBOX
    side = 1
    playerhitbox = pygame.Rect(playerposx, playerposy, 16, 16)
    playerUP = pygame.Rect(playerposx, playerposy - side, 16, side)
    playerDOWN = pygame.Rect(playerposx, playerposy + 16, 16, side)
    playerLEFT = pygame.Rect(playerposx - side, playerposy, side, 16)
    playerRIGHT = pygame.Rect(playerposx + 16, playerposy, side, 16)
    
    #WRITING/READING CHUNK POSITION
    if os.path.isfile("saves/chunkx.json"):
        chunk = open("saves/chunkx.json")
        chunkx = json.loads(chunk.read())
    else:
        chunkx = 0
        chunk = open("saves/chunkx.json", "w")
        chunk.write(json.dumps(chunkx))
        chunk.close()   
    if os.path.isfile("saves/chunky.json"):
        chunk = open("saves/chunky.json")
        chunky = json.loads(chunk.read())
    else:
        chunky = 0
        chunk = open("saves/chunky.json", "w")
        chunk.write(json.dumps(chunky))
        chunk.close()     
    chunks = (chunkx, chunky)
    
    #SEED
    numpy.random.seed(seed.seed())
    
    #GENERATE
    if os.path.isfile("saves/chunk" + str(chunks) + ".py"):
        save = open("saves/chunk" + str(chunks) + ".py")
        trees2 = json.loads(save.read())
    else:
        trees2 = forest_biome.generateTrees()
        save = open("saves/chunk" + str(chunks) + ".py", "w")
        save.write(json.dumps(trees2))
        save.close()
		
    #BIOMES
    if(generation):
        biome = numpy.random.random()
        generation = False
        #FOREST
        forestchance = 1
        if(biome <= forestchance):
            forest = True
    if(forest):
        background = green
        for treepos in trees2:
            treehitbox = pygame.Rect((treepos), (16, 16))
            win.blit(tree, treepos)
            if(playerUP.colliderect(treehitbox)): playervelUP = 0
            if(playerDOWN.colliderect(treehitbox)): playervelDOWN = 0
            if(playerLEFT.colliderect(treehitbox)): playervelLEFT = 0
            if(playerRIGHT.colliderect(treehitbox)): playervelRIGHT = 0
            
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
    if(playerDOWN.colliderect(hudborderup)): playervelDOWN = 0
    
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
        
    #CHUNK BORDERS
    chunkUP = pygame.Rect(0, 0, winx, 1)
    chunkDOWN = pygame.Rect(0, winy - hudheight - 1, winx, 1)
    chunkLEFT = pygame.Rect(0, 0, 1, winy - hudheight)
    chunkRIGHT = pygame.Rect(winx - 1, 0, 1, winy - hudheight)
    if(chunkUP.colliderect(playerUP)): 
        chunky += 1
        chunk = open("saves/chunky.json", "w")
        chunk.write(json.dumps(chunky))
        playerposy = winy - hudheight - 18
        generation = True
    if(chunkDOWN.colliderect(playerDOWN)): 
        chunky -= 1
        chunk = open("saves/chunky.json", "w")
        chunk.write(json.dumps(chunky))
        playerposy = 2
        generation = True
    if(chunkLEFT.colliderect(playerLEFT)): 
        chunkx -= 1
        chunk = open("saves/chunkx.json", "w")
        chunk.write(json.dumps(chunkx))
        playerposx = winx - 18
        generation = True
    if(chunkRIGHT.colliderect(playerRIGHT)): 
        chunkx += 1
        chunk = open("saves/chunkx.json", "w")
        chunk.write(json.dumps(chunkx))
        playerposx = 2
        generation = True
    
    #MOVEMENT
    if keys[pygame.K_w]: playerposy -= playervelUP
    if keys[pygame.K_s]: playerposy += playervelDOWN
    if keys[pygame.K_a]: playerposx -= playervelLEFT
    if keys[pygame.K_d]: playerposx += playervelRIGHT
    playerpos = (playerposx, playerposy)
    
    pygame.display.update()	
pygame.quit()