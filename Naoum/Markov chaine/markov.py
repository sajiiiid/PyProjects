import numpy as np
import matplotlib.pyplot as plt

# 1. Define the transition matrix P
P = np.array([
    [0.95, 0.04, 0.01, 0.00],
    [0.00, 0.90, 0.05, 0.05],
    [0.00, 0.00, 0.80, 0.20],
    [1.00, 0.00, 0.00, 0.00]
])

# 2. Initial distribution: pi(0)
pi = np.array([0.25, 0.25, 0.25, 0.25])

# 3. Simulate for 50 steps (days)
steps = 30
history = np.zeros((steps + 1, 4))
history[0] = pi

for i in range(1, steps + 1):
    pi = np.dot(pi, P)
    history[i] = pi

# 4. Simple Plotting
plt.figure(figsize=(10, 6))
labels = ['State 1 (New)', 'State 2', 'State 3', 'State 4 (Broken)']
colors = ['blue', 'green', 'orange', 'red']

for i in range(4):
    plt.plot(history[:, i], label=labels[i], color=colors[i], linewidth=2)

# Optional: Add steady state target values as horizontal lines
steady_states = [0.625, 0.25, 0.09375, 0.03125]
for i, val in enumerate(steady_states):
    plt.axhline(y=val, color=colors[i], linestyle='--', alpha=0.3)

plt.title("Evolution of Probability Distribution (Markov Chain)")
plt.xlabel("Days")
plt.ylabel("Probability")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()