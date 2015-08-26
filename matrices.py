from __future__ import division

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0] if A else 0)
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_col(A, i):
    return [row[i] for row in A] #ith element of row for each row in A

def make_matrix(num_rows, num_cols, entry_fn):
    """return a num_rows x num_cols matrix
    whose (i,j)th entry is entryfn(i,j)"""
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]

def make_diagonal(x, y):
    return 1 if x == y else 0

def main():
    A = [[1,2], [3,4]]
    print(shape(A)) # (2,2)
    print(get_row(A, 0)) # [1,2]
    print(get_col(A, 0)) # [1,3]
    print(make_matrix(2,2,lambda x, y: 0))  # [[0,0], [0,0]]
    print(make_matrix(4,4,make_diagonal))   # [[1, 0, 0, 0, 0],
                                            #  [0, 1, 0, 0, 0],
                                            #  [0, 0, 1, 0, 0],
                                            #  [0, 0, 0, 1, 0],
                                            #  [0, 0, 0, 0, 1]]
    print(make_matrix(2,6, lambda x, y: 0)) #  [[0,0,0,0,0,0],
                                            #   [0,0,0,0,0,0]]

if __name__ == "__main__":
    main()
