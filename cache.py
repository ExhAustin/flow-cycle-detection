from matplotlib import pyplot as plt
import numpy as np

graph = np.zeros([64,64])

for i in range(64):
    for j in range(64):
        graph[i][j] = 10*(i%4) + np.ceil(j/8)

plt.pcolor(graph)
plt.show()
