import numpy
import seed 
import json
import os.path

treespawnchance = 0.2

def generateTrees():
    tilex = 0
    tiley = 0
    treepos = []
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