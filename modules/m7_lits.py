"""Module M7 — Affectation des patients aux lits.

Type    : Optimisation (Problème d'affectation)
Outils  : gurobipy + comparaison scipy.optimize.linear_sum_assignment
Données : hopitaux.csv, patients.csv
Branche : m7-lits
"""


def solve(data: dict, params: dict) -> dict:
    """Affecte chaque patient à un lit compatible au coût minimal.

    Paramètres attendus dans `params` :
        - lits_indisponibles (list) : identifiants des lits hors service (optionnel).

    Retour attendu :
        {
            "statut": str,       # "optimal", "faisable", "infaisable"
            "objectif": float,   # coût total d'affectation
            "solution": dict,    # affectations patient -> lit, liste d'attente, taux d'occupation
            "temps": float,      # temps de calcul en secondes
        }
    """
    raise NotImplementedError("Module M7 à implémenter.")
