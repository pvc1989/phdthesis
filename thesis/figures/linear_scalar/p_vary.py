#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Songti SC']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == '__main__':

  plt.figure(figsize=(6,3))
  plt.xlabel(r'无量纲坐标 $X$')
  plt.ylabel(r'无量纲函数值 $U$')

  x = np.linspace(0.0, 4.0, 1001)
  u = 10.0 * (x - 2.) / np.abs(x - 2.)
  u[len(u)//2] = 0.0
  plt.plot(x, u, label='解析解')

  names = ['p=3_h=2^-3', 'p=2_h=2^-3', 'p=1_h=2^-3']
  labels = [r'$p=3,\quad h\approx 2^{-3}$', r'$p=2,\quad h\approx 2^{-3}$', r'$p=1,\quad h\approx 2^{-3}$']
  linestyles = ['--', '-.', ':']

  data = []
  for i in range(len(names)):
    data.append(np.loadtxt('../../../mdpi/figures/linear_scalar/'+names[i]+'.csv', delimiter=',', skiprows=1))
    print(data[i].shape)
    plt.plot(data[i][:,3], data[i][:,0], label=labels[i], linestyle=linestyles[i])
  plt.grid()
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('p_vary.pdf')
