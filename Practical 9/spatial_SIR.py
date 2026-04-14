import numpy as np
import matplotlib.pyplot as plt

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

# --------------------------------------------------
# PSEUDOCODE
# 1. Find all currently infected cells
# 2. For each infected cell:
#    - Check its 8 neighbours
#    - If a neighbour is susceptible, infect it with probability beta
#    - Allow the infected cell to recover with probability gamma
# 3. Update the grid
# 4. Save selected time points for plotting
# --------------------------------------------------
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
                    # Only susceptible neighbours can be infected
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
times_to_plot = [0, 10, 50, 100]

fig, axes = plt.subplots(2, 2, figsize=(8, 8), dpi=150)

for ax, t in zip(axes.flatten(), times_to_plot):
    ax.imshow(snapshots[t], cmap="viridis", interpolation="nearest", vmin=0, vmax=2)
    ax.set_title(f"time = {t}")
    ax.set_xticks([])
    ax.set_yticks([])

plt.suptitle("Spatial SIR model")
plt.tight_layout()
plt.savefig("spatial_SIR_plot.png")
plt.show()