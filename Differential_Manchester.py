import matplotlib.pyplot as plt
import numpy as np


def differential_machester(data):

    coded = []
    l = len(data)

    if data[0] == '0':
        coded.append(1)
        coded.append(-1)
        coded.append(1)
    if data[0] == '1':
        coded.append(1)
        coded.append(1)
        coded.append(-1)

    i = 1
    while i < l:
        if data[i] == '0':
            if coded[2*i] == 1:
                coded.append(-1)
                coded.append(1)
            if coded[2*i] == -1:
                coded.append(1)
                coded.append(-1)
        if data[i] == '1':
            if coded[2*i] == 1:
                coded.append(1)
                coded.append(-1)
            if coded[2*i] == -1:
                coded.append(-1)
                coded.append(1)

        i = i+1
    return coded


data = input("give the binary seuqence: ")
x = np.arange(0, 2*len(data)+1, 1)
print(x)
y = differential_machester(data)
print(y)


plt.step(x, y)
plt.show()
