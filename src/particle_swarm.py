import numpy as np
from pyswarm import pso

# Define the Mishra 8 function
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

def swarm_solver(seed=42):
    # Set np seed to reproduce results
    np.random.seed(seed)
    
    # Set bounds
    lb = [-10, -10]  # Lower bounds
    ub = [10, 10]    # Upper bounds

    # Get solution using particle swarm
    return pso(mishra_8, lb, ub, swarmsize=1000, maxiter=1000, debug=False)



# Print the results
if __name__ == "__main__":

    variables, evaluation = swarm_solver()

    print("Best solution found:", variables)
    print("Best objective value:", evaluation)
