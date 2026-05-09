import os
import numpy as np
import matplotlib.pyplot as plt

# Practical 9 - spatial_SIR.py
# Pseudocode:
# 1. Create a 100 x 100 grid of susceptible individuals
# 2. Randomly select one individual to be infected
# 3. For each time point:
#    - Find all infected cells
#    - For each infected cell, check its 8 neighbours
#    - Infect susceptible neighbours with probability beta
#    - Allow infected cells to recover with probability gamma
#    - Update the grid
#    - Save selected snapshots
# 4. Plot snapshots at different time points
# 5. Save the figure to a file

# --------------------------
# Basic parameters
# 0 = susceptible
# 1 = infected
# 2 = recovered
# --------------------------
grid_size = 100
beta = 0.3
gamma = 0.05
time_points = 100

# Make population grid
population = np.zeros((grid_size, grid_size), dtype=int)

# Randomly select one infected individual
outbreak = np.random.choice(range(grid_size), 2)
population[outbreak[0], outbreak[1]] = 1

# Save snapshots for plotting
snapshots = {0: population.copy()}

# --------------------------
# Time course simulation
# --------------------------
for t in range(1, time_points + 1):
    next_population = population.copy()

    # Find infected cells
    infected_positions = np.argwhere(population == 1)

    for row, col in infected_positions:
        # Check all 8 neighbours
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue

                nr = row + dr
                nc = col + dc

                # Stay inside the grid
                if 0 <= nr < grid_size and 0 <= nc < grid_size:
                    # Infect only susceptible neighbours
                    if population[nr, nc] == 0:
                        if np.random.random() < beta:
                            next_population[nr, nc] = 1

        # Infected cell may recover
        if np.random.random() < gamma:
            next_population[row, col] = 2

    population = next_population

    if t in [10, 50, 100]:
        snapshots[t] = population.copy()

# --------------------------
# Plot snapshots
# --------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
output_plot = os.path.join(script_dir, "spatial_SIR_plot.png")

times_to_plot = [0, 10, 50, 100]
fig, axes = plt.subplots(2, 2, figsize=(8, 8), dpi=150)

for ax, t in zip(axes.flatten(), times_to_plot):
    ax.imshow(
        snapshots[t],
        cmap="viridis",
        interpolation="nearest",
        vmin=0,
        vmax=2
    )
    ax.set_title(f"Time = {t}")
    ax.set_xticks([])
    ax.set_yticks([])

plt.suptitle("Spatial SIR Model\n0 = Susceptible, 1 = Infected, 2 = Recovered")
plt.tight_layout()

plt.savefig(output_plot, dpi=300)
plt.show()