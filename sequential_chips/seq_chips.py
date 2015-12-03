# List of units
import random, sys, math
import numpy as np

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
		self.BITs = []
		for i in range(self.n):
			self.BITs.append(BIT(a[i]))
	def clock(self, nex, load):
		G.sizeCheckn(nex, nex, self.n); G.checkBit(load)
		output = []
		for i in range(self.n):
			output.append(self.BITs[i].clock(nex[i], load))
		return output

# RAMr (where r is the number of registers) with 16 bits
class RAMr:
	def __init__(self, a, address, r):
		self.k = math.log(r,2)
		if len(address) != self.k:
			sys.exit("THE NUMBER OF BITS IN ADDRESS DOES NOT MATCH WITH THE NUMBER OF REGISTERS. ABORTING THE MISSION!")
		self.n = 16
		G.sizeCheckn(a, a, self.n)
		self.registers = {}
		for i in range(r):
			den = np.binary_repr(i, int(self.k))
			self.registers[den] = REGISTER([random.randint(0, 1) for i in range(self.n)])
		self.registers[address] = REGISTER(a)
	# load = 0: read; load = 1: write, address should be string of bits
	def clock(self, nex, load, address): 
		G.sizeCheckn(nex, nex, self.n); G.checkBit(load)
		for next in address:
			G.checkBit(int(next))
		if len(address) > self.k:
			sys.exit("THE NUMBER OF BITS IN ADDRESS IS NOT LESS THAN THE NUMBER OF REGISTERS. ABORTING THE MISSION!")
		output = self.registers[address].clock(nex, load)
		return output

