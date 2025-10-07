import numpy as np
import matplotlib.pyplot as plt

# golden angle (mod 180) : tomo p
golden_a = 180 * (3 - np.sqrt(5)) / 2  # ≈ 111.246°
num_proj =100 

# interlaced golden-angle sequence
# offsets  [ 13.76941013, 30., 40.0310562, 56.26164608, 82.52329215, 98.75388203, 108.78493823, 125.0155281, 151.27717418, 167.50776405]

theta_start = np.array([
    13.76941013, 30., 40.0310562, 
])

golden_angles_tomo = np.mod(
    theta_start[:, None] + np.arange(num_proj) * golden_a,
    180
).flatten()

print("Shape:", golden_angles_tomo.shape)
print("10 golden angles:", golden_angles_tomo[:10])

# send to PSO 
golden_angles_tomo_sorted = np.sort(golden_angles_tomo)
print("10 angles sorted:", golden_angles_tomo_sorted[:10])

# Plot 
plt.figure(figsize=(6, 6))
colors = plt.cm.tab10(np.linspace(0, 1, len(theta_start)))

for i, start in enumerate(theta_start):
    angles = np.mod(start + np.arange(num_proj) * golden_a, 180)
    plt.polar(np.deg2rad(angles), np.ones_like(angles), '.', alpha=0.6, color=colors[i])

plt.title("Interlaced golden-angle sampling (mod 180°)")
plt.show()
