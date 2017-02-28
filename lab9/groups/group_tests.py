import unittest
from groups import groups_of_3 as gro

class TestCases(unittest.TestCase):

   def assertListEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertEqual(el1, el2)

   def test_groups_of_3_1(self):
      self.assertListEqual(gro([1,2,3,4]), [[1,2,3], [4]])
   def test_groups_of_3_2(self):
      self.assertListEqual(gro([1,2,3,4,5]), [[1,2,3], [4, 5]])
   def test_groups_of_3_3(self):
      self.assertListEqual(gro([1,2,3,4,5,6,7,8,9]), [[1,2,3], [4,5,6], [7,8,9]])




if __name__ == '__main__':
   unittest.main()
