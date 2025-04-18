import numpy as np
import matplotlib.pyplot as plt
from simpsons_integration import simpsons_rule

# Define 3 different functions to integrate
functions = [
    (lambda x: x**4 - 2*x + 1, 0, 2, 4.4, "x⁴ - 2x + 1"),
    (lambda x: np.sin(x), 0, np.pi, 2.0, "sin(x)"),
    (lambda x: np.exp(-x**2), -2, 2, 1.764162, "exp(-x²)")  # approximate true value
]

for i, (f, a, b, true_value, label) in enumerate(functions):
    result = simpsons_rule(f, a, b, n=10)
    error = abs((result - true_value) / true_value)
    
    # Print result
    print(f"Integral of {label} from {a} to {b}:")
    print(f"  Simpson's Rule result = {result:.6f}")
    print(f"  Fractional Error = {error:.2e}\n")

    # Plot the function
    x = np.linspace(a, b, 400)
    y = f(x)
    plt.figure()
    plt.plot(x, y, label=label)
    plt.title(f"f(x) = {label}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"plot_{i+1}.png")
    plt.close()