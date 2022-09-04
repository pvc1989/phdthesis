#!/usr/bin/env python3

import sys
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Songti SC']

if __name__ == '__main__':
  case = sys.argv[1]
  mesh = ''
  if len(sys.argv) > 2:
    mesh = '_' + sys.argv[2]

  fig, ax = plt.subplots(figsize=[6, 3])
  plt.xlabel(r'$x$')
  plt.ylabel(r'$\rho$')

  # inset axes....
  axins = ax.inset_axes([0.55, 0.5, 0.4, 0.4])
  # sub region of the original image
  axins.set_xlim(3.3, 3.55)
  axins.set_ylim(0.23, 0.46)

  exact = np.loadtxt('../../../mdpi/figures/shock_tubes/'+case+'/exact.csv', delimiter=',')
  plt.plot(exact[0,:], exact[1,:], 'g-', label='精确解')
  axins.plot(exact[0,:], exact[1,:], 'g-')

  names = [case+'/p=1_h=2e-2'+mesh, case+'/p=2_h=55e-3'+mesh, case+'/rkdg3'+mesh]
  labels = [r'$p=1,\quad h\approx 1/50$', r'$p=2,\quad h\approx 1/18$', r'$p=3,\quad h\approx 1/10$']
  styles = ['b:', 'k-.', 'r--']
  data = []
  for i in range(len(names)):
    data.append(np.loadtxt('../../../mdpi/figures/shock_tubes/'+names[i]+'.csv', delimiter=',', skiprows=1))
    plt.plot(data[i][:,3], data[i][:,0], styles[i], label=labels[i], markersize=2)
    axins.plot(data[i][:,3], data[i][:,0], styles[i], label=labels[i], markersize=2)
  ax.indicate_inset_zoom(axins, edgecolor="black")

  plt.grid()
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig(case + '/h_vary' + mesh + '.pdf')
