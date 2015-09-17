# Testing File with unittest

import unittest
import gates 

class MyTest(unittest.TestCase):
    # Test 1
    def test_NAND(self):
        nand_result = [1, 1, 1, 0]
        for i in range(len(x)):
            self.assertEqual(gates.NAND(x[i],y[i]), nand_result[i])

    # Test 2
    def test_NOT(self):
        notx_result = [1, 1, 0, 0]
        for i in range(len(x)):
            self.assertEqual(gates.NOT(x[i]), notx_result[i])

    # Test 3
    def test_AND(self):
        and_result = [0, 0, 0, 1]
        for i in range(len(x)):
            self.assertEqual(gates.AND(x[i],y[i]), and_result[i])

    # Test 4
    def test_OR(self):
        or_result = [0, 1, 1, 1]
        for i in range(len(x)):
            self.assertEqual(gates.OR(x[i],y[i]), or_result[i])

    # Test 5
    def test_XOR(self):
        xor_result = [0, 1, 1, 0]
        for i in range(len(x)):
            self.assertEqual(gates.XOR(x[i],y[i]), xor_result[i])

    # Test 6
    def test_MUX(self):
        mux_result = [x[0], y[0]]
        for i in range(len(sel)):
            self.assertEqual(gates.MUX(x[0],y[0],sel[i]), mux_result[i])

    # Test 7
    def test_DMUX(self):
        dmux_result = [(x[0], 0), (0, x[0])]
        for i in range(len(sel)):
            self.assertEqual(gates.DMUX(x[0],sel[i]), dmux_result[i])

    # Test 8
    def test_NOT16(self):
        notx16_result = [1, 1, 0, 0] * 4
        self.assertEqual(gates.NOT16(x16), notx16_result)

    # Test 9
    def test_AND16(self):
        and16_result = [0, 0, 0, 1] * 4
        self.assertEqual(gates.AND16(x16,y16), and16_result)

    # Test 10
    def test_OR16(self):
        or16_result = [0, 1, 1, 1] * 4
        self.assertEqual(gates.OR16(x16,y16), or16_result)

    # Test 11
    def test_MUX16(self):
        mux16_result = [x16, y16]
        for i in range(len(sel)):
            self.assertEqual(gates.MUX16(x16,y16,sel[i]), mux16_result[i])

    # Test 12
    def test_OR_8Ways(self):
        or_8ways_result = [1,0]
        for i in range(len(x8_2)):
            self.assertEqual(gates.OR_8Ways(x8_2[i]), or_8ways_result[i])

    # Test 13
    def test_MUX16_4Ways(self):
        mux16_4ways_result = [x16, y16, z16, w16]
        for i in range(len(sel2)):
            self.assertEqual(gates.MUX16_4Ways(x16, y16, z16, w16, sel2[i]), mux16_4ways_result[i])

    # Test 14
    def test_DEMUX_4Ways(self):
        demux_4ways_result = ((1, 0, 0, 0),
                              (0, 1, 0, 0),
                              (0, 0, 1, 0),
                              (0, 0, 0, 1))
        for i in range(len(sel2)):
            self.assertEqual(gates.DEMUX_4Ways(1, sel2[i]), demux_4ways_result[i])

    # Test 15
    def test_HalfAdder(self):
        halfadder_result = ((0, 1, 1, 0), (0, 0, 0, 1))
        for i in range(len(x)):
            self.assertEqual(gates.HalfAdder(x[i],y[i]), (halfadder_result[0][i], halfadder_result[1][i]))
        
    # Test 16
    def test_FullAdder(self):
        fulladder_result = ((0, 1, 1, 0, 1, 0, 0, 1), (0, 0, 0, 1, 0, 1, 1, 1))
        for i in range(len(x8)):
            self.assertEqual(gates.FullAdder(x8[i],y8[i],z8[i]), (fulladder_result[0][i], fulladder_result[1][i]))
        
    # Test 17
    def test_Add16(self):
        add16_result = ([1,0,0,0] * 4, w16)
        self.assertEqual(gates.Add16(x16,y16), add16_result[0])
        self.assertEqual(gates.Add16(z16,w16), add16_result[1])

    # Test 18
    def test_Inc16(self):
        check = [0] * 15
        check.append(1)
        inc16_result = (check, z16)
        self.assertEqual(gates.Inc16(z16), inc16_result[0])
        self.assertEqual(gates.Inc16(w16), inc16_result[1])

if __name__ == "__main__":
    #Inputs
    x = [0, 0, 1, 1]
    y = [0, 1, 0, 1]
    sel = [0, 1]
    x16 = [0, 0, 1, 1] * 4
    y16 = [0, 1, 0, 1] * 4
    x8_2 = [[0, 0, 0, 1] * 2, [0] * 8]
    z16 = [0, 0, 0, 0] * 4
    w16 = [1, 1, 1, 1] * 4
    sel2 =[[0, 0], [0, 1], [1, 0], [1, 1]]
    ones = [1] * 4
    zeros = [0] * 4
    x8 = x*2
    y8 = y*2
    z8 = zeros + ones 

    # Run the tests
    unittest.main()

