import random


def is_equal(a, b):
    return abs(a - b) < 10 ** (-4)


def gradient_analitic(f, x, y):
    h = 10 ** -5
    dx_f = (3 * f(x, y) - 4 * f(x - h, y) + f(x - 2 * h, y)) / (2 * h)
    dy_f = (3 * f(x, y) - 4 * f(x, y - h) + f(x, y - 2 * h)) / (2 * h)

    return dx_f, dy_f


def schema_de_calcul(f, dx_f, dy_f):
    x = random.uniform(-10000, 10000)
    y = random.uniform(-10000, 10000)

    gradient = (dx_f(x, y), dy_f(x, y))
    norm = (gradient[0] ** 2 + gradient[1] ** 2) ** 0.5

    eta = 1
    p = 1
    while f(x - gradient[0], y - gradient[1]) > f(x, y) - (eta / 2) * (norm ** 2) and p < 8:
        eta = eta * 0.8
        p += 1

    x -= eta * gradient[0]
    y -= eta * gradient[1]

    k = 1
    while k < 40000 and not is_equal(eta * norm, 0) and eta * norm <= 10_000_000_000:
        gradient = (dx_f(x, y), dy_f(x, y))
        norm = (gradient[0] ** 2 + gradient[1] ** 2) ** 0.5

        eta = 1
        p = 1
        while f(x - gradient[0], y - gradient[1]) > f(x, y) - (eta / 2) * (norm ** 2) and p < 8:
            eta = eta * 0.8
            p += 1

        x -= eta * gradient[0]
        y -= eta * gradient[1]
        # print(f"{x}, {y}, {k}")

        k += 1

    if is_equal(eta * norm, 0):
        return x, y, k
    else:
        return None


def schema_calcul_analitica(f):
    x = random.uniform(-10000, 10000)
    y = random.uniform(-10000, 10000)

    gradient = gradient_analitic(f, x, y)
    norm = (gradient[0] ** 2 + gradient[1] ** 2) ** 0.5

    eta = 1
    p = 1
    while f(x - gradient[0], y - gradient[1]) > f(x, y) - (eta / 2) * (norm ** 2) and p < 8:
        eta = eta * 0.8
        p += 1

    x -= eta * gradient[0]
    y -= eta * gradient[1]

    k = 1
    while k < 40000 and not is_equal(eta * norm, 0) and eta * norm <= 10_000_000_000:
        gradient = gradient_analitic(f, x, y)
        norm = (gradient[0] ** 2 + gradient[1] ** 2) ** 0.5

        eta = 1
        p = 1
        while f(x - gradient[0], y - gradient[1]) > f(x, y) - (eta / 2) * (norm ** 2) and p < 8:
            eta = eta * 0.8
            p += 1

        x -= eta * gradient[0]
        y -= eta * gradient[1]
        # print(f"{x}, {y}, {k}")

        k += 1

    if is_equal(eta * norm, 0):
        return x, y, k
    else:
        return None


def f1(x, y):
    return x ** 2 + y ** 2 - 2 * x - 4 * y - 1


def dx_f1(x, y):
    return 2 * x - 2


def dy_f1(x, y):
    return 2 * y - 4


def f2(x, y):
    return 3 * x ** 2 - 12 * x + 2 * y ** 2 + 16 * y - 10


def dx_f2(x, y):
    return 6 * x - 12


def dy_f2(x, y):
    return 4 * y + 16


def f3(x, y):
    return x ** 2 - 4 * x * y + 5 * y ** 2 - 4 * y + 3


def dx_f3(x, y):
    return 2 * x - 4 * y


def dy_f3(x, y):
    return -4 * x + 10 * y - 4


def f4(x, y):
    return x ** 2 * y - 2 * x * y ** 2 + 3 * x * y + 4


def dx_f4(x, y):
    return 2 * x * y - 2 * y ** 2 + 3 * y


def dy_f4(x, y):
    return x ** 2 - 4 * x * y + 3 * x


print("F1")
print(schema_de_calcul(f1, dx_f1, dy_f1))
print(schema_calcul_analitica(f1))
print()

print("F2")
print(schema_de_calcul(f2, dx_f2, dy_f2))
print(schema_calcul_analitica(f2))
print()

print("F3")
print(schema_de_calcul(f3, dx_f3, dy_f3))
print(schema_calcul_analitica(f3))
print()

print("F4")
print(schema_de_calcul(f4, dx_f4, dy_f4))
print(schema_calcul_analitica(f4))
print()
