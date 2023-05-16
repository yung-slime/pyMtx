from numpy import ndarray, fromstring, reshape, linalg, dot, add

class Matrix:

    def __init__(self, rows: int, columns: int, elementsStream: str|ndarray) -> None:

        if not isinstance(rows, int):
            raise TypeError("rows got to be of type int.")
        self.rows: int = rows
        
        if not isinstance(columns, int):
            raise TypeError("columns got to be of type int.")
        self.columns: int = columns

        if not isinstance(elementsStream, str|ndarray):
            raise TypeError("elementsStream got to be of type str|ndarray.")
        self.elementsStream: str = elementsStream

        if isinstance(elementsStream, str):
            if len(self.elementsStream.split(" ")) != (rows * columns):
                raise ValueError("total elements entered != {totalEl}.".format(totalEl = rows * columns))
            self.matrix: ndarray = fromstring(self.elementsStream, dtype=int, sep=" ").reshape(self.rows, self.columns)
        elif isinstance(elementsStream, ndarray):
            self.matrix: ndarray = elementsStream

    def __str__(self) -> str:
        return str(self.matrix)

        
    def __repr__(self) -> str:
        return repr(self.matrix)
    
    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.columns == other.rows:
            return Matrix(self.rows, other.columns, dot(self.matrix, other.matrix))
    
    def __add__(self, other: "Matrix") -> "Matrix":
        if ( self.rows == other.rows ) and ( self.columns == other.columns ):
            return Matrix(self.rows, self.columns, add(self.matrix, other.matrix))
        


