#!/usr/bin/env python3

from cProfile import label
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Songti SC']

if __name__ == '__main__':
  parts = np.linspace(0, 99, 100)
  cells = np.array([
    4052, 4052, 4060, 4060, 4096, 4074, 4108, 4124, 4100, 4112,
    4070, 4110, 4064, 4110, 4126, 4134, 4138, 4072, 4128, 4122,
    4120, 4116, 4124, 4086, 4120, 4090, 4084, 4092, 4108, 4068,
    4064, 4056, 4024, 4006, 4096, 4096, 4122, 4040, 4094, 4094,
    4102, 4094, 4096, 4096, 4102, 4094, 4100, 4110, 4110, 4108,
    4038, 4124, 4064, 4078, 4092, 4108, 4036, 4120, 4124, 4082,
    4102, 4108, 4078, 4074, 4104, 4100, 4108, 4074, 4086, 4124,
    4048, 4068, 4090, 4062, 4098, 4100, 4100, 4066, 4076, 4056,
    4032, 4036, 4028, 4090, 4100, 4052, 4094, 4090, 4094, 4056,
    4058, 4030, 4110, 4100, 4102, 4096, 4094, 4102, 4100, 4108]) // 2

  print(np.min(cells), np.max(cells))
  avg = np.mean(cells)

  plt.figure(figsize=(6,3))
  plt.bar(parts, cells, label="分布值")
  plt.plot([0, 100], [avg, avg], 'r--', label="平均值")
  plt.ylim((1990, 2080))
  plt.xlabel("分块/进程/核心编号")
  plt.ylabel("体单元数量")
  plt.tight_layout()
  plt.legend()
  # plt.show()
  plt.savefig('./balance.pdf')
