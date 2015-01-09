import unittest

def IsOdd(n):
    return n % 2 == 1

def IsEven(x):
    return x % 2 == 0

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testtwo(self):
        self.failIf(IsOdd(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()

