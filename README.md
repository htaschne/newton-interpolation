# Newton Interpolation

This repository contains a numerical methods project that implements Newton interpolation using divided differences.

The program reads a table of points, builds the divided-difference table, extracts the Newton coefficients, and evaluates the resulting interpolation polynomial. In this project, the data models the height of a projectile over time and estimates the maximum height by applying Newton's method to the derivative of the interpolating polynomial.

## Repository Structure

- `src/newton_interpolation.py`: Python implementation of the interpolation and maximum-height estimate.
- `data/data.txt`: Input data with time and height pairs.
- `data/coeficientes.txt`: Newton coefficients produced for the original dataset.
- `data/results.txt`: Expected result for the original dataset.
- `docs/`: Original LaTeX report and PDFs.

## Running

From the repository root:

```sh
python3 src/newton_interpolation.py data/data.txt
```

## Input Format

The script expects a text file where each non-empty line contains one point:

```txt
time height
```

Example:

```txt
0 1.5
3 1007
7 2075
```

## Output

The script prints:

- the estimated time of maximum height;
- the estimated maximum height;
- the Newton coefficients from the first row of the divided-difference table.

For the included dataset, the expected results are stored in `data/results.txt`, and the coefficients are stored in `data/coeficientes.txt`.

## Report

The original project report is included in `docs/` as LaTeX source and PDF files.
