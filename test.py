import numpy as np

a = [[0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 1], [0, 0, 1, 0]]

b = np.array(a, dtype=object)

c = [[0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

d = np.array(c, dtype=object)

print(b + d)

[[0, 0, 0, 0, 2, 2, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]]