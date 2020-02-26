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

    if(chunkx < 0): chunkx = -2 * chunkx - 1
    else: chunkx *= 2
    if(chunky < 0): chunky = -2 * chunky - 1
    else: chunky *= 2   
    userseed = 10010
    seed = (chunkx * userseed) + (chunky * userseed) + userseed
    return seed
