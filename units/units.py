# List of units
import random, sys

# They need logic gates
sys.path.insert(0, "../gates") # import the necessary directory
import gates as G 

# Part 1: The combination of gates to zero a value
def Zero16(x):
    return G.AND16(x, G.NOT16(x))

# Part 2: The combination of gates to one a value
def One16(x):
    return G.OR16(x, G.NOT16(x))

# Part 3: Convert one bit to nbits with wires
def wiresN(x, n):
    G.checkBit(x)
    return [x] * n

# Arithmetic Logic Unit (ALU) in 16 bits: ALU16
def ALU16(x, y, zx, nx, zy, ny, f, no):
    n = 16
    result = [random.randint(0,1) for i in range(n)] # Random noise in bits
    print("result = ", result)
    G.sizeCheckn(result, result, n)
    # Line 1:
    lineCheck1 = G.AND(zx, G.AND(G.NOT(nx), G.AND(zy, G.AND(G.NOT(zy), G.AND(f, G.NOT(no))))))
    result = G.AND16(wiresN(lineCheck1, n), Zero16(x)) # Not sure if this one is a good way
    return result
    
