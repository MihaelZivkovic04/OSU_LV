import numpy as np
from tensorflow import keras
from matplotlib import pyplot as plt

# ucitaj model
model = keras.models.load_model("lab8/mnist_model.h5")

# ucitaj podatke
(_, _), (x_test, y_test) = keras.datasets.mnist.load_data()

x_test_s = x_test.astype("float32") / 255
x_test_s = np.expand_dims(x_test_s, -1)

# predikcije
y_pred = model.predict(x_test_s)
y_pred_classes = np.argmax(y_pred, axis=1)

# pronadi pogresno klasificirane
wrong = np.where(y_pred_classes != y_test)[0]

# prikazi nekoliko takvih slika
plt.figure(figsize=(10, 5))
for i in range(8):
    idx = wrong[i]
    plt.subplot(2, 4, i + 1)
    plt.imshow(x_test[idx], cmap="gray")
    plt.title(f"Stvarno: {y_test[idx]}, Pred: {y_pred_classes[idx]}")
    plt.axis("off")

plt.show()
