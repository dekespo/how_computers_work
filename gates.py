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
    return OR(AND(a,NOT(sel)), AND(b,sel))

# Demultiplexor: DMUX
def DMUX(bit, sel): 
    return AND(NOT(sel),bit), AND(sel,bit)

# n-bit version of Basic Gates
# For the sake simplicty n-bits will be:
# 4 (2**2)
# 8 (2**3)
# 16 (2**4)

# Check if the sizes of gates are the same
def sizeCheckn(g1, g2, n):
    if len(g1) == n and len(g1) == len(g2): pass
    else: sys.exit("THE INPUTS MUST THE SAME NUMBER OF BITS, ABORTING THE MISSION!")

#Gate: 16-NOT
def NOT16(a):
    n = 16
    sizeCheckn(a, a, n) 
    return [NOT(a[i]) for i in range(n)]

#Gate: 16-AND
def AND16(a, b):
    n = 16
    sizeCheckn(a, b, n) 
    return [AND(a[i], b[i]) for i in range(n)]

#Gate: 16-OR
def OR16(a, b):
    n = 16
    sizeCheckn(a, b, n) 
    return [OR(a[i], b[i]) for i in range(n)]

#16-Multiplexor: MUX16
def MUX16(a, b, sel):
    n = 16
    sizeCheckn(a, b, n) 
    for i in range(n): 
        checkBit(a[i]); checkBit(b[i])
    checkBit(sel)
    sel16 = [sel] * n # 16 different wires?
    return OR16(AND16(a,NOT16(sel16)), AND16(b,sel16))

#8-way OR gate: OR8Ways
def OR_8Ways(a): # It can be solved by recursion
    n = 8
    sizeCheckn(a, a, n) 
    a1 = OR(a[0], a[1])
    a2 = OR(a[2], a[3])
    a3 = OR(a[4], a[5])
    a4 = OR(a[6], a[7])
    b1 = OR(a1, a2)
    b2 = OR(a3, a4)
    return OR(b1, b2)

#4-way 16-bit Multiplexor: MUX16_4Ways
def MUX16_4Ways(a, b, c, d, sel2):
    n = 16
    sizeCheckn(a, b, n) 
    sizeCheckn(c, d, n) 
    for i in range(n): 
        checkBit(a[i]); checkBit(b[i])
        checkBit(c[i]); checkBit(d[i])
    for i in range(2):
        checkBit(sel2[i])
    sel0_16 = [sel2[0]] * n # 16 different wires?
    sel1_16 = [sel2[1]] * n # 16 different wires?

    return OR16(
       AND16(NOT16(sel0_16),MUX16(a, b, sel2[1])),
       AND16(sel0_16,MUX16(c, d, sel2[1]))
       )

#4-way Demultiplexor: DEMUX_4Ways 
def DEMUX_4Ways(bit, sel2):
    checkBit(bit);
    for i in range(2): checkBit(sel2[i])
    return AND(AND(NOT(sel2[0]), NOT(sel2[1])),bit),\
           AND(AND(NOT(sel2[0]), sel2[1]),bit),\
           AND(AND(sel2[0], NOT(sel2[1])),bit),\
           AND(AND(sel2[0], sel2[1]),bit)
