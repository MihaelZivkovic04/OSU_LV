import numpy as np
import matplotlib.pyplot as plt


img = plt.imread("road.jpg")
img = img[:,:,0].copy()

print(img.shape)
print(img.dtype)

#img = img[:] + 80

plt.figure()
plt.imshow(img, cmap ="gray")
plt.show()