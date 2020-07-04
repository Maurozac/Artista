
import random

import numpy as np
from PIL import Image

# acerte o seu path...
PATH_IMG = '/Users/tapirus/Desktop/Imagens/'

dX, dY = 2048, 2048
xArray = np.linspace(0.0, 1.0, dX).reshape((1, dX, 1))
yArray = np.linspace(0.0, 1.0, dY).reshape((dY, 1, 1))

def randColor():
    a = random.choice([0, 0.5, 1, random.random()*0.5, 0.25 + random.random()*0.5])
    b = random.choice([0, 0.5, 1, random.random()*0.5, 0.25 + random.random()*0.5])
    c = random.choice([0, 0.5, 1, random.random()*0.5, 0.25 + random.random()*0.5])
    r = np.array([a, b, c]).reshape((1, 1, 3))
    return r

def getX(): return xArray
def getY(): return yArray
def safeDivide(a, b): return np.divide(a, np.maximum(b, 0.01))

def cria():    
    functions = [(0, randColor),
                 (0, getX),
                 (0, getY),
                 (1, np.sin),
                 (1, np.cos),
                 (1, np.tan),
                 (1, np.arctan),
                 (2, np.add),
                 (2, np.subtract),
                 (2, np.multiply),
                 (2, safeDivide),
                 ]
    return functions


def buildImg(depth = 0):
    funcs = [f for f in cria() if (f[0] > 0 and depth < 10) or (f[0] <= 0 and depth > 3)]
    nArgs, func = random.choice(funcs)
    args = [buildImg(depth + 1) for n in range(nArgs)]
    return func(*args)


def gerador_imagens(t=32):
    for n in range(t):
        img = buildImg()
        img = np.tile(img, (int(dX / img.shape[0]), int(dY / img.shape[1]), int(3 / img.shape[2])))
        img8Bit = np.uint8(np.rint(img.clip(0.0, 1) * (164.0 + 60.0*random.random())))
        Image.fromarray(img8Bit).save(PATH_IMG+str(n)+'.png', 'PNG')

# teste
gerador_imagens()
