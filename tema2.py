import numpy as np
import numpy.linalg


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


def descompunere_LU(A):
    if not (len(A.shape) == 2 and A.shape[0] == A.shape[1]):
        return None, None, "Matricea nu are forma patratica"

    matrix_length = len(A)
    L = np.zeros((matrix_length, matrix_length))
    U = np.zeros((matrix_length, matrix_length))

    for index in range(matrix_length):
        U[index][index] = 1

    for p in range(matrix_length):
        for i in range(p, matrix_length):
            L[i][p] = A[i][p] - np.dot(L[i, :p], U[:p, p])
        for i in range(p + 1, matrix_length):
            if is_equal(L[p, p], 0):
                return None, None, "Matricea are un minor nul"
            U[p][i] = (A[p][i] - np.dot(L[p, :p], U[:p, i])) / L[p, p]

    return L, U, None


A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
L, U, err = descompunere_LU(A)
if err:
    print("Cannot decompose matrix")

print("L")
print(L)
print('U')
print(U)
print()

determinant_A = np.linalg.det(L) * np.linalg.det(U)
print("Este determinantul corect?")
print(is_equal(determinant_A, np.linalg.det(A)))
print()

def metoda_substitutiei_directe(A, b):
    n = len(A)

    x = np.zeros(n)
    for i in range(n):
        x[i] = (b[i] - sum([A[i][j] * x[j] for j in range(i)])) / A[i][i]

    return x


def metoda_substitutiei_inverse(A, b):
    n = len(A)

    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = b[i] - sum([A[i][j] * x[j] for j in range(i, n)])

    return x


b = np.array([1, 2, 3])
y = metoda_substitutiei_directe(L, b)
x_lu = metoda_substitutiei_inverse(U, y)

print("x_lu")
print(x_lu)
print()

print("|| A^init * x_LU - b^init ||_2")
print(numpy.linalg.norm(A.dot(x_lu) - b, 2))
print()

inverse = numpy.linalg.inv(A)

L_lib, U_lib, err = descompunere_LU(inverse)
y_lib = metoda_substitutiei_directe(L_lib, b)
x_lib = metoda_substitutiei_inverse(U_lib, y_lib)

print("|| x_LU - x_lib ||_2")
print(numpy.linalg.norm(x_lu - x_lib, 2))
print()

print("|| x_lu - A^-1_lib * b^init ||_2")
print(numpy.linalg.norm(x_lu - inverse.dot(b), 2))
