import numpy as np
import matplotlib.pyplot as plt


img = plt.imread("road.jpg")
img = img[:,:,0].copy()

print(img.shape)
print(img.dtype)

#img = img[:] + 80

#img = img[:, 160:320]

#img = np.rot90(img, k=-1)

img = np.flip(img, axis=0)

plt.figure()
plt.imshow(img, cmap ="gray")
plt.show()