"""Module M4 — Tournées d'infirmiers à domicile.

Type    : Routage (CVRP avec fenêtres de temps — CVRPTW)
Outils  : OR-Tools routing (dimension temps) + gurobipy (comparaison petite instance)
Données : communes.csv, patients.csv, temps de trajet, cliniques (sortie M1)
Branche : m4-infirmiers
"""


def solve(data: dict, params: dict) -> dict:
    """Résout le problème de tournées d'infirmiers avec fenêtres de temps.

    Paramètres attendus dans `params` :
        - nb_infirmiers (int) : nombre d'infirmiers disponibles.
        - duree_travail_max (float) : charge maximale Q par infirmier.

    Retour attendu :
        {
            "statut": str,       # "optimal", "faisable", "infaisable"
            "objectif": float,   # temps total / coût de tournée
            "solution": dict,    # tournées, heures d'arrivée, retards éventuels, charge
            "temps": float,      # temps de calcul en secondes
        }
    """
    raise NotImplementedError("Module M4 à implémenter.")
