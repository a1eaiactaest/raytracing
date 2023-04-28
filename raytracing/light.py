#!/usr/bin/env python3


class Light:
  def __init__(self, position: tuple[float,float,float], color: tuple[int,int,int]) -> None:
    self.position = position
    self.colors = color
