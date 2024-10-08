#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Songti SC']

def S(seconds):
  return seconds[0] / seconds

def E(seconds, n_cores):
  return S(seconds) / n_cores

if __name__ == '__main__':
  n_cores = np.array([1, 5, 10, 20, 40, 60, 80, 100])
  t100 = np.array([10027.937097, 2134.801669, 1181.787222, 591.963572, 332.974458, 199.999516, 151.947092, 120.239909])
  t399 = np.array([40132.669523, 8590.233856, 4731.575222, 2371.165143, 1236.412180, 797.041915, 602.523519, 473.891921])
  t400 = np.array([40250.367621, 8615.493931, 4745.595286, 2378.351232, 1244.408449, 804.667996, 610.336384, 482.537011])

  plt.figure(figsize=(6,3))
  plt.grid()
  plt.xlabel('分块/进程/核心数量')
  plt.ylabel('加速比')
  plt.plot(n_cores, n_cores, 'r-', label='理想值')
  plt.plot(n_cores, S(t399 - t100), 'bo-', label='无读写')
  plt.plot(n_cores, S(t400 - t100), 'gx-', label='含读写')
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('./speedup.pdf')

  plt.figure(figsize=(6,3))
  plt.grid()
  plt.xlabel('分块/进程/核心数量')
  plt.ylabel('并行效率 (%)')
  plt.ylim(80, 100)
  plt.plot(n_cores, E(t399 - t100, n_cores) * 100, 'bo-', label='无读写')
  plt.plot(n_cores, E(t400 - t100, n_cores) * 100, 'gx-', label='含读写')
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('./efficiency.pdf')
