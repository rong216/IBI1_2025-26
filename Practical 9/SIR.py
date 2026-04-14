import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Basic parameters
# --------------------------
N = 10000
beta = 0.3
gamma = 0.05
time_points = 1000

# Initial conditions
S = N - 1
I = 1
R = 0

# Store history
susceptible_history = [S]
infected_history = [I]
recovered_history = [R]

# --------------------------
# Time course simulation
# --------------------------
for _ in range(time_points):
    # Infection probability depends on:
    # beta * proportion of infected people
    infection_prob = beta * (I / N)
    infection_prob = min(max(infection_prob, 0), 1)

    # Randomly decide how many susceptible people get infected
    new_infections = np.random.binomial(S, infection_prob)

    # Randomly decide how many infected people recover
    new_recoveries = np.random.binomial(I, gamma)

    # Update counts
    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries

    # Store updated values
    susceptible_history.append(S)
    infected_history.append(I)
    recovered_history.append(R)

# --------------------------
# Plot results
# --------------------------
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(susceptible_history, label="susceptible")
plt.plot(infected_history, label="infected")
plt.plot(recovered_history, label="recovered")

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.tight_layout()

# Optional save
plt.savefig("SIR_plot.png")
plt.show()