import numpy as np


def cholesky_solve(A, b):
    n = A.shape[0]

    # Step 2: Cholesky 分解
    L = np.zeros_like(A)
    for r in range(n):
        # 2.2
        L[r, r] = np.sqrt(A[r, r] - np.sum(L[r, :r] ** 2))
        # 2.3
        for i in range(r + 1, n):
            L[i, r] = (A[i, r] - np.sum(L[i, :r] * L[r, :r])) / L[r, r]

    # Step 3: 解 Ly = b
    y = np.zeros_like(b)
    for i in range(n):
        y[i] = (b[i] - np.sum(L[i, :i] * y[:i])) / L[i, i]

    # Step 4: 解 L.T x = y
    x = np.zeros_like(b)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.sum(L[i + 1:, i] * x[i + 1:])) / L[i, i]

    return L, x


if __name__ == '__main__':
    # Example usage
    A = [
        [1, -1, 4, -2, 3],
        [-1, 5, 0, 8, -1],
        [4, 0, 45, 8, 24],
        [-2, 8, 8, 18, 4],
        [3, -1, 24, 4, 39]
    ]

    b = [10, -2, 68, 8, 114]

    L1, x = cholesky_solve(np.array(A), np.array(b))
    print(L1)
    print(x)
