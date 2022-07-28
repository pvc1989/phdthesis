#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Songti SC']

def S(seconds):
  return seconds[0] / seconds

def E(seconds, n_cores):
  return seconds[0] / seconds / n_cores

if __name__ == '__main__':
  n_cores = np.array([1, 20, 40, 60, 80, 100])
  t100 = np.array([17652.2, 960.443, 491.070, 335.651, 251.548, 202.789])
  t199 = np.array([35324.5, 1912.365, 971.710, 666.548, 494.541, 397.641])
  t200 = np.array([35519.3, 1926.584, 983.933, 676.930, 504.951, 408.126])

  plt.figure(figsize=(6,3))
  plt.grid()
  plt.xlabel('分块/进程/核心数量')
  plt.ylabel('加速比')
  plt.plot(n_cores, n_cores, 'r-', label='理想值')
  plt.plot(n_cores, S(t199 - t100), 'bo-', label='无读写')
  plt.plot(n_cores, S(t200 - t100), 'gx-', label='含读写')
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('./speedup.pdf')

  plt.figure(figsize=(6,3))
  plt.grid()
  plt.xlabel('分块/进程/核心数量')
  plt.ylabel('并行效率 (%)')
  plt.plot(n_cores, E(t199 - t100, n_cores) * 100, 'bo-', label='无读写')
  plt.plot(n_cores, E(t200 - t100, n_cores) * 100, 'gx-', label='含读写')
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('./efficiency.pdf')
