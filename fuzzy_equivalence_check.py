import numpy as np

def fuzzy_max_min_composition(A, B):
    result = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            min_values = np.minimum(A[i], B[:, j])
            max_value = np.max(min_values)
            result[i, j] = max_value
    return result

def check_equivalence_property(R):
    R_squared = fuzzy_max_min_composition(R, R)
    return np.allclose(R, R_squared, rtol=1e-05, atol=1e-08)

def input_matrix(n, m):
    mat = []
    for i in range(n):
        row = list(map(float, input(f"Enter row {i+1}: ").split()))
        assert len(row) == m
        mat.append(row)
    return np.array(mat)

if __name__ == "__main__":
    n, m = map(int, input("Enter dimensions of matrix R (n, m): ").split())
    assert n == m, "Matrix R must be a square matrix."
    R = input_matrix(n, m)

    equivalence = check_equivalence_property(R)
    print("Matrix R:\n", R)
    if equivalence:
        print("The Fuzzy relation satisfies the equivalence property.")
    else:
        print("The Fuzzy relation does not satisfy the equivalence property.")
