import math
import numpy as np

from light import Light

class Vector:
  def __init__(self, x, y, z) -> None:
    self.x = x
    self.y = y
    self.z = z

class Sphere:
  def __init__(self, radius: int, position: tuple[float,float,float], color: tuple[int,int,int]) -> None:
    self.radius = radius
    self.position = position # (x,y,z)
    self.color = color

  def overlaps(self, point_position: tuple[float, float, float]) -> bool:
    d = math.sqrt((self.position[0] - point_position[0])** 2 + (self.position[1] - point_position[1])**2)
    return d < self.radius

  def light_coeff(self, point: tuple[int, int], light: Light) -> float:
    dx = point[0] - self.position[0]
    dy = point[1] - self.position[1]

    try:
      z = self.position[2] + math.sqrt(self.radius**2 - dx**2 - dy**2)
    except ValueError:
      return 0

    v1 = Vector(dx, dy, z-self.position[2])
    v2 = Vector(light.position[0] - point[0],
                light.position[1] - point[1],
                light.position[2] - z)

    numerator = (v1.x * v2.x + v1.y * v2.y + v1.z * v2.z)
    denominator = math.sqrt(v1.x**2 + v1.y**2 + v1.z**2) * math.sqrt(v2.x**2 + v2.y**2 + v2.z**2)

    coeff = numerator/denominator

    return coeff if coeff > 0 else 0



