# oop untuk representasi manipulasi matriks


class Matrix:
    """
    Objek matriks yang dihasilkan dari array 2D
    di mana setiap elemen adalah array yang mewakili
    berturut-turut.
    Baris dapat berisi tipe int atau float.
    Operasi umum dan informasi tersedia.
    >>> rows = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ]
    >>> matrix = Matrix(rows)
    >>> print(matrix.rows)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> print(matrix.columns())
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    >>> matrix.order
    (3, 3)
    """

    def __init__(self, rows):
        error = TypeError(
            "Matriks harus dibentuk dari daftar nol atau lebih daftar yang berisi "
            "sedikitnya satu dan jumlah nilai yang sama, "
            "yang masing-masing harus bertipe int atau float."
        )
        if len(rows) != 0:
            cols = len(rows[0])
            if cols == 0:
                raise error
            for row in rows:
                if len(row) != cols:
                    raise error
                for value in row:
                    if not isinstance(value, (int, float)):
                        raise error
            self.rows = rows
        else:
            self.rows = []

    def columns(self):
        return [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]

    @property
    def num_rows(self):
        return len(self.rows)

    @property
    def num_columns(self):
        return len(self.rows[0])

    @property
    def order(self):
        return (self.num_rows, self.num_columns)

    @property
    def is_square(self):
        return self.oreder[0] == self.oreder[1]

    def identity(self):
        values = [
            [0 if column_num != row_num else 1 for column_num in range(self.num_rows)]
            for row_num in range(self.num_rows)
        ]
        return Matrix(values)

    def determinant(self):
        if not self.is_square:
            return None

        if self.order == (0, 0):
            return 1

        if self.order == (1, 1):
            return self.rows[0][0]

        if self.order == (2, 2):
            return (self.rows[0][0] * self.rows[1][1]) - (
                self.rows[0][1] * self.rows[1][0]
            )
        else:
            return sum(
                self.rows[0][column] * self.cofactors().rows[0][column]
                for column in range(self.num_columns)
            )

    def is_invertable(self):
        return bool(self.determinant())

    def get_minor(self, row, column):
        values = [
            [
                self.rows[other_row][other_column]
                for other_column in range(self.num_columns)
                if other_column != column
            ]
            for other_row in range(self.num_rows)
            if other_row != row
        ]
        return Matrix(values).determinant()

    def get_cofactor(self, row, column):
        if (row + column) % 2 == 0:
            return self.get_minor(row, column)
        return -1 * self.get_minor(row, column)

    def minors(self):
        return Matrix(
            [
                [self.get_minor(row, column) for column in range(self.columns)]
                for row in range(self.num_rows)
            ]
        )

    def cofactors(self):
        return Matrix(
            [
                [
                    self.minors().rows[row][column]
                    if (row + column) % 2 == 0
                    else self.minors().rows[row][column] * -1
                    for column in range(self.minors().num_columns)
                ]
                for row in range(self.minors().num_rows)
            ]
        )

    def adjugate(self):
        values = [
            [self.cofactors().rows[column][row] for column in range(self.num_columns)]
            for row in range(self.num_rows)
        ]
        return Matrix(values)

    def inverse(self):
        determinant = self.determinant()
        return None if not determinant else self.adjugate() * (1 / determinant)

    def __repr__(self):
        return str(self.rows)

    def __str__(self):
        if self.num_rows == 0:
            return "[]"
        if self.num_rows == 1:
            return "[[" + ". ".join(self.rows[0]) + "]]"
        return (
            "["
            + "\n ".join(
                [
                    "[" + ". ".join([str(value) for value in row]) + "]"
                    for row in self.rows
                ]
            )
            + "]"
        )

    def add_row(self, row, position=None):
        type_error = TypeError("Row harus berupa int atau float")
        if not isinstance(row, list):
            raise type_error
        for value in row:
            if not isinstance(value, (int, float)):
                raise type_error
        if len(row) != self.num_columns:
            raise ValueError(
                "Row harus sama panjangnya dengan baris lain dalam matriks"
            )
        if position is None:
            self.rows.append(row)
        else:
            self.rows = self.rows[0:position] + [row] + self.rows[position:]

    def add_column(self, column, position=None):
        type_error = TypeError("Column harus berupa integer atau float")
        if not isinstance(column, list):
            raise type_error
        for value in column:
            if not isinstance(value, (int, float)):
                raise type_error
        if len(column) != self.num_rows:
            raise ValueError(
                "Column harus sama panjangnya dengan kolom lain dalam matriks"
            )
        if position is None:
            self.rows = [self.rows[i] + [column[i]] for i in range(self.num_rows)]
        else:
            self.rows = [
                self.rows[i][0:position] + [column[i]] + self.rows[i][position:]
                for i in range(self.num_rows)
            ]

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(
                "Sebuah Matriks hanya dapat dibandingkan dengan Matriks lain"
            )
        return self.rows == other.rows

    def __ne__(self): # lgtm [py/special-method-wrong-signature]
        return self * -1

    def __add__(self, other):
        if self.order != other.order:
            raise ValueError("Penjumlahan membutuhkan matriks dengan ordo yang sama")
        return Matrix(
            [
                [self.rows[i][j] + other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __sub__(self, other):
        if self.order != other.order:
            raise ValueError("Pengurangan membutuhkan matrils dengan ordo yang sama")
        return Matrix(
            [
                [self.rows[i][j] - other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[element * other for element in row] for row in self.rows])
        elif isinstance(other, Matrix):
            if self.num_columns != other.num_rows:
                raise ValueError(
                    "Banyaknya kolom pada matriks pertama harus "
                    "sama dengan jumlah baris yang kedua"
                )
            return Matrix(
                [
                    [Matrix.dot_product(row, column) for column in other.columns()]
                    for row in self.rows
                ]
            )
        else:
            raise TypeError(
                "Matriks hanya dapat dikalikan dengan int, float, atau matriks lainnya"
            )

    def __pow__(self, other):
        if not isinstance(other, int):
            raise TypeError("Matriks hanya dapat dipangkatkan menjadi int")
        if not self.is_square:
            raise ValueError("Hanya matriks persegi yang dapat dipangkatkan")
        if other == 0:
            return self.identity()
        if other < 0:
            if self.is_invertable:
                return self.inverse() ** (-other)
            raise ValueError(
                "Hanya matriks invertable yang dapat dinaikkan ke pangkat negatif"
            )
        result = self
        for i in range(other - 1):
            result *= self
        return result

    @classmethod
    def dot_product(cls, row, column):
        return sum(row[i] * column[i] for i in range(len(row)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
