import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt
from PIL import Image

# ucitaj model
model = keras.models.load_model("lab8/mnist_model.h5")

# ucitaj sliku (mora biti 28x28 iz Painta)
img = Image.open("lab8/test.png").convert("L")

img_array = np.array(img)

# ako je pozadina bijela, a broj crn -> invertiraj
if np.mean(img_array) > 127:
    img_array = 255 - img_array

# skaliranje
img_array = img_array.astype("float32") / 255

# oblik
img_array = np.expand_dims(img_array, -1)
img_array = np.expand_dims(img_array, 0)

# klasifikacija
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction)

# prikaz
plt.imshow(img_array.squeeze(), cmap="gray")
plt.title(predicted_class)
plt.axis("off")
plt.show()

print("Predicted digit:", predicted_class)
