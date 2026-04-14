import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

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

    # If 100% vaccinated, no outbreak can start
    if vaccinated >= N:
        return [0] * (time_points + 1)

    # Keep one infected person initially if possible
    I = 1
    S = N - vaccinated - I
    R = 0

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

plt.figure(figsize=(6, 4), dpi=150)

for idx, rate in enumerate(vaccination_rates):
    infected_curve = run_simulation(rate / 100)
    color_value = idx / (len(vaccination_rates) - 1)
    plt.plot(infected_curve, label=f"{rate}%", color=cm.viridis(color_value))

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.tight_layout()

plt.savefig("SIR_vaccination_plot.png")
plt.show()