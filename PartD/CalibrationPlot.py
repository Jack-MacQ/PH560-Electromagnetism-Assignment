"""
PH560 Coursework - Calibration Demonstration

Plots S21 and S12 magnitude and phase to verify calibration quality.

Copyright (c) 2026 Jack MacQuarrie
MIT Licence
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------

data = np.genfromtxt(
    "Calibration_Demonstration.csv",
    delimiter=",",
    skip_header=15
)

# Extract data
freq = data[:, 7]        # FREQ3 (GHz)

s21_mag = data[:, 8]     # LOGMAG3
s21_phase = data[:, 9]   # PHASE3

s12_mag = data[:, 5]     # LOGMAG2
s12_phase = data[:, 6]   # PHASE2

# Keep only data below 17.5 GHz
mask = freq <= 17.0
freq = freq[mask]
s21_mag = s21_mag[mask]
s21_phase = s21_phase[mask]
s12_mag = s12_mag[mask]
s12_phase = s12_phase[mask]

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------

plt.figure(figsize=(8, 6))

# Magnitude
plt.subplot(2, 1, 1)
plt.plot(freq, s21_mag, label="S21")
plt.plot(freq, s12_mag, linestyle="--", label="S12")
plt.ylabel("Magnitude (dB)")
plt.grid(True, linestyle=":")
plt.legend()

plt.ylim(-4, 2)


# Phase
plt.subplot(2, 1, 2)
plt.plot(freq, s21_phase, label="S21")
plt.plot(freq, s12_phase, linestyle="--", label="S12")
plt.xlabel("Frequency (GHz)")
plt.ylabel("Phase (degrees)")
plt.grid(True, linestyle=":")
plt.legend()

plt.ylim(-150, 10)

plt.tight_layout()
os.makedirs("Plot", exist_ok=True)
plt.savefig("Plot/calibration_check_to_17GHz.png", dpi=300)
plt.show()