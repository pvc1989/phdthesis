#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['Songti SC']
plt.rcParams['axes.unicode_minus'] = False


if __name__ == '__main__':
  x = np.linspace(-32, 32, 33)
  markers = range(0, 11)

  plt.figure(figsize=(6,3))
  table = np.loadtxt('lift.csv', delimiter=',')
  for i in range(0, 11, 2):
    plt.plot(x, table[i], label=r'$Ma$ = {0:.1f}'.format(0.1*i), marker=markers[i])
  plt.legend()
  plt.xticks(np.arange(-32, 33, step=8))
  plt.grid()
  plt.xlabel(r'迎角 $\alpha$ (${}^\circ$)')
  plt.ylabel(r'无量纲升力系数 $C_L$')
  plt.tight_layout()
  # plt.show()
  plt.savefig('lift.pdf')

  plt.figure(figsize=(6,3))
  table = np.loadtxt('drag.csv', delimiter=',')
  for i in range(0, 11, 2):
    plt.plot(x, table[i], label=r'$Ma$ = {0:.1f}'.format(0.1*i), marker=markers[i])
  plt.legend()
  plt.xticks(np.arange(-32, 33, step=8))
  plt.grid()
  plt.xlabel(r'迎角 $\alpha$ (${}^\circ$)')
  plt.ylabel(r'无量纲阻力系数 $C_D$')
  plt.tight_layout()
  # plt.show()
  plt.savefig('drag.pdf')
