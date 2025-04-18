import numpy as np

def simpsons_rule(f, a, b, n=10):
    """Approximate the integral of f(x) from a to b using Simpson's Rule with n slices (n must be even)."""
    if n % 2 == 1:
        n += 1  # n must be even
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 3) * (y[0] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2]) + y[n])