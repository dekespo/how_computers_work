# Testing file with unittest

import unittest
import units

class MyTest(unittest.TestCase):
    # Test 1
    def test_ALU16(self):
        self.assertEqual(units.ALU16(x16, y16, 1, 0, 1, 0, 1, 0), zeros16)

if __name__ == "__main__":
    x16 = [1, 0, 1, 0] * 4
    y16 = [0, 0, 1, 1] * 4
    zeros16 = [0] * 16
    ones16 = [1] * 16

    #Run the tests
    unittest.main()
