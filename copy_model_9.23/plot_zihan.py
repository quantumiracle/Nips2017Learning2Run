import matplotlib.pyplot as ply
import numpy as np


arr = np.load('reward_log.npy')
print(len(arr))
ply.plot(range(len(arr)), arr)
ply.show()
