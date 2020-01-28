from PIL import Image
import PIL.ImageOps
from pytesseract import image_to_string
import time
import os
from ruutu import *


def getChar(char, list):
    ret = []
    for i in list:
        if i.char == char:
            ret.append(i)
    return ret


def recursion(ruutu, sana, index, used=[]):
    if len(used)+1 == len(sana):
        if ruutu.getNbool(sana[-1]):
            for i in ruutu.getNeighbour(sana[-1]):
                if i in used:
                    pass
                else:
                    used.append(i)
                    print(len(sana), sana, used)
    else:
        try:
            if ruutu.getNeighbour(sana[index]):
                for i in ruutu.getNeighbour(sana[index]):
                    if i not in used:
                        used.append(i)
                        recursion(i, sana, index+1, used)
                        used.pop()
        except IndexError:
            return False



if __name__ == "__main__":

    # Location where downloaded images go from Gmail
    img = Image.open('/mnt/c/Users/Tuomaala/Desktop/Programs/sanajahtisolver2/src/static/IMG_1.jpg')

    width, height = img.size

    img_crop = img.crop((65, height/2.1, width-65, height-80))

    img = img_crop
    out = Image.new('RGB', img.size, 0xffffff)

    width, height = img.size


    for x in range(width):
        for y in range(height):
            r,g,b = img.getpixel((x,y))
            if r == g == b and r >= 75 and g <= 94:
                out.putpixel((x,y), (255, 255, 255))
            else:
                out.putpixel((x,y), (0, 0, 0))
    inv_out = PIL.ImageOps.invert(out)

    sana = image_to_string(inv_out, lang='fin', config='--psm 6')
    # print(sana)
    time.sleep(1.5)
    data = sana.replace(' ', '').replace("|", "I")

    white_list = 'QWERTYUIOPASDFGHJKLÖÄZXCVBNM'

    ret = ''
    for k in data:
        if k in white_list:
            ret += k


    chars = ret.lower()
    timeStart = time.time()
    kirjaimet = []
    matriisi = [[], [], [], []]
    laskuri = 0

    for i in chars:
        kirjaimet.append(i)

    for i in range(4):
        for j in range(4):
            matriisi[i].append(kirjaimet[laskuri])
            laskuri += 1


    kopio = kirjaimet.copy()
    set = set()

    f = open('static/sanat.txt', 'r', encoding='latin1')

    found = False

    for i in f:
        sana = i.strip()
        for k in sana:
            if k in kopio:
                kopio.remove(k)
            else:
                kopio = kirjaimet.copy()
                found = False
                break
            found = True
        if found:
            set.add(sana)
            found = False
        kopio = kirjaimet.copy()

    lista = []
    for i in matriisi:
        for j in i:
            lista.append(Ruutu(j, tuple([matriisi.index(i), i.index(j)])))
            matriisi[matriisi.index(i)][i.index(j)] = 1

    for i in lista:
        for j in lista:
            i.addNeighbour(j)

    for sana in sorted(set, key=len):
        eka = getChar(sana[0], lista)
        index = 1
        for i in eka:
            used = [i]
            recursion(i, sana, index, used)
    timeEnd = time.time()
