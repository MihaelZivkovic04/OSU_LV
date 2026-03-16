import numpy as np
import matplotlib.pyplot as plt

white = np.full((50, 50), 255, dtype=np.uint8)
black = np.zeros((50, 50), dtype=np.uint8)

firstRow = np.hstack((black, white))
secondRow = np.hstack((white, black))

img = np.vstack((firstRow, secondRow))

plt.figure()
plt.imshow(img, cmap ="gray")
plt.show()