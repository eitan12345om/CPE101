# Project 2 - Moonlander
#
# Name: Eitan Simler
# Instructor: Jones 

from landerFuncs import *

def main():
   showWelcome()
   
   altitude = getAltitude()
   fuelAmount = getFuel()
   elapsedTime = 0
   velocity = 0
   fuelRate = 0
   
   print"\nLM state at retrorocket cutoff" 

   while altitude > 0:
      
      if fuelAmount > 0:
         displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)  
         print
         fuelRate = getFuelRate(fuelAmount)
     
      else:
         fuelRate = 0
         print "OUT OF FUEL - Elapsed Time: %3d Altitude: %7.2f Velocity: %7.2f" % (elapsedTime, altitude, velocity)    

      elapsedTime += 1
      fuelAmount = updateFuel(fuelAmount, fuelRate)
      acceleration = updateAcceleration(1.62, fuelRate)
      altitude = updateAltitude(altitude, velocity, acceleration)
      velocity = updateVelocity(velocity, acceleration)

   print"\nLM state at landing/impact"
   displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)

   print
   displayLMLandingStatus(velocity)

if __name__ == '__main__':
   main()
