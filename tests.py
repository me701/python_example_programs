import unittest

from first_largest import largest_element

class FirstLargest(unittest.TestCase):

    def test_largest_is_first(self):
        given = [5,3,4,2,1]
        expect = 5
        got = largest_element(given)
        self.assertEqual(got, expect)
    def test_largest_is_first(self):
        given = [5,3,4,2,1]
        expect = 5, 0
        got = largest_element(given, loc=True)
        self.assertEqual(got, expect) 
    """ ADD MORE  """

if __name__ == '__main__':
    unittest.main()
