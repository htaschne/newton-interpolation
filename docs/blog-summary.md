# Newton Interpolation Project

This project was built for a numerical methods class and implements Newton interpolation using divided differences. The input is a small table of projectile height measurements over time, and the goal is to estimate the projectile's maximum height from those discrete points.

I implemented the divided-difference table, extracted the Newton coefficients, and used the resulting interpolation polynomial to evaluate the trajectory. To find the maximum height, I approximated the derivative numerically and applied Newton's method to find where the derivative is zero.

The main lesson from this project was how interpolation connects tabular data to a usable mathematical model. Newton interpolation is useful because it builds the polynomial incrementally from the data points, and the divided-difference coefficients make the structure of the polynomial clear.

The project also combines algorithm implementation with technical writing. Alongside the Python script, the repository includes the original LaTeX report explaining the method, the implementation, and the final numerical result.
