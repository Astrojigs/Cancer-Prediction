from tensorflow import keras
from data import train_labels_arr_final, train_data_arr_final

cancer_model = keras.Sequential([
    keras.layers.Dense(6, input_shape=(1, 9), activation='relu'),
    keras.layers.Dense(4, activation='relu'),
    keras.layers.Dense(3, activation='relu'),
    keras.layers.Dense(5, activation='softmax')])
cancer_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

cancer_model.fit(train_data_arr_final, train_labels_arr_final, epochs=100)
cancer_model.save('cancer_model.h5', overwrite=True)
