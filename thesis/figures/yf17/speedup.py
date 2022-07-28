#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Songti SC']

def S(seconds):
  return seconds[0] / seconds

def E(seconds, n_cores):
  return S(seconds) / n_cores

if __name__ == '__main__':
  n_cores = np.array([1, 5, 10, 15, 20, 40, 60, 80, 100])
  t100 = np.array([10511.297738, 2389.249447, 1246.371857, 839.553684, 645.736730, 325.268503, 222.890379, 168.861584, 137.786587])
  t399 = np.array([42466.453084, 9740.134833, 5086.617883, 3420.170796, 2632.321415, 1310.721133, 923.043398, 672.438984, 543.080835])
  t400 = np.array([42593.014062, 9769.956506, 5101.952423, 3430.747661, 2640.571249, 1319.734141, 931.753585, 681.444736, 552.682058])

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
  plt.plot(n_cores, E(t399 - t100, n_cores) * 100, 'bo-', label='无读写')
  plt.plot(n_cores, E(t400 - t100, n_cores) * 100, 'gx-', label='含读写')
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('./efficiency.pdf')
