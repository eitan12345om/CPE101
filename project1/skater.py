# Project 1
#
# Name: Eitan Simler
# Instructor: B. Jones
# Section: 17

import funcs

def main():
   pounds = float(raw_input('How much do you weigh (pounds)? '))
   distance = float(raw_input('How far away is your professor (meters)? '))
   object = raw_input('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ')

   massSkater = funcs.poundsToKG(pounds)
   massObject = funcs.getMassObject(object)
   velObject = funcs.getVelocityObject(distance)
   velSkater = funcs.getVelocitySkater(massSkater, massObject, velObject)

   if massObject <= 0.1:
      statement1 = "You're going to get an F!"
   elif massObject <= 1.0:
      statement1 = "Make sure your professor is OK."
   else:
      if distance < 20:
         statement1 = "How far away is the hospital?"
      else:
         statement1 = "RIP professor."
   
   if velSkater < 0.2:
      statement2 = "My grandmother skates faster than you!"
   elif velSkater >= 1.0:
         statement2 = "Look out for that railing!!!"
   else:
      statement2 = ""

   print "\nNice throw! " + statement1
   print "Velocity of skater: %.3f m/s" % velSkater
   if statement2:
      print statement2

if __name__ == '__main__':
   main()
