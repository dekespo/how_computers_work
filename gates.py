# List of gates
import sys

# Check if it is a bit (0 or 1)
def checkBit(bit):
    if bit == 0 or bit == 1: pass
    else: sys.exit("THE INPUT MUST BE A BIT, ABORTING THE MISSION!")

# Basic Logic Gates

# Primitive Gate: NAND
def NAND(a, b):
    checkBit(a); checkBit(b)
    if a == 1 and a == b: return 0
    else: return 1

# Gate: NOT
def NOT(a):
    return NAND(a, a)

# Gate: AND
def AND(a,b):
    return NOT(NAND(a,b))

# Gate: OR
def OR(a, b):
    return NOT(AND(NOT(a), NOT(b)))

# Gate: XOR
def XOR(a, b):
    return OR(AND(a, NOT(b)), AND(NOT(a), b))

# Multiplexor: MUX
def MUX(a, b, sel):
    checkBit(a); checkBit(b); checkBit(sel)
    if sel == 0: return a
    else: return b

# Demultiplexor: DMUX
def DMUX(bit, sel):
    if sel == 0: return bit, 0
    else: return 0, bit

x = 0
y = 1
print NAND(x,y)
print NOT(x)
print AND(x,y)
print OR(x,y)
print XOR(x,y)
print MUX(x,y,1)
print DMUX(1,0)
