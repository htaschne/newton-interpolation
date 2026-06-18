#!/usr/bin/env python3

from sys import argv


def newton(points):
    n = len(points)
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    table = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i]
                           [j - 1]) / (x[i + j] - x[i])

    return table


def build_poli(points, table):
    coefficients = table[0]

    def p(value):
        result = coefficients[0]
        product = 1.0

        for i in range(1, len(coefficients)):
            product *= value - points[i - 1][0]
            result += coefficients[i] * product

        return result

    return p


def derivative(f, h=1e-6):
    return lambda x: (f(x + h) - f(x - h)) / (2*h)


def main():
    if len(argv) < 2:
        print("usage: python3 src/newton_interpolation.py data/data.txt")
        return 1

    points = [
        tuple(map(float, line.strip().split()))
        for line in open(argv[1]).readlines()
        if line.strip()
    ]

    table = newton(points)
    p = build_poli(points, table)
    dp = derivative(p)
    ddp = derivative(dp)

    # Newton's method for finding roots:
    t = 14
    while abs(dp(t)) > 1e-6:
        t = t - dp(t) / ddp(t)

    print("time =", t)
    print("height =", p(t))

    for c in table[0]:
        print(c)


if __name__ == "__main__":
    main()
