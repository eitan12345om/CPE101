# Project 2 - Moonlander
#
# Name: Eitan Simler
# Instructor: Jones 

def showWelcome():
   print "\nWelcome aboard the Lunar Module Flight Simulator\n"
   print "   To begin you must specify the LM's initial altitude"
   print "   and fuel level.  To simulate the actual LM use"
   print "   values of 1300 meters and 500 liters, respectively.\n"
   print "   Good luck and may the force be with you!\n"
 
def getFuel():
   fuelAmount = int(raw_input("Enter the initial amount of fuel on board the LM (in liters): "))
   
   while fuelAmount < 1:
      print "ERROR: Amount of fuel must be positive, please try again"
      fuelAmount = int(raw_input("Enter the initial amount of fuel on board the LM (in liters): ")) 

   return fuelAmount   

def getAltitude():     
   altitude = float(raw_input("Enter the initial altitude of the LM (in meters): "))

   while altitude < 1 or altitude > 9999:
      print "ERROR: Altitude must be between 1 and 9999, inclusive, please try again"
      altitude = int(raw_input("Enter the initial altitude of the LM (in meters): "))
   
   return altitude
   
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   print "Elapsed Time: %4d s" % elapsedTime
   print "        Fuel: %4d l" % fuelAmount
   print "        Rate: %4d l/s" % fuelRate
   print "    Altitude: %7.2f m" % altitude
   print "    Velocity: %7.2f m/s" % velocity

def getFuelRate(currentFuel):
   fuelRate = int(raw_input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   
   while fuelRate < 0 or fuelRate > 9:
      print "ERROR: Fuel rate must be between 0 and 9, inclusive"
      fuelRate = int(raw_input("\nEnter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))

   if currentFuel - fuelRate < 0:
      return currentFuel
   return fuelRate
 
def updateAcceleration(gravity, fuelRate):
   return gravity * ((fuelRate / 5.0) - 1)
	
def updateAltitude(altitude, velocity, acceleration):
   return max(altitude + velocity + (acceleration / 2), 0) 

def updateVelocity(velocity, acceleration):
   return velocity + acceleration

def updateFuel(fuel, fuelRate):
   return fuel - fuelRate

def displayLMLandingStatus(velocity):
   if -1 <= velocity <= 0:
      print "Status at landing - The eagle has landed!"
   elif -10 < velocity < -1:
      print "Status at landing - Enjoy your oxygen while it lasts!"
   else:
      print "Status at landing - Ouch - that hurt!"
