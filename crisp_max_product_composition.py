import numpy as np

def crisp_max_product_composition(A, B):
    result = np.zeros((A.shape[0], B.shape[1]), dtype=int)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            product_values = np.multiply(A[i], B[:, j])
            max_value = np.max(product_values)
            result[i, j] = max_value
    return result

def input_matrix(n, m):
    mat = []
    for i in range(n):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        assert len(row) == m
        mat.append(row)
    return np.array(mat)

if __name__ == "__main__":
    n, m = map(int, input("Enter dimensions of matrix A (n, m): ").split())
    A = input_matrix(n, m)
    m, p = map(int, input("Enter dimensions of matrix B (m, p): ").split())
    B = input_matrix(m, p)

    result = crisp_max_product_composition(A, B)
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    print("Crisp max-product composition:\n", result)
