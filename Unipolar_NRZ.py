import matplotlib.pyplot as plt
import numpy as np


def Unipolar_NRZ(data):

    l = len(data)

    x = []
    y = []

    for i in range(l+1):
        x.append(i)

    y = [int(data[0])]
    for i in range(l):
        y.append(int(data[i]))
    return y


data = input("Enter the binary sequence: ")
x = np.arange(0, len(data)+1, 1)
y = Unipolar_NRZ(data)

plt.step(x, y)
plt.show()
