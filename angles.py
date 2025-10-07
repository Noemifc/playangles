# Esempio di angoli interlacciati , di Franceso 
#idea : modifica il programma tale da essere utilizzato con golden angle 


import time
import numpy as np
import matplotlib.pyplot as plt

# Genera angoli interlacciati

def genang(numproj, nProj_per_rot):
    """Interlaced angles generator
    Parameters
    ----------
    numproj : int #numero totale di angoli che vogliamo generare
            Total number of projections.
    nProj_per_rot : int #quanti angoli per rotazione completa di 360
            Number of projections per rotation.
    """
  # Inizializzazione delle variabili,
  
    prime = 3 # Sistema di Van der Corput in base n : angoli non ripetuti, distribuiti in modo uniforme 
    pst = 0
    pend = 360  # Intervallo tra pst e pend
    seq = [] # Lista vuota di accumulo angoli 
    i = 0 # Contatore pe generare la sequenza
# Converte i in una sequenza di frazioni in base prime per ottenere valori ben distribuiti tra 0 e 1 
# con r numero normalizzato tra 0 e 1 che verrà scalato all’intervallo dell’angolo
  
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

      # Scala l’angolo e genera la rotazione
        r *= ((pend-pst) / nProj_per_rot)
        k = 0
        while (np.logical_and(len(seq) < , k < nProj_per_rot)):
            seq.append((pst + (r + k * (pend-pst) / nProj_per_rot))/180*np.pi)
            k += 1
    return seq
    print(seq, )

# La funzione restituisce una lista di angoli in radianti utilizzabile per simulazioni o scansioni

def line_plot(theta): #Visualizza gli angoli in un grafico lineare, ogni punto corrisponde an un angolo, con posiz nell'arrau su asse x 

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(theta, marker='o', linestyle='-', color='b')  # you can customize markers, colors, etc.
    plt.title('Theta values')
    plt.xlabel('Index')
    plt.ylabel('Theta (rad)')
    plt.grid(True)
    plt.show()

def circle_plot(theta):

    # Convert to x, y coordinates e li plotta su cerchio di raggio uno 
    x = np.cos(theta)
    y = np.sin(theta)

    # Identify rotation number for each point Identifica quante rotazioni complete sono state fatte
    rotations = np.floor(theta / (2 * np.pi)).astype(int)
    num_rotations = rotations.max() + 1

    # Create the plot e Plotta ogni rotazione
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

  # Genera 45 angoli totali, con 15 per rotazione
  
    ntheta = 45  # Total number of projections
    nthetap = 15  # Number of angles per rotation
    theta = np.array(genang(ntheta, nthetap), dtype='float32')
    line_plot(theta)
    circle_plot(theta)
