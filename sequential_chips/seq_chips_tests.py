# Testing file with unittest

import unittest
import seq_chips
import gates as G 

class MyTest(unittest.TestCase):
    # Test 1
    def test_DFF(self):
        arrx16, arry16 = [], []
        xDFF, yDFF = seq_chips.DFF(x16[0]), seq_chips.DFF(y16[0])
        for i in range(len(x16)):
            arrx16.append(xDFF.clock(x16[i]))
            arry16.append(yDFF.clock(y16[i]))
        self.assertEqual(arrx16[1:], x16[:15]) 
        self.assertEqual(arry16[1:], y16[:15]) 

if __name__ == "__main__":
    x16 = [1, 0, 1, 0] * 4
    y16 = [0, 0, 1, 1] * 4

    #Run the tests
    unittest.main()
