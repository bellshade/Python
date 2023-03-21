# kmeans clutsering adalah salah satu algoritma
# unsupervised learning yang sangat populer digunakan
# algoritma ini di desain untuk memungkinkan untuk
# mengelompokkan datake dalam  grup yang berbeda dengan
# cara yang lebih mudah berdasarkan variable tertentu
# tanpa melakukan proses training
# algoritma k means mengambil  dataset yang tidak berlabel
# sebagai input, kemudian menmbagi dataset menjadi sejumlah
# k clutser, dan mengulangi proses tersebut sampai tidak
# menemukan clutser terbaik. maka nilai K harus ditentukan
# sebelumnya dalam algoritma ini.
# tugas utama dari kmeans ini antara lain:
# 1. menentukan nilai  terbaik untuk titik pusat K atau
#   centroid dengan proses perulangan
# 2. menetapkan setiap titik data ke pusat k terdekat.
#   titik yang dekat dengan pusat k tertentu
import numpy as np
import pandas as pd
import warnings
from sklearn.metrics import pairwise_distances
from matplotlib import pyplot as plt

warnings.filterwarnings("ignore")
TAG = "K-MEANS-CLUTSER/ "


def dapatkan_inisial_centroid(data, k, seed=None):
    """
    pilih secara acak titik  k sebagai centroid awal
    """
    if seed is not None:
        np.random.seed(seed)
    n = data.shape[0]

    # memilih indeks k dari rentang data [0 , N]
    indeks_k = np.random.randint(0, n, k)

    # tahan centroid sebagai format padat, karena
    # banyak entri akan menjadi bukan nol karena
    # nilai rata-rata. selama tidaknya satu dokumen
    # dalam klutser  berisi kata, itu kana membawa
    # bobot bukan nol dalam  vektor TF-IDF dari centroid
    centroid = data[indeks_k, :]
    return centroid


def combine_centroid(x, centroid):
    return dapatkan_inisial_centroid(x, centroid, metric="euclidean")


def assign_model_clutser(data, centroid):
    #  hitung jarak antara setiap titik data dan kumpulan
    # centroid
    jarak_antara_centroid = combine_centroid(data, centroid)
    assign_clutser = np.argmin(jarak_antara_centroid, axis=1)
    return assign_clutser


def fixing_centroid(data, k, assign_clutser):
    centroid_baru = []
    for i in range(k):
        # pilih semua titik data yang termasuk dalam klutser
        # isi bagian yang kososng
        member_data_points = data[assign_clutser == 1]
        centroid = member_data_points.mean(axis=0)
        centroid_baru.append(centroid)
    centroid = np.array(centroid_baru)
    return centroid_baru


def hitung_heterogenity(data, k, centroid, clutser_assign):
    heterogenity = 0.0
    # pilih semua titik datayang termasuk dalam klutser
    for i in range(k):
        member_data_points = data[clutser_assign == i, :]

        # check member data poin apakah  tidak kosong
        if member_data_points.shape[0] > 0:
            jarak = pairwise_distances(
                member_data_points, [centroid[i]], metric="euclidean"
            )
            pengelompokkan_jarak = jarak**2
            heterogenity += np.sum(pengelompokkan_jarak)

    return heterogenity


def plot_heteroginity(heterogenity, k):
    plt.figure(figsize=(7, 4))
    plt.plot(heterogenity, linewidth=4)
    plt.xlabel("# iterasi")
    plt.ylabel("heterogenity")
    plt.title(f"klutser, K={k:d}")
    plt.rcParams.update({"font.size": 16})
    plt.show()


def kmeans(
    data, k, inisial_centroid, maxiter=500, var_hitung_heterogenity=None, verbose=False
):
    centroid = inisial_centroid[:]
    prev_assign_clutser = None

    for itr in range(maxiter):
        if verbose:
            print(itr, end="")

        # buat tugas clutser menggunakan centroid
        # terdekat
        assign_clutser = assign_model_clutser(data, centroid)

        # hitung centroid baru untuk setiap klutser k, rata-ratakan
        # semua data
        # poin yang ditetapkan ke klutser tersebut
        centroid = fixing_centroid(data, k, assign_clutser)

        if (prev_assign_clutser is not None) and (
            prev_assign_clutser == assign_clutser
        ).all():
            break

        # tampilkan jumlah dari assignment terbaru
        if prev_assign_clutser is not None:
            angka_berubah = np.sum(prev_assign_clutser != assign_clutser)
            if verbose:
                print(f"{angka_berubah:5d} elemen berbuah")
        if var_hitung_heterogenity is not None:
            skor = hitung_heterogenity(data, k, centroid, assign_clutser)
            var_hitung_heterogenity.append(skor)

    return centroid, assign_clutser


if False:
    from sklearn import dataset as ds

    dataset = ds.load_iris()
    k = 3
    heterogenity = []
    inisial_centroid = dapatkan_inisial_centroid(dataset["data"], k, seed=0)
    centroid, assign_clutser = kmeans(
        dataset["data"],
        k,
        inisial_centroid,
        maxiter=400,
        hitung_heterogenity=heterogenity,
        verbose=True,
    )
    plot_heteroginity(heterogenity, k)


def report_generator(
    df: pd.DataFrame, clutsering_variable: np.ndarray, fill_missing_report=None
) -> pd.DataFrame:
    # isi daata yang hilang dengan rule yang diberikan
    if fill_missing_report:
        df = df.fillna(value=fill_missing_report)
    df["dummy"] = 1
    numeric_cols = df.select_dtypes(np.number).columns
    report = (
        df.groupby(["Clutser"])[numeric_cols]
        .agg(
            [
                ("sum", np.sum),
                ("mean_with_zeros", lambda x: np.mean(np.nan_to_num(x))),
                ("mean_without_zeros", lambda x: x.replace(0, np.NaN).mean()),
                (
                    "mean_25-75",
                    lambda x: np.mean(
                        np.nan_to_num(
                            sorted(x)[
                                round(len(x) * 25 / 100) : round(len(x) * 75 / 100)
                            ]
                        )
                    ),
                ),
                ("mean_with_na", np.mean),
                ("min", lambda x: x.min()),
                ("5%", lambda x: x.quantile(0.05)),
                ("25%", lambda x: x.quantile(0.25)),
                ("50%", lambda x: x.quantile(0.50)),
                ("75%", lambda x: x.quantile(0.75)),
                ("95%", lambda x: x.quantile(0.95)),
                ("max", lambda x: x.max()),
                ("count", lambda x: x.count()),
                ("stdev", lambda x: x.std()),
                ("mode", lambda x: x.mode()[0]),
                ("median", lambda x: x.median()),
                ("# > 0", lambda x: (x > 0).sum()),
            ]
        )
        .T.reset_index()
        .rename(index=str, columns={"level_0": "Features", "level_1": "Type"})
    )
    # menghitung ukuran dari klutser
    clutsersize = report["ClutserSize"]
    clutsersize.Features = "# of Customer"
    clutserproportion = pd.DataFrame(
        clutsersize.iloc[:, 2:].values / clutsersize.iloc[:, 2:].values.sum()
    )
    clutserproportion["Type"] = "% of Customer"
    clutserproportion["Features"] = "ClutserProportion"
    cols = clutserproportion.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    clutserproportion = clutserproportion[cols]
    clutserproportion.columns = report.column
    a = pd.DataFrame(
        abs(
            report[report["Type"] == "count"].iloc[:, 2:].values
            - clutsersize.iloc[:, 2:].values
        )
    )
    # menghasilkan df dengan hitungan nilai nan
    a["Features"] = 0
    a["Type"] = "# of nan"
    # menigisi nilai agar sesuai dengan report
    a.Features = report[report["Type"] == "count"].Features.tolist()
    cols = a.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    # mengatur ulang kolom untuk mencocokkan laporan
    a = a[cols]
    # ganti nama kolom agar cocok dengan laporan
    a.columns = report.columns
    report = report.drop(report[report.Type == "count"].index)
    report = pd.concat([report, a, clutsersize, clutserproportion], axis=0)
    report["Mark"] = report["Features"].isin(clutsering_variable)
    cols = report.columns.tolist()
    cols = cols[0:2] + cols[-1:] + cols[2:-1]
    report = report[cols]
    sorter1 = {
        "ClusterSize": 9,
        "ClusterProportion": 8,
        "mean_with_zeros": 7,
        "mean_with_na": 6,
        "max": 5,
        "50%": 4,
        "min": 3,
        "25%": 2,
        "75%": 1,
        "# of nan": 0,
        "# > 0": -1,
        "sum_with_na": -2,
    }
    report = (
        report.assign(
            Sorter1=lambda x: x.Type.map(sorter1),
            Sorter2=lambda x: list(reversed(range(len(x)))),
        )
        .sort_values(["Sorter1", "Mark", "Sorter2"], ascending=False)
        .drop(["Sorter1", "Sorter2"], axis=1)
    )
    report.column.name = ""
    report = report.reset_index()
    report = report.drop(columns=["index"])
    return report


if __name__ == "__main__":
    import doctest

    doctest.testmod()
