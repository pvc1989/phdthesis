#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Songti SC']

if __name__ == '__main__':

  n = 1001
  x = np.linspace(0.0, 4.0, n)
  u = np.zeros((2, n), dtype=float)
  for i in range(n):
    if x[i] < 1.2:
      u[0, i] = 0
      u[1, i] = 0
    elif x[i] < 2.4:
      u[0, i] = 4
      u[1, i] = 4
    else:
      u[0, i] = 12
      u[1, i] = -4

  names = ['lazy_p=2', 'eigen_p=2', 'lazy_p=3', 'eigen_p=3']
  labels = [r'$p=2, \mathtt{LazyWeno}$', r'$p=2, \mathtt{EigenWeno}$', r'$p=3, \mathtt{LazyWeno}$', r'$p=3, \mathtt{EigenWeno}$']
  linestyles = [':', '--', '-.', (0, (3, 1, 1, 1, 1, 1))]

  # figure 1
  plt.figure(figsize=(6,3))
  plt.xlabel(r'$x$')
  plt.ylabel(r"$U_1$")
  plt.plot(x, u[0], label='解析解')
  data = []
  for i in range(len(names)):
    data.append(np.loadtxt('../../../mdpi/figures/linear_system/'+names[i]+'.csv', delimiter=',', skiprows=1))
    plt.plot(data[i][:,4], data[i][:,0], linestyle=linestyles[i], label=labels[i])
  plt.grid()
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('u_1.pdf')

  # figure 2
  plt.figure(figsize=(6,3))
  plt.xlabel(r'$x$')
  plt.ylabel(r"$U_2$")
  plt.plot(x, u[1], label='解析解')
  data = []
  for i in range(len(names)):
    data.append(np.loadtxt('../../../mdpi/figures/linear_system/'+names[i]+'.csv', delimiter=',', skiprows=1))
    plt.plot(data[i][:,4], data[i][:,1], linestyle=linestyles[i], label=labels[i])
  plt.grid()
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('u_2.pdf')

  # figure 3
  fig, ax = plt.subplots(figsize=[6, 3])
  plt.xlabel(r'$x$')
  plt.ylabel("绝对误差")
  # inset axes....
  axins = ax.inset_axes([0.15, 0.6, 0.3, 0.35])
  # sub region of the original image
  axins.set_xlim(1.3, 2.2)
  axins.set_ylim(-.1, 0.5)
  data = []
  plt.plot(x, x*0, label='解析解')
  axins.plot(x, x*0)
  for i in range(len(names)):
    data.append(np.loadtxt('../../../mdpi/figures/linear_system/'+names[i]+'.csv', delimiter=',', skiprows=1))
    error = (np.abs(data[i][:,0]-u[0]) + np.abs(data[i][:,1]-u[1]))
    plt.plot(data[i][:,4], error, linestyle=linestyles[i], label=labels[i], markersize=2)
    axins.plot(data[i][:,4], error, linestyle=linestyles[i], label=labels[i], markersize=2)
  ax.indicate_inset_zoom(axins, edgecolor="black")
  plt.grid()
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig('error.pdf')
