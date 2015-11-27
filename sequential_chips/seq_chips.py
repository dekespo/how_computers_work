# List of units
import random, sys

# They need logic gates
sys.path.insert(0, "../gates") # import the necessary directory
import gates as G 

# Data-Flip-Folps (DFFs):
# Warning: this one is assumed a primitive gate like NAND
class DFF:
    def __init__(self, a):
        G.checkBit(a)
        self.temp = random.randint(0,1) # Noise
    def clock(self, nex):
        G.checkBit(nex)
        self.prev = self.temp
        self.temp = nex
        return self.prev

# A single-bit register: BIT
class BIT:
    def __init__(self, a):
        G.checkBit(a)
        self.aDFF = DFF(a)
        self.prev = random.randint(0,1) # Noise
        self.prevLoad = random.randint(0,1) # Noise
    def clock(self, nex, load):
        G.checkBit(nex); G.checkBit(load)
        part1 = G.AND(self.prevLoad, self.aDFF.clock(nex))
        part2 = G.AND(G.NOT(self.prevLoad), self.prev)
        self.prevLoad = load
        self.prev = G.OR(part1, part2)
        return self.prev

#Register-16bit: REGISTER
class REGISTER:
    def __init__(self, a):
        self.n = 16
        G.sizeCheckn(a, a, self.n)
        self.DFFs = []
        for i in range(self.n):
            self.DFFs.append(BIT(a[i]))
        #self.prev = random.randint(0,1) # Noise
        #self.prevLoad = random.randint(0,1) # Noise
    def clock(self, nex, load):
        G.sizeCheckn(nex, nex, self.n); G.checkBit(load)
        output = []
        for i in range(self.n):
            output.append(self.DFFs[i].clock(nex[i], load))
        return output
