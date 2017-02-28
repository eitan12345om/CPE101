# Project 2 - Moonlander
#
# Name: Eitan Simler
# Instructor: Jones 

import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   def test_update_acc2(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 5), 0)
   def test_update_acc3(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 9), 1.296)
  
   def test_update_alt1(self):
      self.assertAlmostEqual(updateAltitude(1.62, 0, 0), 1.62)
   def test_update_alt2(self):
      self.assertAlmostEqual(updateAltitude(5.0, -3, -1.62), 1.19)
   def test_update_alt3(self):
      self.assertAlmostEqual(updateAltitude(10.0, 0, -1.62), 9.19)
   def test_update_alt4(self):
      self.assertAlmostEqual(updateAltitude(2.0, -4.0, 0), 0)

   def test_update_vel1(self):
      self.assertAlmostEqual(updateVelocity(2.0, 0), 2.0)
   def test_update_vel2(self):
      self.assertAlmostEqual(updateVelocity(2.0, -1.62), 0.38)
   def test_update_vel3(self):
      self.assertAlmostEqual(updateVelocity(-2.0, 0), -2.0)
   def test_update_vel4(self):
      self.assertAlmostEqual(updateVelocity(-2.0, -1.62), -3.62)
   
   def test_update_fuel1(self):
      self.assertAlmostEqual(updateFuel(100, 9), 91)
   def test_update_fuel2(self):
      self.assertAlmostEqual(updateFuel(100, 0), 100)
   def test_update_fuel3(self):
      self.assertAlmostEqual(updateFuel(100, 5), 95)
      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

