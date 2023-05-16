from numpy import ndarray, fromstring, reshape

class Matrix:

    def __init__(self, rows: int, columns: int, elementsStream: str) -> None:

        if not isinstance(rows, int):
            raise TypeError("rows got to be of int type.")
        self.rows: int = rows
        
        if not isinstance(columns, int):
            raise TypeError("columns got to be of int type.")
        self.columns: int = columns

        if not isinstance(elementsStream, str):
            raise TypeError("elementsStream got to be of str type.")
        self.elementsStream: str = elementsStream

        if len(self.elementsStream.split(" ")) != (rows * columns):
            raise ValueError("total elements entered != {totalEl}.".format(totalEl = rows * columns))
        self.matrix: ndarray = fromstring(self.elementsStream, dtype=int, sep=" ").reshape(self.rows, self.columns)
    
    def __str__(self) -> str:
        return str(self.matrix)

        
    def __repr__(self) -> str:
        return repr(self.matrix)
    
    def __mul__(self, other: "Matrix") -> "Matrix":
        pass
    
    def __add__(self, other: "Matrix") -> "Matrix":
        pass

matA = Matrix(3, 2, "1 2 3 4 5 6")