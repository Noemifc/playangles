#genera angoli angoli distribuiti uniformemente ma senza ripetizioni su più rotazioni ma con path di golden angle 
#poi visualizzo la sequenza sia linearmente sia su un cerchio per vedere la diistribuzione 
# ANGOLI INTERLACCIATI GOLDEN ANGLE  inizializzo scan theta_g generato dall'arrai a path di golden angle 
# sequenza di angoli interlacciati basata sul golden angle, con dieci diversi angoli di partenza (


import numpy as np
import matplotlib.pyplot as plt


# per rotazioneintesra usa 360 ed angolo 137.50776° mod 360°
# se lavori in tomo parallela θ + 180° sono uguali, mod 180°, golden angle = 111.246



#golden angles array 
golden_a = 180*(3 - np.sqrt(5)) / 2  # deg ≈ 111.246°
golden_a_rad = golden_a*np.pi / 180  # rad 
num_proj = 360    #select number of projections , int
theta_start = [ 13.76941013 , 30. ,    40.0310562 ,  56.26164608 , 82.52329215 ,
  98.75388203 , 108.78493823 , 125.0155281 ,  151.27717418 , 167.50776405] #offset iniziali : angoli di partenza interlacciamento theta_start[i] è l’inizio di una serie interlacciata che crescono con passo costante golden_a

 # mod fa rimanere nel range 180 
golden_angles_tomo = np.mod(
    theta_start[:, None] + np.arange(num_proj) * golden_a,
    180
).flatten()
print("Shape:", golden_angles_tomo.shape)
print("10 golden angles:", golden_angles_tomo[:10])

 #golden angles sorted, utile da passare al pso 

golden_angles_tomo_sorted = np.sort(golden_angles_tomo)
print("10 angles sorted:", golden_angles_tomo_sorted[:10])


plt.figure(figsize=(6,6))
for start in theta_start:
    angles = np.mod(start + np.arange(num_proj) * golden_a, 180)
    plt.polar(np.deg2rad(angles), np.ones_like(angles), '.', alpha=0.6)
plt.title("Interlaced golden-angle sampling (mod 180°)")
plt.show()





























