"""
Module des Observables Mathématiques pour l'IA Fluide
"""

import numpy as np

def observable_convergence(state):
    return np.tanh(state)

def observable_divergence(state):
    return state * np.random.uniform(0.9, 1.1)

def observable_cycle(state):
    return np.sin(state)

def observable_optimisation_renforce(state):
    return state / (1 + np.abs(state))

def ajustement_validite(state):
    poids = np.exp(-np.abs(state - 0.5) * 5)
    return np.where(poids < 0.7, state * 0.9, state * 1.1)