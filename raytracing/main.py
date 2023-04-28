#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from sphere import Sphere
from colors import Colors as colors

def save_bitmap(bitmap: np.array, output_filename: str) -> None:
  im = Image.fromarray(bitmap)
  im.save("")

def create_random_bitmap(size: tuple[int,int]) -> np.array:
  return np.random.rand(*size)

def create_empty_bitmap(size: tuple[int, int]) -> np.array:
  return np.full(size, (0, 0, 0))

def plot_bitmap(bitmap: np.array) -> None:
  plt.imshow(bitmap)
  plt.show()

def raytrace(bitmap: np.array, scene: list[Sphere]):
  shape = bitmap.shape
  for row in range(len(bitmap)):
    for col in range(len(bitmap[row])):
      point = (col, row, 0)
      for s in scene:
        if s.overlaps(point):
          bitmap[row, col] = s.color


def main() -> None:
  spheres = [Sphere(100, (500, 500, 0), colors.BLUE), Sphere(50, (100, 100, 0), colors.RED)]

  size = (1000,1000, 3)
  bitmap = create_empty_bitmap(size)
  raytrace(bitmap, spheres)
  plot_bitmap(bitmap)


if __name__ == "__main__":
  main()