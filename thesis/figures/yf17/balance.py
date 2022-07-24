#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
  parts = np.linspace(0, 99, 100)
  cells = np.array([
    5332, 5249, 5250, 5251, 5250, 5250, 5250, 5249, 5250, 5300,
    5299, 5279, 5300, 5300, 5300, 5300, 5300, 5301, 5299, 5300,
    5299, 5300, 5300, 5301, 5300, 5276, 5260, 5250, 5275, 5276,
    5275, 5331, 5277, 5277, 5277, 5276, 5276, 5276, 5276, 5276,
    5277, 5277, 5277, 5277, 5277, 5277, 5277, 5277, 5276, 5277,
    5299, 5298, 5299, 5294, 5296, 5295, 5299, 5298, 5298, 5298,
    5298, 5299, 5295, 5295, 5295, 5295, 5295, 5295, 5295, 5295,
    5295, 5295, 5295, 5295, 5294, 5299, 5300, 5300, 5299, 5299,
    5299, 5299, 5299, 5299, 5299, 5299, 5300, 5299, 5300, 5300,
    5300, 5299, 5299, 5299, 5298, 5298, 5299, 5298, 5299, 5299])

  print(np.sum(cells), np.max(cells))
  print(np.sum(cells) / 100 / np.max(cells))

  plt.figure(figsize=(6,3))
  plt.plot(parts, cells)
  plt.xlabel("Core Index")
  plt.ylabel("Number of Cells")
  plt.tight_layout()
  # plt.show()
  plt.savefig('./balance.pdf')
