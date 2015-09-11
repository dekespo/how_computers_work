# Testing File with unittest

import unittest
import gates 

class MyTest(unittest.TestCase):
    def test_NAND(self):
        nand_result = [1, 1, 1, 0]
        for i in xrange(len(x)):
            self.assertEqual(gates.NAND(x[i],y[i]), nand_result[i])

    def test_NOT(self):
        notx_result = [1, 1, 0, 0]
        for i in xrange(len(x)):
            self.assertEqual(gates.NOT(x[i]), notx_result[i])

    def test_AND(self):
        and_result = [0, 0, 0, 1]
        for i in xrange(len(x)):
            self.assertEqual(gates.AND(x[i],y[i]), and_result[i])

    def test_OR(self):
        or_result = [0, 1, 1, 1]
        for i in xrange(len(x)):
            self.assertEqual(gates.OR(x[i],y[i]), or_result[i])

    def test_XOR(self):
        xor_result = [0, 1, 1, 0]
        for i in xrange(len(x)):
            self.assertEqual(gates.XOR(x[i],y[i]), xor_result[i])

    def test_MUX(self):
        mux_result = [x[0], y[0]]
        for i in xrange(len(sel)):
            self.assertEqual(gates.MUX(x[0],y[0],sel[i]), mux_result[i])

    def test_DMUX(self):
        dmux_result = [(x[0], 0), (0, x[0])]
        for i in xrange(len(sel)):
            self.assertEqual(gates.DMUX(x[0],sel[i]), dmux_result[i])

if __name__ == "__main__":

    #Inputs
    x = [0, 0, 1, 1]
    y = [0, 1, 0, 1]
    sel = [0, 1]
    unittest.main()
#x = 0
#y = 1
#print NAND(x,y)
#print NOT(x)
#print AND(x,y)
#print OR(x,y)
#print XOR(x,y)
#print MUX(x,y,1)
#print DMUX(1,0)
#
#x = [0, 1, 0, 1]
#x = [0, 0, 0, 1]
#y = [0, 1, 1, 0]
#print NOTn(x, len(x))
#print ANDn(x, y, len(x))
#print ORn(x, y, len(x))
#print MUXn(x,y,len(x), 1)
#print ORnWays(x, len(x))
