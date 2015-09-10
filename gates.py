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

# n-bit version of Basic Gates

# Check if the sizes of gates are the same
def sizeCheck(g1, g2, nbits):
    if nbits == len(g1) and len(g1) == len(g2): pass
    else: sys.exit("THE INPUTS MUST THE SAME NUMBER OF BITS, ABORTING THE MISSION!")

#Gate: n-NOT
def NOTn(a, n):
    sizeCheck(a, a, n) # For this case
    return [NOT(a[i]) for i in xrange(n)]

#Gate: n-AND
def ANDn(a, b, n):
    sizeCheck(a, b, n) 
    return [AND(a[i], b[i]) for i in xrange(n)]

#Gate: n-OR
def ORn(a, b, n):
    sizeCheck(a, b, n) 
    return [OR(a[i], b[i]) for i in xrange(n)]

#n-Multiplexor: MUXn
def MUXn(a, b, n, sel):
    sizeCheck(a, b, n) 
    for i in xrange(n): checkBit(a[i]); checkBit(b[i])
    checkBit(sel)
    if sel == 0: return a
    else: return b

#n-way OR gates: ORnWays
def ORnWays(a, n):
    sizeCheck(a, a, n) # For this case


x = 0
y = 1
print NAND(x,y)
print NOT(x)
print AND(x,y)
print OR(x,y)
print XOR(x,y)
print MUX(x,y,1)
print DMUX(1,0)

x = [0, 1, 0, 1]
y = [0, 1, 1, 0]
print NOTn(x, len(x))
print ANDn(x, y, len(x))
print ORn(x, y, len(x))
print MUXn(x,y,len(x), 1)
