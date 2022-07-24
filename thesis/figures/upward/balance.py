#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
  parts = np.linspace(0, 99, 100)
  cells = np.array([
    731, 729, 730, 729, 729, 729, 730, 729, 729, 730,
    730, 730, 730, 729, 729, 728, 729, 731, 731, 730,
    731, 730, 730, 731, 732, 730, 731, 731, 731, 730,
    730, 730, 730, 729, 731, 731, 731, 730, 731, 731,
    731, 731, 731, 730, 729, 728, 728, 727, 728, 728,
    728, 727, 728, 727, 727, 730, 728, 728, 728, 728,
    728, 727, 727, 727, 728, 728, 729, 727, 727, 728,
    728, 727, 727, 728, 727, 727, 727, 729, 728, 727,
    727, 727, 726, 726, 727, 726, 727, 726, 729, 727,
    727, 727, 726, 726, 726, 727, 726, 727, 726, 729])

  print(np.sum(cells), np.max(cells))
  print(np.sum(cells) / 100 / np.max(cells))

  plt.figure(figsize=(6,3))
  plt.plot(parts, cells)
  plt.xlabel("Core Index")
  plt.ylabel("Number of Cells")
  plt.tight_layout()
  # plt.show()
  plt.savefig('./balance.pdf')
