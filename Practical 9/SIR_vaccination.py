import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Practical 9 - SIR_vaccination.py
# Pseudocode:
# 1. Define the population size and model parameters
# 2. Create a function that runs the SIR simulation for a given vaccination rate
# 3. Vaccinate a fraction of the population before the outbreak starts
# 4. Simulate infection and recovery over time
# 5. Store the number of infected people at each time point
# 6. Repeat for vaccination rates from 0% to 100%
# 7. Plot all infected curves on one figure
# 8. Save the plot to a file

# --------------------------
# Basic parameters
# --------------------------
N = 10000
beta = 0.3
gamma = 0.05
time_points = 1000


def run_simulation(vaccination_rate):
    """
    vaccination_rate: fraction between 0 and 1
    returns the infected history
    """
    vaccinated = int(N * vaccination_rate)

    # Keep total population equal to N
    if vaccinated >= N:
        return [0] * (time_points + 1)

    # Start with one infected person if possible
    I = 1
    S = N - vaccinated - I
    R = vaccinated

    infected_history = [I]

    for _ in range(time_points):
        infection_prob = beta * (I / N)
        infection_prob = min(max(infection_prob, 0), 1)

        new_infections = np.random.binomial(S, infection_prob)
        new_recoveries = np.random.binomial(I, gamma)

        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries

        infected_history.append(I)

    return infected_history


# --------------------------
# Plot infected curves for different vaccination rates
# --------------------------
vaccination_rates = list(range(0, 101, 10))

script_dir = os.path.dirname(os.path.abspath(__file__))
output_plot = os.path.join(script_dir, "SIR_vaccination_plot.png")

plt.figure(figsize=(6, 4), dpi=150)

for idx, rate in enumerate(vaccination_rates):
    infected_curve = run_simulation(rate / 100)
    color_value = idx / (len(vaccination_rates) - 1)
    plt.plot(
        infected_curve,
        label=f"{rate}%",
        color=cm.viridis(color_value)
    )

plt.xlabel("Time")
plt.ylabel("Number of infected people")
plt.title("SIR Model with Different Vaccination Rates")
plt.legend(title="Vaccinated")
plt.tight_layout()

plt.savefig(output_plot, dpi=300)
plt.show()