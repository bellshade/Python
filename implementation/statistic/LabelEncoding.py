from typing import Union

import numpy as np
import pandas as pd


class LabelEncoding:
    """
    Deskripsi:

    ---
    Label Enconding adalah algoritma untuk tanda setiap value
    agar bisa di kategorikan

    Example:

    ----

    """

    def __init__(self):
        self.unique_values = []
        self.label_map = {}

    def fit(self, data: Union[np.array, pd.DataFrame]):
        if isinstance(data, pd.DataFrame):
            data = data.value
        self.unique_values = np.unique(data)
        return self

    def transform(self, data: np.array):
        labels = []
        for row in data:
            row_labels = []
            for value in row:
                if value not in self.label_map:
                    self.label_map[value] = len(self.label_map)
                row_labels.append(self.label_map[value])
            labels.append(row_labels)
        return np.array(labels)


if __name__ == "__main__":
    data = np.array([[1, 2, 1, 2], [1, 2, 2, 1]])
    # df = pd.DataFrame({"S": data[0], "B": data[1]})
    label = LabelEncoding()
    label.fit(data)
    print(label.transform(data))
