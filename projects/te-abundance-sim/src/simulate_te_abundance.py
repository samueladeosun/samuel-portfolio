import numpy as np
import matplotlib.pyplot as plt


def simulate_te_abundance(n_steps=500, initial_abundance=50.0, growth_rate=0.02, noise=0.15):
    """Simple stochastic simulation for TE abundance over time."""
    abundance = np.empty(n_steps)
    abundance[0] = initial_abundance

    for i in range(1, n_steps):
        drift = abundance[i - 1] * (1.0 + growth_rate)
        stochastic_term = np.random.normal(0, noise * np.sqrt(max(abundance[i - 1], 1.0)))
        abundance[i] = max(drift + stochastic_term, 0.0)

    return abundance


def main():
    times = np.arange(500)
    trajectory = simulate_te_abundance()

    plt.figure(figsize=(10, 5))
    plt.plot(times, trajectory, color="steelblue", linewidth=2)
    plt.title("Simple TE Abundance Simulation")
    plt.xlabel("Time")
    plt.ylabel("TE abundance")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
