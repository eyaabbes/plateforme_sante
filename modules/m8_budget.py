"""Module M8 — Budget et achats de médicaments.

Type    : Optimisation (Programmation linéaire continue)
Outils  : gurobipy (variables duales et analyse de sensibilité)
Données : medicaments.csv, fournisseurs.csv (demande liée au M7)
Branche : m8-budget
"""


def solve(data: dict, params: dict) -> dict:
    """Détermine les quantités de médicaments à acheter par fournisseur au coût minimal.

    Paramètres attendus dans `params` :
        - budget_max (float) : budget total B disponible.

    Retour attendu :
        {
            "statut": str,       # "optimal", "faisable", "infaisable"
            "objectif": float,   # coût total d'achat
            "solution": dict,    # quantités par (médicament, fournisseur), budget consommé, prix duals
            "temps": float,      # temps de calcul en secondes
        }
    """
    raise NotImplementedError("Module M8 à implémenter.")
