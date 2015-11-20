# Testing file with unittest

import unittest
import units
import gates as G 

class MyTest(unittest.TestCase):
    # Test 1
    def test_ALU16(self):
        self.assertEqual(units.ALU16(x16, y16, 1, 0, 1, 0, 1, 0), zeros16)
        #self.assertEqual(units.ALU16(x16, y16, 1, 1, 1, 1, 1, 1), ones16)
        # TODO: Gives error how to define 1 or -1 in 16-bits?
        self.assertEqual(units.ALU16(x16, y16, 0, 0, 1, 1, 0, 0), x16)
        self.assertEqual(units.ALU16(x16, y16, 1, 1, 0, 0, 0, 0), y16)
        self.assertEqual(units.ALU16(x16, y16, 0, 0, 1, 1, 0, 1), G.NOT16(x16))
        self.assertEqual(units.ALU16(x16, y16, 1, 1, 0, 0, 0, 1), G.NOT16(y16))
        self.assertEqual(units.ALU16(x16, y16, 0, 0, 0, 0, 1, 0), G.Add16(x16, y16))
        self.assertEqual(units.ALU16(x16, y16, 0, 0, 0, 0, 0, 0), G.AND16(x16, y16))
        self.assertEqual(units.ALU16(x16, y16, 0, 1, 0, 1, 0, 1), G.OR16(x16, y16))


if __name__ == "__main__":
    x16 = [1, 0, 1, 0] * 4
    y16 = [0, 0, 1, 1] * 4
    zeros16 = [0] * 16
    ones16 = [1] * 16

    #Run the tests
    unittest.main()
