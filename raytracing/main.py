#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from PIL import Image
import random

from sphere import Sphere
from light import Light
from colors import Colors as colors

colors_list = [
  (0, 0, 0),
  (255, 255, 255),
  (255, 0, 0),
  (0, 255, 0),
  (0, 0, 255)
]

def save_bitmap(bitmap: np.array, output_filename: str) -> None:
  im = Image.fromarray(bitmap)
  im.save("")

def create_random_bitmap(size: tuple[int,int]) -> np.array:
  return np.random.rand(*size)

def create_empty_bitmap(size: tuple[int, int]) -> np.array:
  return np.full(size, (0, 0, 0))

def generate_random_speheres(n: int) -> list[Sphere]:
  spheres = []
  for _ in range(n):
    r = random.randint(10, 50)
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    z = random.randint(0, 1000)
    print(r, x, y,)
    position = (x, y, z)
    color = colors_list[random.randint(0, len(colors_list)-1)]
    spheres.append(Sphere(r, position, color))
  return spheres

def plot_bitmap(bitmap: np.array) -> None:
  plt.imshow(bitmap)
  plt.show()

def raytrace(bitmap: np.array, scene: list[Sphere], lights: list[Light]):
  shape = bitmap.shape
  for row in range(len(bitmap)):
    for col in range(len(bitmap[row])):
      point = (col, row, 0)
      for s in scene:
        if s.overlaps(point):
          # funkcja
          coeff = s.light_coeff((row, col), lights[0])
          bitmap[row, col] = tuple(v * coeff for v in s.color)


def main() -> None:
  lights = [
    Light((800, 800, 500), colors.BLUE)
  ]

  spheres = [
    Sphere(100, (500, 500, 0), colors.BLUE),
    Sphere(50, (100, 100, 0), colors.RED),
    Sphere(200, (200, 800, 0), colors.GREEN),
  ]
  #spheres = generate_random_speheres(10)

  size = (1000,1000, 3)
  bitmap = create_empty_bitmap(size)
  raytrace(bitmap, spheres, lights)
  plot_bitmap(bitmap)

if __name__ == "__main__":
  main()