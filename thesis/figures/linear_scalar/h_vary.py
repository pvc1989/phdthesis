#!/usr/bin/env python3

import sys
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':

  plt.figure(figsize=(6,3))
  plt.xlabel(r'$x$')
  plt.ylabel(r'$U$')

  x = np.linspace(1.9, 2.1, 1001)
  u = 10.0 * (x - 2.) / np.abs(x - 2.)
  u[len(u)//2] = 0.0
  plt.plot(x, u, label='Exact')

  names = ['h=2^-3', 'h=2^-4', 'h=2^-5']
  labels = [r'$h\approx 1/8$', r'$h\approx 1/16$', r'$h\approx 1/32$']

  data = []
  for i in range(len(names)):
    data.append(np.loadtxt(names[i]+'.csv', delimiter=',', skiprows=1))
    plt.plot(data[i][:,3], data[i][:,0], label=labels[i])
  plt.grid()
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('h_vary.pdf')
