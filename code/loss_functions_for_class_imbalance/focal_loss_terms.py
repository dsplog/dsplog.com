import numpy as np
import matplotlib.pyplot as plt

# Parameters
gamma = 2
p = np.linspace(0.01, 0.99, 500)  # Avoiding 0 and 1 to prevent log(0)

# Terms
pt = 1 - p
ce_term = pt - 1
focal_term = gamma * pt * np.log(pt)

# Combined expression
expression = (1 - pt)**gamma * (ce_term + focal_term)

# Plot
plt.figure(figsize=(8, 6))

# Plot each term
plt.plot(p, (1 - pt)**gamma, label=r'$(1-p_t)^\gamma$ (scaling term)', linestyle='--')
plt.plot(p, ce_term, label=r'$(p_t - 1)$ (CE term)', linestyle='-.')
plt.plot(p, focal_term, label=r'$\gamma p_t \log(p_t)$ (Focal term)', linestyle=':')
plt.plot(p, expression, label=r'Combined: $(1-p_t)^\gamma \left[(p_t-1) + \gamma p_t \log(p_t)\right]$', linewidth=2)

# Labels and title
plt.xlabel(r'$p$')
plt.ylabel('Value')
plt.title(f'Plot of Individual Terms and Combined Expression vs $p$ (gamma={gamma})')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.legend()
plt.grid()
plt.show()