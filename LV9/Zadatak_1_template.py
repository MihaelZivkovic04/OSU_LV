import numpy as np
import keras
from keras import layers
from keras.datasets import cifar10
from keras.utils import to_categorical
from matplotlib import pyplot as plt


# ucitaj CIFAR-10 podatkovni skup
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# prikazi 9 slika iz skupa za ucenje
plt.figure()
for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.xticks([]),plt.yticks([])
    plt.imshow(X_train[i])

plt.show()


# pripremi podatke (skaliraj ih na raspon [0,1]])
X_train_n = X_train.astype('float32')/ 255.0
X_test_n = X_test.astype('float32')/ 255.0

# 1-od-K kodiranje
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# CNN mreza
model = keras.Sequential()
model.add(layers.Input(shape=(32,32,3)))
model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(500, activation='relu'))
# model.add(layers.Dropout(0.5)) #2. zadatak
model.add(layers.Dense(10, activation='softmax'))

#1)CNN mreza ima konvolucijeske slojeve, slojeve sažimanja,  potpuno povezani slojevi i sloj ravnanja i ima 1,122,758 parametara

model.summary()

# definiraj listu s funkcijama povratnog poziva
import os
from datetime import datetime

log_dir = os.path.join("logs", "run_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
os.makedirs(log_dir, exist_ok=True)

my_callbacks = [
    keras.callbacks.TensorBoard(
        log_dir=log_dir,
        update_freq='epoch'   # ← promjena
    )
]
    #keras.callbacks.TensorBoard(log_dir='logs/cnn_dropout', update_freq=100) #2. zadatak

    # keras.callbacks.EarlyStopping(    #z3
    #     monitor='val_loss',
    #     patience=5,
    #     verbose=1
    # ),
    # keras.callbacks.TensorBoard(
    #     log_dir='logs/cnn_es',
    #     update_freq=100
    # )



model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(
    X_train_n,
    y_train,
    epochs=40,
    batch_size=64,
    validation_split=0.1,
    callbacks=my_callbacks   # ← OVO FALI
)

score = model.evaluate(X_test_n, y_test, verbose=0)
print(f'Tocnost na testnom skupu podataka: {100.0*score[1]:.2f}')

#Zadatak 4 odgovori:
#a) velika batch size omogućuje  stabilnije učenje, ali sporije generaliziranje
# mala batch size oomogućuje rže učenje, ali više šuma (nestabilno)

#b) s manjom vrijednosti stope učenja učenje je sporije, a sa prevelikom stopom učenja proces ne kovergira

#c) ako imamo manju mrežu imat ćemo i manje parametara, učenje će biti brže ali riskiramo slabiju točnost i čak underfitting

#d) ako smanjimo veličinu skupa podataka sam proces poopćenja će biti lošiji što onda uzorkuje manju točnost 
