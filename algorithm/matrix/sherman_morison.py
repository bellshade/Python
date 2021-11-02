class Matrix:
    """
    <class Matrix>
    struktur matrix
    """

    def __init__(self, row: int, column: int, default_value: float = 0):
        """
        <method Matrix.__init__>
        >>> a = Matrix(2, 3, 1)
        >>> a
        Matriks terdiri dari 2 baris dan 3 kolom
        [1, 1, 1]
        [1, 1, 1]
        """

        self.row, self.column = row, column
        self.array = [[default_value for c in range(column)] for r in range(row)]

    def __str__(self):
        """
        <method Matrix.__str__>
        Return string representasi dari matrix.
        """
        s = "Matriks terdiri dari %d baris dan %d kolom\n" % (self.row, self.column)

        max_element_length = 0
        for row_vector in self.array:
            for obj in row_vector:
                max_element_length = max(max_element_length, len(str(obj)))
        string_format_identifier = "%%%ds" % (max_element_length,)

        # Make string and return
        def single_line(row_vector):
            nonlocal string_format_identifier
            line = "["
            line += ", ".join(string_format_identifier % (obj,) for obj in row_vector)
            line += "]"
            return line

        s += "\n".join(single_line(row_vector) for row_vector in self.array)
        return s

    def __repr__(self):
        return str(self)

    def validateIndices(self, loc: tuple):
        """
        <method Matrix.validateIndices>
        >>> a = Matrix(2, 6, 0)
        >>> a.validateIndices((2, 7))
        False
        >>> a.validateIndices((0, 0))
        True
        """
        if not (isinstance(loc, (list, tuple)) and len(loc) == 2):
            return False
        elif not (0 <= loc[0] < self.row and 0 <= loc[1] < self.column):
            return False
        else:
            return True

    def __getitem__(self, loc: tuple):
        """
        <method Matrix.__getitem__>
        >>> a = Matrix(3, 2, 7)
        >>> a[1, 0]
        7
        """
        assert self.validateIndices(loc)
        return self.array[loc[0]][loc[1]]

    def __setitem__(self, loc: tuple, value: float):
        """
        <method Matrix.__setitem__>
        >>> a = Matrix(2, 3, 1)
        >>> a[1, 2] = 51
        >>> a
        Matriks terdiri dari 2 baris dan 3 kolom
        [ 1,  1,  1]
        [ 1,  1, 51]
        """
        assert self.validateIndices(loc)
        self.array[loc[0]][loc[1]] = value

    def __add__(self, another):
        """
        <method Matrix.__add__>
        >>> a = Matrix(2, 1, -4)
        >>> b = Matrix(2, 1, 3)
        >>> a+b
        Matriks terdiri dari 2 baris dan 1 kolom
        [-1]
        [-1]
        """

        # Validasi
        assert isinstance(another, Matrix)
        assert self.row == another.row and self.column == another.column

        result = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                result[r, c] = self[r, c] + another[r, c]
        return result

    def __neg__(self):
        """
        <method Matrix.__neg__>
        >>> a = Matrix(2, 2, 3)
        >>> a[0, 1] = a[1, 0] = -2
        >>> -a
        Matriks terdiri dari 2 baris dan 2 kolom
        [-3,  2]
        [ 2, -3]
        """

        result = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                result[r, c] = -self[r, c]
        return result

    def __sub__(self, another):
        return self + (-another)

    def __mul__(self, another):
        """
        <method Matrix.__mul__>
        >>> a = Matrix(2, 3, 1)
        >>> a[0,2] = a[1,2] = 3
        >>> a * -2
        Matriks terdiri dari 2 baris dan 3 kolom
        [-2, -2, -6]
        [-2, -2, -6]
        """

        if isinstance(another, (int, float)):  # perkalian skalar
            result = Matrix(self.row, self.column)
            for r in range(self.row):
                for c in range(self.column):
                    result[r, c] = self[r, c] * another
            return result
        elif isinstance(another, Matrix):  # perkalian matrix
            assert self.column == another.row
            result = Matrix(self.row, another.column)
            for r in range(self.row):
                for c in range(another.column):
                    for i in range(self.column):
                        result[r, c] += self[r, i] * another[i, c]
            return result
        else:
            raise TypeError(f"tipe tidak support ({type(another)})")

    def transpose(self):
        """
        <method Matrix.transpose>
        Return self^T.
        Example:
        >>> a = Matrix(2, 3)
        >>> for r in range(2):
        ...     for c in range(3):
        ...             a[r,c] = r*c
        ...
        >>> a.transpose()
        Matriks terdiri dari 3 baris dan 2 kolom
        [0, 0]
        [0, 1]
        [0, 2]
        """

        result = Matrix(self.column, self.row)
        for r in range(self.row):
            for c in range(self.column):
                result[c, r] = self[r, c]
        return result

    def ShermanMorrison(self, u, v):
        """
        <method Matrix.ShermanMorrison>
        https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula
        >>> ainv = Matrix(3, 3, 0)
        >>> for i in range(3): ainv[i,i] = 1
        ...
        >>> u = Matrix(3, 1, 0)
        >>> u[0,0], u[1,0], u[2,0] = 1, 2, -3
        >>> v = Matrix(3, 1, 0)
        >>> v[0,0], v[1,0], v[2,0] = 4, -2, 5
        >>> ainv.ShermanMorrison(u, v)
        Matriks terdiri dari 3 baris dan 3 kolom
        [  1.2857142857142856, -0.14285714285714285,   0.3571428571428571]
        [  0.5714285714285714,   0.7142857142857143,   0.7142857142857142]
        [ -0.8571428571428571,  0.42857142857142855,  -0.0714285714285714]
        """

        # validasi size matrix
        assert isinstance(u, Matrix) and isinstance(v, Matrix)
        assert self.row == self.column == u.row == v.row
        assert u.column == v.column == 1

        # Kalkulasi
        vT = v.transpose()
        numerator_factor = (vT * self * u)[0, 0] + 1
        if numerator_factor == 0:
            return None
        return self - ((self * u) * (vT * self) * (1.0 / numerator_factor))


# Testing
if __name__ == "__main__":

    def test1():
        # a^(-1)
        ainv = Matrix(3, 3, 0)
        for i in range(3):
            ainv[i, i] = 1
        print(f"a^(-1) is {ainv}")
        # u, v
        u = Matrix(3, 1, 0)
        u[0, 0], u[1, 0], u[2, 0] = 1, 2, -3
        v = Matrix(3, 1, 0)
        v[0, 0], v[1, 0], v[2, 0] = 4, -2, 5
        print(f"u is {u}")
        print(f"v is {v}")
        print("uv^T is %s" % (u * v.transpose()))
        print(f"(a + uv^T)^(-1) is {ainv.ShermanMorrison(u, v)}")

    def test2():
        import doctest

        doctest.testmod()

    test2()
