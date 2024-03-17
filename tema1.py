import random
import math


def get_machine_precision():
    u = 0.1
    m = 0
    while 1 + u != 1:
        u = u / 10
        m += 1

    return m


machine_precision = 10 ** (-get_machine_precision())
# Exercitiu 1
print(machine_precision)

x = 1.0
y = machine_precision
z = machine_precision
# Exercitiu 2
print((x + y) + z == x + (y + z))
print((0.1 * 0.2) * 0.3 == 0.1 * (0.2 * 0.3))


def T(i, a):
    if i == 4:
        return (105 * a - 10 * pow(a, 3)) / (105 - 45 * pow(a, 2) + pow(a, 4))
    elif i == 5:
        return (945 * a - 105 * pow(a, 3) + pow(a, 5)) / (945 - 420 * pow(a, 2) + 15 * pow(a, 4))
    elif i == 6:
        return (10395 * a - 1260 * pow(a, 3) + 21 * pow(a, 5)) / (
                10395 - 4725 * pow(a, 2) + 210 * pow(a, 4) - pow(a, 6))
    elif i == 7:
        return (135135 * a - 17325 * pow(a, 3) + 378 * pow(a, 5) - pow(a, 7)) / (
                135135 - 62370 * pow(a, 2) + 3150 * pow(a, 4) - 28 * pow(a, 6))
    elif i == 8:
        return (2027025 * a - 27027 * pow(a, 3) + 6930 * pow(a, 5) - 36 * pow(a, 7)) / (
                2027025 - 945945 * pow(a, 2) + 51975 * pow(a, 4) - 630 * pow(a, 6) + pow(a, 8))
    elif i == 9:
        return (34459425 * a - 4729725 * pow(a, 3) + 135135 * pow(a, 5) - 990 * pow(a, 7) + pow(a, 9)) / (
                34459425 - 16216200 * pow(a, 2) + 945945 * pow(a, 4) - 13860 * pow(a, 6) + 45 * pow(a, 8))


def sin(i, a):
    return T(i, a) / (1 + T(i, a)) ** 0.5


def cos(i, a):
    return 1 / (1 + T(i, a)) ** 0.5


def generate_random():
    return random.uniform(-1 * math.pi / 2, math.pi / 2)


tanErrors = {}
sinErrors = {}
cosErrors = {}
for function in range(4, 10):
    tanErrors[function] = 0
    sinErrors[function] = 0
    cosErrors[function] = 0

for iteration in range(100001):
    test_case = generate_random()
    for function in range(4, 10):
        tanErrors[function] = tanErrors[function] + abs(T(function, test_case) - math.tan(test_case))
        sinErrors[function] = sinErrors[function] + abs(sin(function, test_case) - math.sin(test_case))
        cosErrors[function] = cosErrors[function] + abs(cos(function, test_case) - math.cos(test_case))

tanResults = [(k, v / 10000) for k, v in tanErrors.items()]
tanResults = sorted(tanResults, key=lambda pair: pair[1])

sinResults = [(k, v / 10000) for k, v in sinErrors.items()]
sinResults = sorted(sinResults, key=lambda pair: pair[1])

cosResults = [(k, v / 10000) for k, v in cosErrors.items()]
cosResults = sorted(cosResults, key=lambda pair: pair[1])

print(tanResults)
print(sinResults)
print(cosResults)
