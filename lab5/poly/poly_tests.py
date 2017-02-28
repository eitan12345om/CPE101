import unittest
import poly

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)


   # Add tests here
   def test_poly(self):
      poly1 = [2.3, 4.7, 1.0]
      poly2 = [1.2, 2.1, -3.2]
      self.assertListAlmostEqual(poly.poly_add2(poly1, poly2), [3.5, 6.8, -2.2])

   def test_poly2(self):
      poly1 = [-2.3, -4.7, -1.0]
      poly2 = [1.2, 2.1, -3.2]
      self.assertListAlmostEqual(poly.poly_add2(poly1, poly2), [-1.1, -2.6, -4.2])

   def test_mult(self):
      poly1 = [1, 2, 3]
      poly2 = [2, 1, 2]
      self.assertListAlmostEqual(poly.poly_mult2(poly1, poly2), [2, 5, 10, 7, 6])
   
   def test_mult2(self):
      poly1 = [0, 1, 1]
      poly2 = [1, 0, 1]
      self.assertListAlmostEqual(poly.poly_mult2(poly1, poly2), [0, 1, 1, 1, 1])



if __name__ == '__main__':
   unittest.main()
