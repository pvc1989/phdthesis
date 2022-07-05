#!/usr/bin/env python3

import sys
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':

  plt.figure(figsize=(8,3))
  plt.xlabel(r'$x$')
  plt.ylabel(r'$U$')

  x = np.linspace(0.0, 4.0, 1001)
  u = 10.0 * (x - 2.) / np.abs(x - 2.)
  u[len(u)//2] = 0.0
  plt.plot(x, u, label='Analytic Solution')

  names = ['p=3_h=2^-3', 'p=2_h=2^-3', 'p=1_h=2^-3']
  labels = [r'$p=3,\quad h\approx 2^{-3}$', r'$p=2,\quad h\approx 2^{-3}$', r'$p=1,\quad h\approx 2^{-3}$']

  data = []
  for i in range(len(names)):
    data.append(np.loadtxt(names[i]+'.csv', delimiter=',', skiprows=1))
    print(data[i].shape)
    plt.plot(data[i][:,3], data[i][:,0], label=labels[i])
  plt.grid()
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('p_vary.pdf')
