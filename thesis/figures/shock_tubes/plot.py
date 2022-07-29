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

  exact = np.loadtxt('../../../mdpi/figures/shock_tubes/'+case+'/exact.csv', delimiter=',')
  rkdg1 = np.loadtxt('../../../mdpi/figures/shock_tubes/'+case+'/rkdg1' + mesh + '.csv', delimiter=',', skiprows=1)
  rkdg2 = np.loadtxt('../../../mdpi/figures/shock_tubes/'+case+'/rkdg2' + mesh + '.csv', delimiter=',', skiprows=1)
  rkdg3 = np.loadtxt('../../../mdpi/figures/shock_tubes/'+case+'/rkdg3' + mesh + '.csv', delimiter=',', skiprows=1)

  plt.figure(figsize=(6,3))
  plt.xlabel(r'$x$')
  plt.ylabel(r'$\rho$')
  plt.plot(exact[0,:], exact[1,:], 'g-', label='精确解')
  plt.plot(rkdg1[:,3], rkdg1[:,0], 'b-', label=r'$p=1$')
  plt.plot(rkdg2[:,3], rkdg2[:,0], 'k-', label=r'$p=2$')
  plt.plot(rkdg3[:,3], rkdg3[:,0], 'r-', label=r'$p=3$')
  plt.grid()
  plt.legend()
  plt.tight_layout()
  # plt.show()
  plt.savefig(case + '/result' + mesh + '.pdf')
