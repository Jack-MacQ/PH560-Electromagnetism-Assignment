"""
PH560 Coursework - Part (c)
Theoretical phase shift vs frequency for rectangular waveguide.

Uses measured dimensions to compute the expected phase shift
for the TE10 mode.

Copyright (c) 2026 Jack MacQuarrie
MIT Licence
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

c = 3.0e8  # speed of light (m/s)

# ---------------------------------------------------------------------------
# Measured parameters
# ---------------------------------------------------------------------------

a = 15.66e-3   # waveguide width (m)
L = 62.20e-3   # waveguide length (m)

# Cutoff frequency (TE10)
fc = c / (2 * a)

# ---------------------------------------------------------------------------
# Frequency range (avoid very close to cutoff)
# ---------------------------------------------------------------------------

f = np.linspace(10e9, 18e9, 500)  # 10–18 GHz

# ---------------------------------------------------------------------------
# Phase shift calculation
# ---------------------------------------------------------------------------

phi_rad = (2 * np.pi * f * L / c) * np.sqrt(1 - (fc / f)**2)
phi_deg = np.degrees(phi_rad)

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(f / 1e9, phi_deg, label="Theoretical phase shift (TE$_{10}$)")

# Labels
plt.xlabel("Frequency (GHz)")
plt.ylabel("Phase shift (degrees)")

# Grid (clean, like your other plots)
plt.grid(True, linestyle="--", linewidth=0.7)

# Legend
plt.legend()

# Title (optional depending on style)
plt.title("Expected Phase Shift vs Frequency for Smooth Waveguide")

# Save
plt.savefig("phase_shift_theoretical.png", dpi=300)

plt.show()