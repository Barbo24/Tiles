import numpy
import json
import os.path

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

def seed():
    with open("saves/chunkx.json", "r") as chunk:
        chunkx_data = chunk.read()
        chunkx = json.loads(chunkx_data)
    with open("saves/chunky.json", "r") as chunk:
        chunky_data = chunk.read()
        chunky = json.loads(chunky_data)       
    userseed = 69
    temp = '{}{}{}'.format(chunkx, chunky, userseed)
    temp_hash = hash(temp)
    seed = temp_hash & 0xFFFFFFFF
    return seed