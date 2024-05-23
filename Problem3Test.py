from Problem3 import Payload
import unittest

class TestProblem3(unittest.TestCase):
    def testPOST(self):
        self.assertIn("tx_hash", str(Payload("ETH", 4500, 1678912345).sendPayLoad()))

    def testGET(self):
        self.assertIn("tx_status", str(Payload("ETH", 4500, 1678912345).getPayLoad()))

if __name__ == '__main__':
    unittest.main()