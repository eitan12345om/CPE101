from funcs_objects import distance
from objects import *

def distance_all(points):
   return [distance(point, Point(0,0)) for point in points]

def are_in_first_quadrant(points):
   return [(point.x, point.y) for point in points if point.x > 0 and point.y > 0]
