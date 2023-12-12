class Matrix:
    def __init__(self, rows: int = 1, columns: int = 1):
        if rows <= 0 or columns <= 0:
            raise Exception("Error: matrix must have at least 1 row and column")
        self._contents = []
        self._rows = rows
        self._columns = columns
        for r in range(self._rows):
            self._contents.append([])
            for _ in range(self._columns):
                self._contents[r].append(0)

    def getContents(self) -> list:
        """
        Get the contents of this matrix
        :return: list of lists, each sublist is a row of this matrix
        """
        return self._contents

    def getRowNumber(self) -> int:
        """
        :return: number of rows of this matrix
        """
        return self._rows

    def getColumnNumber(self) -> int:
        """
        :return: number of columns of this matrix
        """
        return self._columns

    def getElement(self, r: int, c: int) -> float:
        """
        Returns a specific element of this matrix, given the row and the column
        :param r: row number of this matrix
        :param c: column number of this matrix
        :return: element found at this r*c cell
        """
        return self.getContents()[r][c]

    def getRow(self, r: int) -> list:
        """
        Returns a specific row of this matrix
        :param r: row number of this matrix
        :return: all elements from this r row
        """
        return self.getContents()[r]

    def getColumn(self, c: int) -> list:
        """
        Returns a specific column of this matrix
        :param c: column number of this matrix
        :return: all elements from the c column
        """
        column = []
        for r in range(self.getRowNumber()):
            e = self.getElement(r, c)
            column.append(e)
        return column

    def setElement(self, r: int, c: int, e: float):
        """
        Sets an element of this matrix with the given value
        :param r: row number of this matrix
        :param c: column number of this matrix
        :param e: new element to be set at the cell r*c
        """
        self._contents[r][c] = e

    def setRow(self, r: int, new_r: list):
        """
        Sets a row of this matrix with the given values
        :param r: row number of this matrix
        :param new_r: list of values to be set as a row
        """
        if len(new_r) != self.getColumnNumber():
            raise Exception("Error: number of elements must be equal to the number of columns")
        self._contents[r] = new_r

    def setColumn(self, c: int, new_c: list):
        """
        Sets a column of this matrix with the given values
        :param c: column number of this matrix
        :param new_c: list of values to be set as a column
        """
        if len(new_c) != self.getRowNumber():
            raise Exception("Error: number of elements must be equal to the number of rows")
        for r in range(self.getRowNumber()):
            e = new_c[r]
            self.setElement(r, c, e)

    def addRow(self, r: int):
        """
        Adds a new row to this matrix, no rows will be replaced
        :param r: location of the row
        """
        new_m = Matrix(self.getRowNumber() + 1, self.getColumnNumber())
        for i in range(0, r):
            e = self.getRow(i)
            new_m.setRow(i, e)
        row = []
        for _ in range(new_m.getColumnNumber()):
            row.append(0)
        new_m.setRow(r, row)
        for i in range(r + 1, new_m.getRowNumber()):
            e = self.getRow(i - 1)
            new_m.setRow(i, e)
        self._contents = new_m.getContents()
        self._rows += 1

    def addColumn(self, c: int):
        """
        Adds a new column to this matrix, no columns will be replaced
        :param c: location of the column
        """
        new_m = Matrix(self.getRowNumber(), self.getColumnNumber() + 1)
        for i in range(0, c):
            e = self.getColumn(i)
            new_m.setColumn(i, e)
        column = []
        for _ in range(new_m.getRowNumber()):
            column.append(0)
        new_m.setColumn(c, column)
        for i in range(c + 1, new_m.getColumnNumber()):
            e = self.getColumn(i - 1)
            new_m.setColumn(i, e)
        self._contents = new_m.getContents()
        self._columns += 1

    def removeRow(self, r: int):
        """
        Removes a row from this matrix
        :param r: number of the row
        """
        new_m = Matrix(self.getRowNumber() - 1, self.getColumnNumber())
        for i in range(0, r):
            e = self.getRow(i)
            new_m.setRow(i, e)
        for i in range(r + 1, new_m.getRowNumber() + 1):
            e = self.getRow(i)
            new_m.setRow(i - 1, e)
        self._contents = new_m.getContents()
        self._rows -= 1

    def removeColumn(self, c: int):
        """
        Removes a column from this matrix
        :param c: number of the column
        """
        new_m = Matrix(self.getRowNumber(), self.getColumnNumber() - 1)
        for i in range(0, c):
            e = self.getColumn(i)
            new_m.setColumn(i, e)
        for i in range(c + 1, new_m.getColumnNumber() + 1):
            e = self.getColumn(i)
            new_m.setColumn(i - 1, e)
        self._contents = new_m.getContents()
        self._columns -= 1

    def transpose(self):
        """
        :return: transpose of this matrix
        """
        new_m = Matrix(self.getColumnNumber(), self.getRowNumber())
        for r in range(self.getRowNumber()):
            c = self.getRow(r)
            new_m.setColumn(r, c)
        return new_m

    def copy(self):
        """
        :return: copy of this matrix
        """
        new_m = Matrix(self.getRowNumber(), self.getColumnNumber())
        for r in range(self.getRowNumber()):
            for c in range(self.getColumnNumber()):
                e = self.getElement(r, c)
                new_m.setElement(r, c, e)
        return new_m

    def isSquareMatrix(self) -> bool:
        """
        :return: true if this is a square matrix, otherwise return false
        """
        return self.getRowNumber() == self.getColumnNumber()

    def isRectangularMatrix(self) -> bool:
        """
        :return: true if this is a rectangular matrix, otherwise return false
        """
        return not self.isSquareMatrix()

    def isRowMatrix(self) -> bool:
        """
        :return: true if this is a row matrix, otherwise return false
        """
        return self.getRowNumber() == 1

    def isColumnMatrix(self) -> bool:
        """
        :return: true if this is a column matrix, otherwise return false
        """
        return self.getColumnNumber() == 1

    def isZeroMatrix(self) -> bool:
        """
        :return: true if this is a zero matrix, otherwise return false
        """
        for r in range(self.getRowNumber()):
            for c in range(self.getColumnNumber()):
                if self.getElement(r, c) != 0:
                    return False
        return True

    def isDiagonalMatrix(self) -> bool:
        """
        :return: true if this is a diagonal matrix, otherwise return false
        """
        if not self.isSquareMatrix():
            return False
        for r in range(self.getRowNumber()):
            for c in range(self.getColumnNumber()):
                if r != c and self.getElement(r, c) != 0:
                    return False
        return True

    def isScalarMatrix(self) -> bool:
        """
        :return: true if this is a scalar matrix, otherwise return false
        """
        if not self.isDiagonalMatrix():
            return False
        first_element = self.getElement(0, 0)
        for r in range(self.getRowNumber()):
            for c in range(self.getColumnNumber()):
                if r == c and self.getElement(r, c) != first_element:
                    return False
        return True

    def isIdentityMatrix(self) -> bool:
        """
        :return: true if this is an identity matrix, otherwise return false
        """
        if not self.isDiagonalMatrix() and not self.isScalarMatrix():
            return False
        for i in range(self.getRowNumber()):
            if self.getElement(i, i) != 1:
                return False
        return True

    def isSymmetric(self) -> bool:
        """
        :return: true if this matrix is symmetric, otherwise return false
        """
        return self.getContents() == self.transpose().getContents()

    @staticmethod
    def identity(i: int = 1):
        """
        Creates an identity matrix
        :param i: number of rows and columns
        :return: i*i identity matrix
        """
        if i <= 0:
            raise Exception("Error: matrix must have at least 1 row and column")
        new_m = Matrix(i, i)
        for j in range(new_m.getRowNumber()):
            new_m.setElement(j, j, 1)
        return new_m

    def __add__(self, other):
        if self.getRowNumber() != other.getRowNumber() and self.getColumnNumber() != other.getRowNumber():
            raise Exception("Error: the size of the first matrix must be equal to the size of the second matrix")
        new_m = Matrix(self.getRowNumber(), self.getColumnNumber())
        for r in range(self.getRowNumber()):
            for c in range(self.getColumnNumber()):
                e = self.getElement(r, c) + other.getElement(r, c)
                new_m.setElement(r, c, e)
        return new_m

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        def matrixMultiplication():
            def rowColumnMultiplication(new_r: list, new_c: list) -> float:
                add = 0
                for i in range(len(new_r)):
                    add += new_r[i] * new_c[i]
                return add

            if self.getColumnNumber() != other.getRowNumber():
                raise Exception("Error: the number of columns of the first matrix must be equal to the number of rows "
                                "of the second matrix")
            new_m = Matrix(self.getRowNumber(), other.getColumnNumber())
            for r in range(new_m.getRowNumber()):
                for c in range(new_m.getColumnNumber()):
                    row = self.getRow(r)
                    column = other.getColumn(c)
                    e = rowColumnMultiplication(row, column)
                    new_m.setElement(r, c, e)
            return new_m

        if type(other) is Matrix:
            return matrixMultiplication()
        new_m = Matrix(self.getRowNumber(), self.getColumnNumber())
        for r in range(self.getRowNumber()):
            for c in range(self.getColumnNumber()):
                e = self.getElement(r, c) * other
                new_m.setElement(r, c, e)
        return new_m

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power: int):
        if not self.isSquareMatrix():
            raise Exception("Error: matrix is not square")
        if power == 0:
            return Matrix.identity(self.getRowNumber())
        new_m = self.copy()
        for _ in range(power - 1):
            new_m *= self
        return new_m

    def __eq__(self, other) -> bool:
        if self.getRowNumber() != other.getRowNumber() and self.getColumnNumber() != other.getRowNumber():
            return False
        for r in range(self.getRowNumber()):
            for c in range(self.getColumnNumber()):
                if self.getElement(r, c) != other.getElement(r, c):
                    return False
        return True

    def __ne__(self, other) -> bool:
        return not self == other

    def __neg__(self):
        return self * -1

    def __str__(self) -> str:
        string = ""
        for r in range(self.getRowNumber()):
            for c in range(self.getColumnNumber()):
                string += str(self.getElement(r, c)) + " "
            string = string[:-1] + "\n"
        return string[:-1]
