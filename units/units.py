# List of units
import random, sys

# They need logic gates
sys.path.insert(0, "../gates") # import the necessary directory
import gates as G 

# Part 1: The combination of gates to set the value to 0
def Zero16(x):
    return G.AND16(x, G.NOT16(x))

# Part 2: The combination of gates to set the value to 1
def One16(x):
    return G.OR16(x, G.NOT16(x))

# Part 3: Convert one bit to n bits with wires
def wiresN(x, n):
    G.checkBit(x)
    return [x] * n

# Arithmetic Logic Unit (ALU) in 16 bits: ALU16
def ALU16(x, y, zx, nx, zy, ny, f, no):
    n = 16
    output = [random.randint(0,1) for i in range(n)] # Random noise in bits
    print("current output (noise or leftover) = ", output)
    G.sizeCheckn(output, output, n)

    # Condition 1
    if zx == 1: x = Zero16(x)
    else: pass # x does not change

    # Condition 2
    if nx == 1: x = G.NOT16(x)
    else: pass

    # Condition 3
    if zy == 1: y = Zero16(y)
    else: pass # y does not change

    # Condition 4
    if ny == 1: y = G.NOT16(y)
    else: pass

    # Condition 5
    if f == 1: output = G.Add16(x, y) 
    else: output = G.AND16(x, y)

    # Condition 6
    if no == 1: output = G.NOT16(output)
    else: pass

    return output
    
