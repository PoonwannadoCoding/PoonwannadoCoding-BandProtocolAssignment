import unittest
import Problem2


class TestProblem2(unittest.TestCase):
    def test_5_chicken(self):

        self.assertEqual(Problem2.superManChicken(5,10,[1,11,15,17,20]), 4)
        self.assertEqual(Problem2.superManChicken(5,2,[1,2,7,11,17]), 2)
        self.assertEqual(Problem2.superManChicken(5,5,[1,2,3,5,10]), 4)
    
    def test_10_chicken(self):
        self.assertEqual(Problem2.superManChicken(10,10,[10,11,15,17,19, 20, 26, 29, 30, 35]), 5)

if __name__ == '__main__':
    unittest.main()