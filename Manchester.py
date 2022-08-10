import matplotlib.pyplot as plt
import numpy as np


def Manchester(data):

    y = []
    l = len(data)

    if data[0] == '0':
        y.append(1)
    if data[0] == '1':
        y.append(-1)

    for i in range(l):
        if data[i] == '0':
            y.append(1)
            y.append(-1)
        if data[i] == '1':
            y.append(-1)
            y.append(1)
    return y


data = input("Provide a binary sequence: ")
y = Manchester(data)
x = np.arange(0, 2*len(data)+1, 1)


plt.step(x, y)
plt.show()
