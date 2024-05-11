eps = 10 ** (-11)


def read_A(filename):
    f = open(filename, "r")

    elements_default = []
    valori = []
    ind_col = []

    t = f.readline()
    size = int(t)

    for i in range(size):
        elements_default.append([])
        valori.append([])
        ind_col.append([])

    t = f.readline()
    while t is not None and t.strip() != "":
        values = t.split(",")

        value = float(values[0].strip())
        i_index = int(values[1].strip())
        j_index = int(values[2].strip())

        # Default
        element_exists = False
        for j in range(len(elements_default[i_index])):
            if elements_default[i_index][j][1] == j_index:
                element_exists = True
                elements_default[i_index][j][0] += value
                if abs(elements_default[i_index][j][0]) < eps:
                    elements_default[i_index].remove(elements_default[i_index][j][0])
                break

        if not element_exists:
            elements_default[i_index].append([value, j_index])

        # Val + Col
        element_exists = False
        for j in range(len(ind_col[i_index])):
            if ind_col[j] == j_index:
                element_exists = True
                valori[i_index][j] += value
                if abs(valori[i_index][j]) < eps:
                    valori[i_index].remove(valori[i_index][j])
                    ind_col[i_index].remove(j_index)
                break

        if not element_exists:
            valori[i_index].append(value)
            ind_col[i_index].append(j_index)

        t = f.readline()

    f.close()

    for i in range(size):
        elements_default[i].sort(key=lambda value: value[0])

    return elements_default, valori, ind_col, size


def read_B(filename):
    f = open(filename, "r")

    b = []

    t = f.readline()

    t = f.readline()
    while t is not None and t.strip() != "":
        b.append(float(t.strip()))
        t = f.readline()

    f.close()

    return b


elements_default, valori, ind_col, size = read_A("a_1.txt")
b = read_B("b_1.txt")

has_non_null_diag = True
for i in range(0, size):
    if not has_non_null_diag:
        break
    for element in elements_default[i]:
        if element[1] == i:
            if abs(element[0]) < eps:
                has_non_null_diag = False
            break

print(has_non_null_diag)
if not has_non_null_diag:
    exit(1)


def formula_3(reprezentare, x_ds):
    norm = 0

    if reprezentare == 1:
        for i in range(size):
            elem_diag = None
            suma_default = 0
            for element in elements_default[i]:
                if element[1] == i:
                    elem_diag = element[0]
                else:
                    suma_default += element[0] * x_ds[element[1]]

            value_default = (b[i] - suma_default) / elem_diag
            norm += (value_default - x_ds[i]) ** 2
            x_ds[i] = value_default
    elif reprezentare == 2:
        for i in range(size):
            elem_diag = None
            suma_default = 0
            for element, col in zip(valori[i], ind_col[i]):
                if col == i:
                    elem_diag = element
                else:
                    suma_default += element * x_ds[col]

            value_default = (b[i] - suma_default) / elem_diag
            norm += (value_default - x_ds[i]) ** 2
            x_ds[i] = value_default

    return norm ** 0.5


def calculate_norm(a, b):
    norm = 0
    for i in range(size):
        norm += (a[i] - b[i]) ** 2
    norm = norm ** 0.5

    return norm


def gauss_seidel(matrice):
    k = 1
    x_ds = [float(i) for i in range(1, size + 1)]
    norm = formula_3(matrice, x_ds)

    while eps <= norm <= 100000000 and k < 10000:
        norm = formula_3(matrice, x_ds)
        k += 1

    if norm < eps:
        return x_ds, k
    else:
        return None


x, iterations = gauss_seidel(2)
print(x)
print(iterations)

A_x_gs_default = []
A_x_gs_secondary = []
for i in range(size):
    elem_default = 0
    for element in elements_default[i]:
        elem_default += element[0] * x[element[1]]
    A_x_gs_default.append(elem_default)

    elem_secondary = 0
    for j in range(len(valori[i])):
        elem_secondary += valori[i][j] * x[ind_col[i][j]]
    A_x_gs_secondary.append(elem_secondary)

norm_default = sum([(A_x_gs_default[i] - b[i]) ** 2 for i in range(size)]) ** 0.5
norm_secondary = sum([(A_x_gs_secondary[i] - b[i]) ** 2 for i in range(size)]) ** 0.5

print(norm_default)
print(norm_secondary)

a, _, _, size = read_A("a.txt")
b, _, _, _ = read_A("b.txt")
aplusb, _, _, _ = read_A("aplusb.txt")

for i in range(size):
    for j in range(len(b[i])):
        is_in_a = False

        for k in range(len(a[i])):
            if b[i][j][1] == a[i][k][1]:
                is_in_a = True
                a[i][k][0] += b[i][j][0]
                break

        if not is_in_a:
            a[i].append([b[i][j][0], b[i][j][1]])

for i in range(size):
    for element1 in aplusb[i]:
        has_element = False
        for element2 in a[i]:
            if element1[0] == element2[0] and element1[1] == element2[1]:
                has_element = True

        if not has_element:
            print(element1)
            print("Diferite")

print("Sunt la fel")
