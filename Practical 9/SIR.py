import os
import numpy as np
import matplotlib.pyplot as plt

# Practical 9 - SIR.py
# Pseudocode:
# 1. Define the population size and model parameters
# 2. Start with one infected person and the rest susceptible
# 3. For each time point:
#    - Calculate the infection probability
#    - Randomly infect susceptible people
#    - Randomly recover infected people
#    - Update S, I, and R
#    - Store the results
# 4. Plot susceptible, infected, and recovered over time
# 5. Save the plot to a file

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
    # Infection probability depends on beta and the proportion of infected people
    infection_prob = beta * (I / N)
    infection_prob = min(max(infection_prob, 0), 1)

    # Randomly determine new infections and recoveries
    new_infections = np.random.binomial(S, infection_prob)
    new_recoveries = np.random.binomial(I, gamma)

    # Update counts
    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries

    # Store results
    susceptible_history.append(S)
    infected_history.append(I)
    recovered_history.append(R)

# --------------------------
# Plot results
# --------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
output_plot = os.path.join(script_dir, "SIR_plot.png")

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(susceptible_history, label="Susceptible")
plt.plot(infected_history, label="Infected")
plt.plot(recovered_history, label="Recovered")

plt.xlabel("Time")
plt.ylabel("Number of people")
plt.title("Basic SIR Model")
plt.legend()
plt.tight_layout()

plt.savefig(output_plot, dpi=300)
plt.show()