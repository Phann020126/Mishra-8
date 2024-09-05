from src.differential_evolution import de_solver
from src.particle_swarm import swarm_solver
import matplotlib.pyplot as plt

de_better_solutions = 0
swarm_better_solutions = 0

t = 50

x =  [i for i in range(t)]
z1 = [eval for _, eval in (de_solver(i) for i in range(t))]
z2 = [eval for _, eval in (swarm_solver(i) for i in range(t))]


# Plot both arrays
plt.plot(x, z1, marker='o', linestyle='-', color='b', label='DE')
plt.plot(x, z2, marker='x', linestyle='--', color='r', label='PSO')

# Add title and labels
plt.title('PSO vs DE')
plt.xlabel('x values')
plt.ylabel('y values')


plt.legend()

plt.grid(True)

plt.savefig("img/pso_vs_de.png")

plt.show()


