#genera angoli angoli distribuiti uniformemente ma senza ripetizioni su più rotazioni ma con path di golden angle 
#poi visualizzo la sequenza sia linearmente sia su un cerchio per vedere la diistribuzione 
# ANGOLI INTERLACCIATI GOLDEN ANGLE  inizializzo scan theta_g generato dall'arrai a path di golden angle 
# sequenza di angoli interlacciati basata sul golden angle, con dieci diversi angoli di partenza (


import numpy as np
import matplotlib.pyplot as plt


# per rotazioneintesra usa 360 ed angolo 137.50776° mod 360°
# se lavori in tomo parallela θ + 180° sono uguali, mod 180°, golden angle = 111.246



#golden angles array 
golden_a = 180*(3 - np.sqrt(5)) / 2  # deg
golden_a_rad = golden_a*np.pi / 180  # rad 
num_proj = 360    #select number of projections , int
theta_start = [ 13.76941013 , 30. ,    40.0310562 ,  56.26164608 , 82.52329215 ,
  98.75388203 , 108.78493823 , 125.0155281 ,  151.27717418 , 167.50776405] #offset iniziali : angoli di partenza interlacciamento theta_start[i] è l’inizio di una serie interlacciata che crescono con passo costante golden_a


golden_angles_tomo = np.mod(theta_start + np.arange(num_proj) * golden_a, 180) # mod fa rimanere nel range 180 
print(" 10 golden angles (float):", golden_angles_tomo[:10])


# golden-angle sorted 
golden_angles_tomo_sorted = np.sort(golden_angles_tomo) #golden angles sorted, utile da passare al pso 
print("10 angles sorted", golden_angles_tomo_sorted[:10])


plt.figure(figsize=(6,6))
for start in theta_start:
    angles = np.mod(start + np.arange(num_proj) * golden_a, 180)
    plt.polar(np.deg2rad(angles), np.ones_like(angles), '.', alpha=0.6)
plt.title("Interlaced golden-angle sampling (mod 180°)")
plt.show()




































def genang(numproj, nProj_per_rot):
    """Interlaced angles generator
    Parameters
    ----------
    numproj : int
            Total number of projections.
    nProj_per_rot : int
            Number of projections per rotation.
    """
    prime = 3
    pst = 0
    pend = 360
    seq = []
    i = 0
    while len(seq) < numproj:
        b = i
        i += 1
        r = 0
        q = 1 / prime
        while (b != 0):
            a = np.mod(b, prime)
            r += (a * q)
            q /= prime
            b = np.floor(b / prime)
        r *= ((pend-pst) / nProj_per_rot)
        k = 0
        while (np.logical_and(len(seq) < numproj, k < nProj_per_rot)):
            seq.append((pst + (r + k * (pend-pst) / nProj_per_rot))/180*np.pi)
            k += 1
    return seq

def line_plot(theta):

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(theta, marker='o', linestyle='-', color='b')  # you can customize markers, colors, etc.
    plt.title('Theta values')
    plt.xlabel('Index')
    plt.ylabel('Theta (rad)')
    plt.grid(True)
    plt.show()

def circle_plot(theta):

    # Convert to x, y coordinates
    x = np.cos(theta)
    y = np.sin(theta)

    # Identify rotation number for each point
    rotations = np.floor(theta / (2 * np.pi)).astype(int)
    num_rotations = rotations.max() + 1

    # Create the plot
    plt.figure(figsize=(6, 6))
    cmap = plt.cm.viridis

    # Plot each rotation with a different color (dots only)
    for r in range(num_rotations):
        mask = rotations == r
        if np.any(mask):
            plt.scatter(x[mask], y[mask], color=cmap(r / max(1, num_rotations - 1)), s=15, label=f'Rotation {r+1}')

    # Make it look like a circle
    plt.gca().set_aspect('equal', 'box')
    plt.title('Theta plotted on a circle (colored per rotation)')
    plt.xlabel('cos(θ)')
    plt.ylabel('sin(θ)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    ntheta = 45  # Total number of projections
    nthetap = 15  # Number of angles per rotation
    theta = np.array(genang(ntheta, nthetap), dtype='float32')
    line_plot(theta)
    circle_plot(theta)
