import numpy as np
import tensorflow as tf


def model_answer(mod, image):
    image = np.expand_dims(image, 0)
    image = np.expand_dims(image, -1)
    a = mod.predict(image)
    return a


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train / 255
x_test = x_test / 255

X_TRAIN = np.concatenate([x_train,
                          np.rot90(x_train, axes=(1, 2), k=1),
                          np.rot90(x_train, axes=(1, 2), k=2),
                          np.rot90(x_train, axes=(1, 2), k=3)])
Y_TRAIN = np.concatenate([y_train, y_train, y_train, y_train])

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(input_shape=(28, 28, 1), filters=32, kernel_size=(5, 5), padding='same', activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(filters=64, kernel_size=(5, 5), padding='same', activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1024, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.load_weights('weights.hdf5')  # load the weights

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# learning and creating weights
# print('shit')
# weights_file = 'weights.hdf5'
#
# model.fit(X_TRAIN.reshape(-1, 28, 28, 1), Y_TRAIN, epochs=5, batch_size=30)
# print(model.evaluate(x_test.reshape(-1, 28, 28, 1), y_test))
