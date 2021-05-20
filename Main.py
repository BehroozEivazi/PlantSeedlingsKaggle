import os
import keras
from keras.applications import Xception
from keras.layers import Dense, Flatten, Dropout
from keras.optimizers import RMSprop
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator

base_dir = "D:/dataset/images/kaggle/"
train_dir = os.path.join(base_dir, "train")
test_dir = os.path.join(base_dir, 'test')
validation_dir = os.path.join(base_dir, 'validation')
num_classes = 12
import matplotlib.pyplot as plt

conv_base = Xception(include_top=False,
                     weights='imagenet',
                     input_shape=(71, 71, 3))
print(conv_base.summary())

datagen = ImageDataGenerator(rescale=1. / 255,
                             rotation_range=0.2,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True,
                             fill_mode='nearest'
                             )

train_gen = datagen.flow_from_directory(
    train_dir,
    target_size=(71, 71),
    batch_size=20,
    class_mode='categorical'
)

test_gen = datagen.flow_from_directory(
    test_dir,
    target_size=(71, 71),
    batch_size=20,
    class_mode='categorical'
)

validation_gen = datagen.flow_from_directory(
    validation_dir,
    target_size=(71, 71),
    batch_size=20,
    class_mode='categorical'
)

model = Sequential()
model.add(conv_base)
model.add(Flatten())
model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(optimizer=RMSprop(lr=1e-4),
              loss='categorical_crossentropy',
              metrics=['acc'])

print(model.summary())

history = model.fit_generator(
    train_gen,
    steps_per_epoch=100,
    epochs=10,
    verbose=1,
    validation_data=validation_gen,
    shuffle=True,
    validation_steps=20
)

model.save('PlantSeedlings_Xception.h5')

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()
