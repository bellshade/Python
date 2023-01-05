# implementasi algoritma gradient descent untuk meminimalkan cost dari
# fungsi hipotesis linear
import numpy

train_data = (
    ((5, 2, 3), 15),
    ((6, 5, 9), 25),
    ((11, 12, 13), 41),
    ((1, 1, 1), 8),
    ((11, 12, 13), 41),
)
test_data = (((515, 22, 13), 555), ((61, 35, 49), 150))
parameter_vector = [2, 4, 1, 5]
m = len(train_data)
LEARNING_RATE = 0.009


def _error(contoh_no, data_set="train"):
    """
    parameter:
        data_set: train data
        contoh_no: contoh nomor  yang kesalahannya
                    harus diperiksa
    """
    return kalkulasi_nilai_hipotesis(contoh_no, data_set) - output(contoh_no, data_set)


def _nilai_hipotesis(data_input_tuple):
    """
    menghitung nilai fungsi hipotesis untuk
    masukan masukan tertentu
    parameter:
        data_input_tuple: input data tuple
    return:
        nilai fungsi hipotesis pada saat itu
        perhatikan bahwa ada input bias yang nilainya
        ditetapkan sebagai 1.
        itu tidak secara eksplisit disebutkan dalam data
        input.
    """
    hyp_val = 0
    for i in range(len(parameter_vector) - 1):
        hyp_val += data_input_tuple[i] * parameter_vector[i + 1]
    hyp_val += parameter_vector[0]
    return hyp_val


def output(contoh_no, data_set):
    """
    parameter:
        data_set: train data
        contoh_no: contoh nilai keluaran yang  akan
                    diambil
    return:
        output dari contoh data
    """
    if data_set == "train":
        return train_data[contoh_no][1]
    elif data_set == "test":
        return test_data[contoh_no][1]


def kalkulasi_nilai_hipotesis(contoh_no, data_set):
    """
    menghitung nilai hipotesis untuk contoh yang diberikan
    param:
        data_set : train data
        contoh_no: contoh nilai yang akan dihitung
    return:
        nilai dari contoh yang diberikan
    """
    if data_set == "train":
        return _nilai_hipotesis(train_data[contoh_no][0])
    elif data_set == "test":
        return _nilai_hipotesis(test_data[contoh_no][0])


def jumlah_nilai_derivatif(index, end=m):
    """
    menghitung jumlah turunan fungsi
    parameter:
        index: turunan index wrt yang akan
                dihitung
        end: nilai dimana penjumlahan berakhir, standarnya
                adalah m
    """
    summtion_value = 0
    for i in range(end):
        if index == -1:
            summtion_value += _error(i)
        else:
            summtion_value += _error(i) * train_data[i][0][index]
    return summtion_value


def hasil_nilai_derivatif(index):
    """
    jika index adalah -1, ini berarti kit akn menghitung penjumlahan
    bias
    """
    nilai_derivatif = jumlah_nilai_derivatif(index, m) / m
    return nilai_derivatif


def gradient_descent():
    global parameter_vector
    absolute_error_limit = 0.000002
    relative_error_limit = 0
    j = 0
    while True:
        j += 1
        temp_parameter_vector = [0, 0, 0, 0]
        for i in range(0, len(parameter_vector)):
            cost_derivatif = hasil_nilai_derivatif(i - 1)
            temp_parameter_vector[i] = (
                parameter_vector[i] - LEARNING_RATE * cost_derivatif
            )
        if numpy.allclose(
            parameter_vector,
            temp_parameter_vector,
            atol=absolute_error_limit,
            rtol=relative_error_limit,
        ):
            break
        parameter_vector = temp_parameter_vector
    print(("nilai iterasi: ", j))


def test_gradient_descent():
    for i in range(len(test_data)):
        print(("nilai aktual: ", output(i, "test")))
        print(("nilai hipotesis: ", kalkulasi_nilai_hipotesis(i, "test")))


if __name__ == "__main__":
    gradient_descent()
    print("\ntesting gradient descent untuk fungsi hipotesis linear.\n")
    test_gradient_descent()
