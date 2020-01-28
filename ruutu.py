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
