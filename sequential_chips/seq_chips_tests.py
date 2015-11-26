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

    # Test 2
    def test_BIT(self):
        arrx16Ones, arry16Ones = [], []
        xBITOnes, yBITOnes = seq_chips.BIT(x16[0]), seq_chips.BIT(y16[0])
        for i in range(len(loadOnes)):
            arrx16Ones.append(xBITOnes.clock(x16[i], loadOnes[i]))
            arry16Ones.append(yBITOnes.clock(y16[i], loadOnes[i]))
        self.assertEqual(arrx16Ones[1:], x16[:15]) 
        self.assertEqual(arry16Ones[1:], y16[:15]) 

        arrx16Zeros, arry16Zeros = [], []
        xBITZeros, yBITZeros = seq_chips.BIT(x16[0]), seq_chips.BIT(y16[0])
        for i in range(len(loadZeros)):
            arrx16Zeros.append(xBITOnes.clock(x16[i], loadZeros[i]))
            arry16Zeros.append(yBITOnes.clock(y16[i], loadZeros[i]))
        self.assertEqual(arrx16Zeros[1:], arrx16Zeros[:15]) 
        self.assertEqual(arry16Zeros[1:], arry16Zeros[:15]) 

        arrxSpecial, arrySpecial = [], []
        xBITSpecial, yBITSpecial = seq_chips.BIT(x16[0]), seq_chips.BIT(y16[0])
        for i in range(len(loadSpecial)):
            arrxSpecial.append(xBITOnes.clock(x16[i], loadSpecial[i]))
            arrySpecial.append(yBITOnes.clock(y16[i], loadSpecial[i]))
        self.assertEqual(arrxSpecial[1:], resultSpecialX) 
        self.assertEqual(arrySpecial[1:], resultSpecialY) 

if __name__ == "__main__":
    x16 = [1, 0, 1, 0] * 4
    y16 = [0, 0, 1, 1] * 4
    loadOnes = [1] * 16
    loadZeros = [0] * 16
    loadSpecial = [1, 1, 0, 1, 1]
    resultSpecialX = [1, 0, 0, 0]
    resultSpecialY = [0, 0, 0, 1]

    #Run the tests
    unittest.main()
