import unittest
import Problem1

class TestProblem1(unittest.TestCase):
    def test_good_boy(self):
        self.assertEqual(Problem1.IsGoodBoy("SRSSRRR"),"Good boy")
        self.assertEqual(Problem1.IsGoodBoy("SRSSSRRRR"),"Good boy")
        self.assertEqual(Problem1.IsGoodBoy("SSRSSRRR"),"Good boy")

    def test_bad_boy(self):
        self.assertEqual(Problem1.IsGoodBoy("R"),"Bad boy")
        self.assertEqual(Problem1.IsGoodBoy("S"),"Bad boy")
        self.assertEqual(Problem1.IsGoodBoy("SRRR"),"Bad boy")
        self.assertEqual(Problem1.IsGoodBoy("SRSSSRRRRR"),"Bad boy")

if __name__ == '__main__':
    unittest.main()