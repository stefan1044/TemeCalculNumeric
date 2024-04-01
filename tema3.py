import numpy as np


def get_machine_precision():
    u = 0.1
    m = 0
    while 1 + u != 1:
        u = u / 10
        m += 1

    return m


machine_precision = 10 ** (-get_machine_precision())


def is_equal(a, b):
    return abs(a - b) < machine_precision


# Exercitiu 1
def get_bi(matrix, vec):
    n = len(vec)
    b = np.zeros(n)

    for i in range(n):
        bi = 0.0
        for j in range(n):
            bi += vec[j] * matrix[i][j] * 1.0
        b[i] = bi

    return b


n = 3

test_A = np.random.random((n, n))
A_init = test_A.copy()
test_s = np.random.random(n)

# test_A = np.array([[1.0, 2.0, 3.0],
#                    [4.0, 5.0, 6.0],
#                    [7.0, 8.0, 9.0]])
# test_s = np.array([1.0, 2.0, 3.0])

bi = get_bi(test_A, test_s)
b_init = bi.copy()
print(bi)


# Exercitiu 2
def house_holder(A, b):
    n = len(A)
    q = np.identity(n)

    for r in range(n - 1):
        sigma = 0
        for j in range(r, n):
            sigma += A[j][r] ** 2

        if sigma < machine_precision:
            return None

        k = -1 * (-1 if A[r][r] < 0 else 1) * (sigma ** 0.5)
        beta = sigma - k * A[r][r]

        u = np.zeros(n)
        for i in range(n):
            if i <= r - 1:
                continue
            elif i == r:
                u[i] = A[r][r] - k
            else:
                u[i] = A[i][r]

        for i in range(r + 1, n):
            A[i][r] = 0
        A[r][r] = k

        for j in range(r + 1, n):
            gamma = 0
            for i in range(r, n):
                gamma += u[i] * A[i][j]
            gamma = gamma / beta

            for i in range(r, n):
                A[i][j] -= gamma * u[i]

        gamma = 0.0
        for i in range(r, n):
            gamma += u[i] * b[i]
        gamma = gamma / beta
        for i in range(r, n):
            b[i] -= gamma * u[i]

        for j in range(n):
            gamma = 0
            for i in range(r, n):
                gamma += u[i] * q[i][j]
            gamma /= beta

            for i in range(r, n):
                q[i][j] -= gamma * u[i]

    Q = q.transpose()

    return A, Q, b


A, Q, b = house_holder(test_A, bi)
print("A")
print(A)
print("Q")
print(Q)
print("b")
print(b)


# Exercitiu 3

def solve_QR(A, b):
    n = len(bi)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += x[j] * A[i][j]

        x[i] = (b[i] - suma) / A[i][i]

    return x


x_householder = solve_QR(A, b)
print("x_householder")
print(x_householder)

Q_np, R_np = np.linalg.qr(A_init)

print("Q_np")
print(Q_np)
print("R_np")
print(R_np)

print(b_init)
x_QR = np.linalg.solve(R_np, np.transpose(Q_np).dot(np.array(b_init)))
print("x_QR")
print(x_QR)

print("Norma euclidiana")
print(np.linalg.norm(x_QR - x_householder, 2))
print()

# Exercitiu 4
print(np.linalg.norm(np.dot(A_init, x_householder) - b_init, 2))
print(np.linalg.norm(np.dot(A_init, x_QR) - b_init, 2))
print(np.linalg.norm(x_householder - test_s, 2) / np.linalg.norm(test_s, 2))
print(np.linalg.norm(x_QR - test_s, 2) / np.linalg.norm(test_s, 2))

# Exercitiu 5
A_inv = np.zeros((n, n))
for i in range(n):
    x = solve_QR(A, Q[i])
    for j in range(n):
        A_inv[i][j] = x[i]

print("A_householder^-1")
print(A_inv)

print("A_bibl^-1")
A_bibl_inv = np.linalg.inv(A)
print(A_bibl_inv)

print("Norma euclidiana")
print(np.linalg.norm(A_inv - A_bibl_inv, 2))
