import unittest
import calc

class TestSum(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test2(self):
        self.assertEqual(calc.add(524, 125), 649)

class TestSub(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc.sub(15, 4), 11)

    def test2(self):
        self.assertEqual(calc.sub(1, 3), -2)

class TestMul(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc.mul(32, 2), 64)
    
    def test2(self):
        self.assertEqual(calc.mul(5, 0), 0)

    def test3(self):
        self.assertEqual(calc.mul(95, 1), 95)

class TestDiv(unittest.TestCase):
    def test1(self):
        self.assertEqual(calc.div(6, 2), 3)
    
    def test2(self):
        self.assertEqual(calc.div(100, 5), 20)

    def test3(self):
        self.assertEqual(calc.div(13, 2), 6)

if __name__ == '__main__':
    unittest.main()