"""Module M3 — Tournées d'ambulances.

Type    : Routage (VRP avec urgences)
Outils  : gurobipy (petites instances) + OR-Tools routing (grandes instances)
Données : communes.csv, hopitaux.csv, patients.csv, temps de trajet, bases (sortie M2)
Branche : m3-tournees-amb
"""


def solve(data: dict, params: dict) -> dict:
    """Résout le problème de routage d'ambulances avec priorisation des urgences.

    Paramètres attendus dans `params` :
        - nb_ambulances (int) : nombre d'ambulances disponibles.
        - duree_max (float) : durée maximale T d'une tournée.
        - base_depart : identifiant de la base de départ.

    Retour attendu :
        {
            "statut": str,       # "optimal", "faisable", "infaisable"
            "objectif": float,   # temps total de tournée
            "solution": dict,    # routes par ambulance, temps par ambulance
            "temps": float,      # temps de calcul en secondes
        }
    """
    raise NotImplementedError("Module M3 à implémenter.")
