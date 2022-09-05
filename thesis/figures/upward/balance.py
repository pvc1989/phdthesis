#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Songti SC']

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

  print(np.min(cells), np.max(cells))
  avg = np.mean(cells)

  plt.figure(figsize=(6,3))
  plt.bar(parts, cells, label="分布值")
  plt.plot([0, 100], [avg, avg], 'r--', label="平均值")
  plt.ylim((724, 734))
  plt.xlabel("分块/进程/核心编号")
  plt.ylabel("体单元数量")
  plt.tight_layout()
  plt.legend()
  # plt.show()
  plt.savefig('./balance.pdf')
