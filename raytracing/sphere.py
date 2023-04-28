import math
import numpy as np

class Sphere:
  def __init__(self, radius: int, position: tuple[float,float,float], color: tuple[int,int,int]) -> None:
    self.radius = radius
    self.position = position # (x,y,z)
    self.color = color


  def overlaps(self, point_position: tuple[float, float, float]) -> bool:
    d = math.sqrt((self.position[0] - point_position[0])** 2 + (self.position[1] - point_position[1])**2)
    return d < self.radius

