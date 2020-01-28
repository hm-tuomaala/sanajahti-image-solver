from PIL import Image
import PIL.ImageOps
from pytesseract import image_to_string
import time
import os


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


class Ruutu():
    def __init__(self, char, coord, rn=None, rdn=None, dn=None, ldn=None, ln=None, lun=None, un=None, run=None):
        self.char = char
        self.coord = coord

        self.rn = rn
        self.rdn = rdn
        self.dn = dn
        self.ldn = ldn
        self.ln = ln
        self.lun = lun
        self.un = un
        self.run = run

    def addNeighbour(self, neighbour):
        if self.coord[0] == neighbour.coord[0]:
            if self.coord[1] == neighbour.coord[1]:
                return False
            elif self.coord[1] < neighbour.coord[1] and abs(self.coord[1] - neighbour.coord[1]) == 1:
                self.rn = neighbour
                return True
            elif self.coord[1] > neighbour.coord[1] and abs(self.coord[1] - neighbour.coord[1]) == 1:
                self.ln = neighbour
                return True
        if self.coord[0] > neighbour.coord[0] and abs(self.coord[0] - neighbour.coord[0]) == 1:
            if self.coord[1] > neighbour.coord[1] and abs(self.coord[1] - neighbour.coord[1]) == 1:
                self.lun = neighbour
                return True
            elif self.coord[1] == neighbour.coord[1]:
                self.un = neighbour
                return True
            elif self.coord[1] < neighbour.coord[1] and abs(self.coord[1] - neighbour.coord[1]) == 1:
                self.run = neighbour
                return True
        if self.coord[0] < neighbour.coord[0] and abs(self.coord[0] - neighbour.coord[0]) == 1:
            if self.coord[1] > neighbour.coord[1] and abs(self.coord[1] - neighbour.coord[1]) == 1:
                self.ldn = neighbour
                return True
            elif self.coord[1] == neighbour.coord[1]:
                self.dn = neighbour
                return True
            elif self.coord[1] < neighbour.coord[1] and abs(self.coord[1] - neighbour.coord[1]) == 1:
                self.rdn = neighbour
                return True
        else:
            return False

    def getNeighbour(self, char):
        ret = []
        if self.rn:
            if self.rn.char == char:
                ret.append(self.rn)
        if self.rdn:
            if self.rdn.char == char:
                ret.append(self.rdn)
        if self.dn:
            if self.dn.char == char:
                ret.append(self.dn)
        if self.ldn:
            if self.ldn.char == char:
                ret.append(self.ldn)
        if self.ln:
            if self.ln.char == char:
                ret.append(self.ln)
        if self.lun:
            if self.lun.char == char:
                ret.append(self.lun)
        if self.un:
            if self.un.char == char:
                ret.append(self.un)
        if self.run:
            if self.run.char == char:
                ret.append(self.run)
        return ret

    def getNbool(self, char):
        if self.rn:
            if self.rn.char == char:
                return True
        if self.rdn:
            if self.rdn.char == char:
                return True
        if self.dn:
            if self.dn.char == char:
                return True
        if self.ldn:
            if self.ldn.char == char:
                return True
        if self.ln:
            if self.ln.char == char:
                return True
        if self.lun:
            if self.lun.char == char:
                return True
        if self.un:
            if self.un.char == char:
                return True
        if self.run:
            if self.run.char == char:
                return True
        return False


    def __repr__(self):
        return "%s:(%s,%s)" % (self.char, str(self.coord[0]), str(self.coord[1]))


if __name__ == "__main__":

    # Location where downloaded images go from Gmail
    img = Image.open('/mnt/c/Users/Tuomaala/Downloads/Image-1.jpg')

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
    print(sana)
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

    f = open('sanat.txt', 'r', encoding='latin1')

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
