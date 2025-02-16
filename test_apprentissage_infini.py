"""
Expérimentation : IA Fluide en Apprentissage Infini
"""

from src.ia_fluide import IAFluide
import numpy as np
import time

# Initialisation de l'IA fluide avec 5 dimensions
ia = IAFluide(n_dimensions=5)

# Boucle d’apprentissage infini
iteration = 0
while True:
    input_data = np.random.rand(5)  # Génération aléatoire d’entrée
    output = ia.evolve(input_data)  # Évolution de l’IA

    # Affichage des résultats
    print(f"Iteration {iteration}:")
    print("Données d'entrée :", input_data)
    print("État actuel de l'IA :", output)
    print("-" * 40)

    iteration += 1
    time.sleep(1)  # Pause pour voir l’évolution en temps réel