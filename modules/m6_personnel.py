"""Module M6 — Planning du personnel (Nurse Rostering).

Type    : Ordonnancement (Planning avec règles de repos)
Outils  : gurobipy ou OR-Tools CP-SAT
Données : personnel.csv
Branche : m6-personnel
"""


def solve(data: dict, params: dict) -> dict:
    """Construit le planning des infirmiers sur 7 ou 28 jours (matin, soir, nuit).

    Paramètres attendus dans `params` :
        - nb_infirmiers (int) : effectif N.
        - nb_jours (int) : horizon du planning (7 ou 28).
        - besoins_min (dict) : besoins minimums par service (matin, soir, nuit).

    Retour attendu :
        {
            "statut": str,       # "optimal", "faisable", "infaisable"
            "objectif": float,   # coût total / préférences non respectées
            "solution": dict,    # planning par infirmier/jour/service, heures, équité
            "temps": float,      # temps de calcul en secondes
        }
    """
    raise NotImplementedError("Module M6 à implémenter.")
