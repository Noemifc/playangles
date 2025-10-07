import numpy as np
import matplotlib.pyplot as plt

#golden angles array 
golden_a = 180*(3 - np.sqrt(5)) / 2  # deg ≈ 111.246° tomo
golden_a_rad = golden_a*np.pi / 180  # rad 
num_proj = 360    #select number of projections , int

#offset iniziali : angoli di partenza interlacciamento theta_start[i] è l’inizio di una serie interlacciata che crescono con passo costante golden_a

# [ 13.76941013, 30., 40.0310562, 56.26164608, 82.52329215, 98.75388203, 108.78493823, 125.0155281, 151.27717418, 167.50776405]

theta_start = np.array([
    13.76941013, 30., 40.0310562
])

# mod 180 tomo
golden_angles_tomo = np.mod(
    theta_start[:, None] + np.arange(num_proj) * golden_a,
    180
).flatten()
print("Shape:", golden_angles_tomo.shape)
print("10 golden angles:", golden_angles_tomo[:100])

 #golden angles sorted (PSO)

golden_angles_tomo_sorted = np.sort(golden_angles_tomo)
print("10 angles sorted:", golden_angles_tomo_sorted[:100])


plt.figure(figsize=(6,6))
for start in theta_start:
    angles = np.mod(start + np.arange(num_proj) * golden_a, 180)
    plt.polar(np.deg2rad(angles), np.ones_like(angles), '.', alpha=0.6)
plt.title("Interlaced golden-angle sampling (mod 180°)")
plt.show()





