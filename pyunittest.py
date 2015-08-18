# install pip and then run pip install pyunit
import unittest
class simpletest(unittest.TestCase):
    def test(self):
        self.failUnless(True)
if __name__=='__main__':
    unittest.main()
