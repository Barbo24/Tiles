import numpy
import seed 
import json
import os.path

treespawnchance = 0.01
lakechance = 0.001

def generateTrees():
    tilex = 0
    tiley = 0
    treepos = []
    global treespawnchance
    numpy.random.seed(seed.seed())
    for tiles in range(0,1500):
        tilevalue = numpy.random.random()
        if(tilevalue < treespawnchance):
            treepos.append((tilex, tiley))    
        if(tilex < 800):
            tilex += 16
        if(tilex == 800):
            tilex = 0
            tiley += 16
    return treepos
    
def generateLakes():
    tilex = 0
    tiley = 0
    laketiles = []
    global lakechance
    numpy.random.seed(seed.seed())
    for tiles in range(0,1500):
        tilevalue = numpy.random.random()
        if(tilevalue < lakechance):
            lakex = numpy.random.randint(-10, 10)
            lakey = numpy.random.randint(-10, 10)
            for lake in range(0, abs(lakex)):
                laketiles.append((tilex, tiley))
                for lake1 in range(0,abs(lakey)):
                    laketiles.append((tilex, tiley + 16 * lake1))
                tilex += 16
        if(tilex < 800):
            tilex += 16
        if(tilex == 800):
            tilex = 0
            tiley += 16
    return laketiles