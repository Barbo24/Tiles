import numpy
import seed 
import json
import os.path

cactusspawnchance = 0.01

def generateCacti():
    tilex = 0
    tiley = 0
    cactipos = []
    numpy.random.seed(seed.seed())
    for tiles in range(0,1500):
        tilevalue = numpy.random.random()
        if(tilevalue < cactusspawnchance):
            cactipos.append((tilex, tiley))
        if(tilex < 800):
            tilex += 16
        if(tilex == 800):
            tilex = 0
            tiley += 16
    return cactipos