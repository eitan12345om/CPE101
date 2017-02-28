class Point():
   def __init__(self, x, y):
      self.x = x
      self.y = y

class Circle():
   def __init__(self, x, y, radius):
      self.center = Point(x, y)
      self.radius = radius

