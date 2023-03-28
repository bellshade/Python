# contoh sederahana dari long short term memory
# dataset bisa dilihat pada file ``dataset_lstm.csv``
# pengertian dari lstm bisa dilihat disini
# https://en.wikipedia.org/wiki/Long_short-term_memory
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential

if __name__ == "__main__":
    # pertama menyiaapkan data yang sudah kita
    # siapkan
    df = pd.read_csv("dataset_lstm.csv", header=None)
    panjang_data = df.shape[0]

    # jika dataset yang diinputkan lain, pastikan
    # input tujun dari target dataset
    data_aktual = df.iloc[:, 1:2]
    data_aktual = data_aktual.values.reshape(panjang_data, 1)
    data_aktual = MinMaxScaler().fit_transform(data_aktual)
    data_sebelumnya = 10
    hari_berikut = 5
    periode = 20
    pembagi_data = panjang_data - periode * data_sebelumnya
    training_data = data_aktual[:pembagi_data]
    testing_data = data_aktual[pembagi_data - data_sebelumnya :]
    train_x, train_y = [], []
    test_x, test_y = [], []

    for i in range(0, len(training_data) - hari_berikut - data_sebelumnya + 1):
        train_x.append(training_data[i : i + data_sebelumnya])
        train_y.append(
            training_data[i + data_sebelumnya : i + data_sebelumnya + hari_berikut]
        )
    for i in range(0, len(testing_data) - hari_berikut - data_sebelumnya + 1):
        test_x.append(testing_data[i : i + data_sebelumnya])
        test_y.append(testing_data[i + data_sebelumnya + hari_berikut])
    x_train = np.array(train_x)
    x_test = np.array(test_x)
    y_train = np.array([list(i.ravel()) for i in train_y])
    y_test = np.array([list(i.ravel()) for i in test_y])

    model = Sequential()
    model.add(LSTM(128, input_shape=(data_sebelumnya, 1), return_sequences=True))
    model.add(LSTM(64, input_shape=(128, 1)))
    model.add(Dense(hari_berikut))
    model.compile(loss="mean_squared_error", optimizer="adam")
    history = model.fit(
        x_train, y_train, epochs=150, verbose=1, shuffle=True, batch_size=4
    )
    prediksi = model.predict(x_test)
