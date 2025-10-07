import numpy as np

N = 100  # numero totale di proiezioni
golden_angle = 137.50776405003785  # gradi

# Array base di angoli
angles = [(n * golden_angle) % 360 for n in range(N)]

# Interlacciamento (opzionale)
angles_even = angles[::2]
angles_odd = angles[1::2]
