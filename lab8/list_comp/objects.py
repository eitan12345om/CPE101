from utility import epsilon_equal as fl_eq

class Point():
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def __eq__(self, other):
      return fl_eq(self.x, other.x) and fl_eq(self.y, other.y)
   def __ne__(self, other):
      return not self == other #self.__eq__(self, other)


class Circle():
   def __init__(self, x, y, radius):
      self.center = Point(x, y)
      self.radius = radius

