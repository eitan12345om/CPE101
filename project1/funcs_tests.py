# Project 1
#
# Name: Eitan Simler
# Instructor: B. Jones
# Section: 17

import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_poundsToKG(self):
      self.assertAlmostEqual(funcs.poundsToKG(20), 9.07183999)
   def test_poundsToKG_2(self):
      self.assertAlmostEqual(funcs.poundsToKG(0), 0)
   def test_poundsToKG_3(self):
      self.assertAlmostEqual(funcs.poundsToKG(3.14159), 1.4250000912)

   def test_getMassObject(self):
      self.assertAlmostEqual(funcs.getMassObject('t'), 0.1)
   def test_getMassObject_2(self):
      self.assertAlmostEqual(funcs.getMassObject('p'), 1.0)
   def test_getMassObject_3(self):
      self.assertAlmostEqual(funcs.getMassObject('r'), 3.0)
   def test_getMassObject_4(self):
      self.assertAlmostEqual(funcs.getMassObject('g'), 5.3)
   def test_getMassObject_5(self):
      self.assertAlmostEqual(funcs.getMassObject('l'), 9.07)
   def test_getMassObject_6(self):
      self.assertAlmostEqual(funcs.getMassObject('a'), 0.0)
   def test_getMassObject_7(self):
      self.assertAlmostEqual(funcs.getMassObject(3), 0.0)

   def test_getVelocityObject(self):
      self.assertAlmostEqual(funcs.getVelocityObject(0), 0.0)
   def test_getVelocityObject_2(self):
      self.assertAlmostEqual(funcs.getVelocityObject(10), 7.0)
   def test_getVelocityObject_3(self):
      self.assertAlmostEqual(funcs.getVelocityObject(15.0), 8.573214099)

   def test_getVelocitySkater(self):
      self.assertAlmostEqual(funcs.getVelocitySkater(1, 1, 0.0), 0)
   def test_getVelocitySkater_2(self):
      self.assertAlmostEqual(funcs.getVelocitySkater(1, 1, 54.0), 54.0)
   def test_getVelocitySkater_3(self):
      self.assertAlmostEqual(funcs.getVelocitySkater(3.0, 1, 27.0), 9.0)
   def test_getVelocitySkater_4(self):
      self.assertAlmostEqual(funcs.getVelocitySkater(3.0, 3.0, 27.0), 27.0)
   def test_getVelocitySkater_5(self):
      self.assertAlmostEqual(funcs.getVelocitySkater(1, 3.0, 27), 81.0)
   def test_getVelocitySkater_6(self):
      self.assertAlmostEqual(funcs.getVelocitySkater(1, 3, 27), 81)

if __name__ == '__main__':
   unittest.main()
