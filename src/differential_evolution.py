import numpy as np
from scipy.optimize import differential_evolution

# Define Mishra 8 function
def mishra_8(x):
    x1, x2 = x
    term1 = (
        x1**10
        - 20    * x1**9
        + 180   * x1**8
        - 960   * x1**7
        + 3360  * x1**6
        - 8064  * x1**5
        + 1334  * x1**4
        - 15360 * x1**3
        + 11520 * x1**2
        - 5120  * x1
        + 2624
    )
    term2 = x2**4 + 12 * x2**3 + 54 * x2**2 + 108 * x2 + 81
    return 0.001 * (np.abs(term1) * np.abs(term2)) ** 2


def de_solver(seed=1):

    # Get solution using differential evolution
    solution = differential_evolution(
        mishra_8,
        bounds=[(-10, 10), (-10, 10)],
        seed=seed,
        disp=False
    )

    return solution.x, solution.fun


# Print the results
if __name__ == "__main__":

    variables, evaluation = de_solver()

    print("Best solution found:", variables)
    print("Best objective value:", evaluation)