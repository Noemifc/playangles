#Prova del campinamento con varie path agolari 

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Definizione degli angoli
# ------------------------------
# Golden Angle
golden_a = 180*(3 - np.sqrt(5)) / 2  # deg

# Campionamenti
angoli_1grado = np.arange(0, 2000, 1)       # passo 1°
angoli_10gradi = np.arange(0, 2000, 10)     # passo 10°
angoli_golden = np.arange(0, 2000, golden_a)  # passo golden

# Conversione in radianti per il polare
angoli_1_rad = np.deg2rad(angoli_1grado)
angoli_10_rad = np.deg2rad(angoli_10gradi)
angoli_golden_rad = np.deg2rad(angoli_golden)

# Vettori r per il polare
r_1 = np.ones_like(angoli_1_rad)
r_10 = np.ones_like(angoli_10_rad)
r_golden = np.ones_like(angoli_golden_rad)

# ------------------------------
# Stampa dei valori
# ------------------------------
print("Golden angles in gradi:", angoli_golden)
print("Golden angles in radianti:", angoli_golden_rad)
print("Vettore r_golden:", r_golden)

# ------------------------------
# Plot polare
# ------------------------------


r_1 = np.ones_like(angoli_1_rad) * 0.4      # cerchio interno
r_10 = np.ones_like(angoli_10_rad) * 0.7    # cerchio medio
r_golden = np.ones_like(angoli_golden_rad) * 1  # cerchio esterno


plt.figure(figsize=(7, 7))
plt.subplot(projection='polar')
plt.scatter(angoli_1_rad, r_1, c='blue', s=10, label='1°')
plt.scatter(angoli_10_rad, r_10, c='red', s=30, label='10°')
plt.scatter(angoli_golden_rad, r_golden, c='green', s=20, label='Golden Angle')

plt.title("Confronto campionamenti angolari (polare)")
plt.yticks([])  # togliamo i raggi concentrici
plt.legend(loc='upper right')
plt.show()

# ------------------------------
# Plot lineare con linee e punti
# ------------------------------
# Y costante per distinguere i campionamenti
y_1 = np.ones_like(angoli_1grado)
y_10 = np.ones_like(angoli_10gradi) * 0.5
y_golden = np.ones_like(angoli_golden) * 0.25

plt.figure(figsize=(10, 3))

# Passo 1°
plt.plot(angoli_1grado, y_1, c='blue', linewidth=1, alpha=0.5)
plt.scatter(angoli_1grado, y_1, c='blue', s=10, label='1°')

# Passo 10°
plt.plot(angoli_10gradi, y_10, c='red', linewidth=1, alpha=0.5)
plt.scatter(angoli_10gradi, y_10, c='red', s=30, label='10°')

# Golden Angle
plt.plot(angoli_golden, y_golden, c='green', linewidth=1, alpha=0.5)
plt.scatter(angoli_golden, y_golden, c='green', s=20, label='Golden Angle')

plt.yticks([0.25, 0.5, 1], ['Golden', '10°', '1°'])
plt.xlabel("Angolo (°)")
plt.title("Confronto campionamenti angolari con linee")
plt.legend(loc='upper right')
plt.grid(True, axis='x', linestyle='--', alpha=0.5)
plt.show()
