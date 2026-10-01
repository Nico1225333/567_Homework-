import unittest

def classifyTriangle(a,b,c):

    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'

    if a == b and b == c:
        return 'Equilateral'

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return 'Right'

    if a == b or a == c or b == c:
        return 'Isoceles'

    return 'Scalene'


def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


class TestTriangles(unittest.TestCase):

    def testSet1(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right')
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle')

    def testMyTestSet2(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
        self.assertEqual(classifyTriangle(5,5,8),'Isoceles')
        self.assertEqual(classifyTriangle(4,5,6),'Scalene')


if __name__ == '__main__':

    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)

    unittest.main(exit=False)