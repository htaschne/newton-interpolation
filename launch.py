#!/usr/bin/env python3

from sys import argv


def newton(ds):

    def diffdiv(a, b):
        return (ds[b][1] - ds[a][1]) / (ds[b][0] - ds[a][0])

    n = len(ds)
    c = [ds[0][1]]

    for i in range(1, n):
        for j in range(i):
            # f(x1) - f(x0) / x1 - x0
            c.append(diffdiv(j, i))

    return c



def main():
    if len(argv) < 2:
        print("please, enter the dataset")
        return 1

    ds: list[tuple[float, float]] = [
        list(map(float, line.strip().split(" ")))
        for line in open(argv[1]).readlines()
    ]

    print(ds)

    d = newton(ds)
    print(d)


if __name__ == "__main__":
    main()
