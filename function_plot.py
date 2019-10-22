#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 100, 0.1)
y = x ** (-3) + x ** (-1) + 1

plt.plot(x, y)
plt.show()

print("你好，numpy")
