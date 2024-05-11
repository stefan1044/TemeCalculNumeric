import math
import random


def is_equal(a, b):
    return abs(a - b) < 10 ** (-16)


def schema_horner(p, x):
    sol = p[0]
    for i in range(1, len(p)):
        sol = sol * x + p[i]

    return sol


def metoda_lui_muller(p, R):
    if R is None:
        A = float('-inf')
        for value in p:
            if value > A:
                A = value

        first_val = (p[0] if p[0] >= 0 else -p[0])

        R = (first_val + A) / first_val

    xk0 = random.uniform(-R, R)

    xk1 = random.uniform(-R, R)
    while is_equal(xk1, xk0):
        xk1 = random.uniform(-R, R)

    xk2 = random.uniform(-R, R)
    while is_equal(xk2,  xk1) or is_equal(xk2,  xk0):
        xk2 = random.uniform(-R, R)

    k = 3
    dxk = 1

    while k <= 1000 and not is_equal(dxk, 0) and math.fabs(dxk) <= 10 ** 8:
        h0 = xk1 - xk0
        h1 = xk2 - xk1

        if is_equal(h0, 0) or is_equal(h1, 0) or is_equal(h0 + h1, 0):
            print(f"Conditia h0, h1 sau h1 + h0 == 0 a esuat")
            return None

        pxk0 = schema_horner(p, xk2)
        pxk1 = schema_horner(p, xk1)
        pxk2 = schema_horner(p, xk0)

        d0 = (pxk1 - pxk2) / h0
        d1 = (pxk0 - pxk1) / h1

        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = pxk0

        if b ** 2 - 4 * a * c < 0:
            # print(f"Conditia b**2 - 4ac < 0 nu a fost indeplinita pentru {xk0}, {xk1}, {xk2}")
            return None

        delta_under = b + (1 if b > 0 else -1) * (b ** 2 - 4 * a * c) ** 0.5
        if is_equal(delta_under, 0):
            # print(f"Conditia b + sign(b) * sqrt(b**2 - 4ac) < e nu a fost indeplinita pentru {xk0}, {xk1}, {xk2}")
            return None

        dxk = (2 * c) / delta_under

        xk0 = xk1
        xk1 = xk2
        xk2 = xk2 - dxk

        k += 1

    if is_equal(dxk, 0):
        # print(f"Solutia este {xk2}")
        return xk2
    else:
        print("Diverge")
        return None



def rezolva(question):
    p, filename = question
    solutions = []
    is_solution_present = False
    x = None


    with open(filename, "r") as file:
        for line in file.readlines():
            line = line.strip()
            solutions.append(float(line))

        x = metoda_lui_muller(p, None)
        while x is None:
            x = metoda_lui_muller(p, None)

        for solution in solutions:
            if is_equal(solution, x):
                is_solution_present = True
                break

    if not is_solution_present:
        with open(filename, "a") as file:
            file.writelines(str(x) + "\n")


a1 = [1.0, -6.0, 11.0, -6], "a1"
a2 = [42, -55, -42, 49, -6], "a2"
a3 = [8, -38, 49, -22, 3], "a3"

for i in range(10000):
    rezolva(a1)
