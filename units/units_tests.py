# Testing file with unittest

import unittest
import units
import gates as G 

class MyTest(unittest.TestCase):
    # Test 1
    def test_ALU16(self):
        self.assertEqual(units.ALU16(x16, y16, 1, 0, 1, 0, 1, 0), zeros16) # 0
        self.assertEqual(units.ALU16(x16, y16, 1, 1, 1, 1, 1, 1), oneIn16) # 1
        self.assertEqual(units.ALU16(x16, y16, 1, 1, 1, 0, 1, 0), ones16) # -1
        self.assertEqual(units.ALU16(x16, y16, 0, 0, 1, 1, 0, 0), x16)
        self.assertEqual(units.ALU16(x16, y16, 1, 1, 0, 0, 0, 0), y16)
        self.assertEqual(units.ALU16(x16, y16, 0, 0, 1, 1, 0, 1), G.NOT16(x16))
        self.assertEqual(units.ALU16(x16, y16, 1, 1, 0, 0, 0, 1), G.NOT16(y16))
        self.assertEqual(units.ALU16(x16, y16, 0, 0, 1, 1, 1, 1), G.Inc16(G.NOT16(x16))) # -x16
        self.assertEqual(units.ALU16(x16, y16, 1, 1, 0, 0, 1, 1), G.Inc16(G.NOT16(y16))) # -y16
        self.assertEqual(units.ALU16(x16, y16, 0, 1, 1, 1, 1, 1), G.Inc16(x16)) # x + 1
        self.assertEqual(units.ALU16(x16, y16, 1, 1, 0, 1, 1, 1), G.Inc16(y16)) # y + 1
        self.assertEqual(units.ALU16(x16, y16, 0, 0, 1, 1, 1, 0), G.NOT16(G.Inc16(G.NOT16(x16)))) # x - 1
        self.assertEqual(units.ALU16(x16, y16, 1, 1, 0, 0, 1, 0), G.NOT16(G.Inc16(G.NOT16(y16)))) # y - 1
        self.assertEqual(units.ALU16(x16, y16, 0, 0, 0, 0, 1, 0), G.Add16(x16, y16))
        self.assertEqual(units.ALU16(x16, y16, 0, 0, 0, 0, 0, 0), G.AND16(x16, y16))
        self.assertEqual(units.ALU16(x16, y16, 0, 1, 0, 1, 0, 1), G.OR16(x16, y16))
        self.assertEqual(units.ALU16(oneIn16, y16, 0, 1, 1, 1, 1, 1), twoIn16) # 1 + 1 = 2
        self.assertEqual(units.ALU16(twoIn16, y16, 0, 0, 1, 1, 1, 0), oneIn16) # 2 - 1 = 1


if __name__ == "__main__":
    x16 = [1, 0, 1, 0] * 4
    y16 = [0, 0, 1, 1] * 4
    zeros16 = [0] * 16 # represent 0
    ones16 = [1] * 16 # represent -1
    oneIn16 = [0] * 15 + [1] # represent 1
    twoIn16 = [0] * 14 + [1] + [0] # represent 2

    #Run the tests
    unittest.main()
