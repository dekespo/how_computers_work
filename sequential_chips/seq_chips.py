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

#def bit(a, load):
#    G.checkBit(a); G.checkbit(load)
#    G.NOT()
