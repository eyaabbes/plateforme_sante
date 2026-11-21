"""Module M5 — Planning des blocs opératoires.

Type    : Ordonnancement (Affectation salle × créneau)
Outils  : gurobipy ou OR-Tools CP-SAT, Plotly (diagramme de Gantt)
Données : hopitaux.csv, personnel.csv, operations.csv
Branche : m5-blocs
"""


def solve(data: dict, params: dict) -> dict:
    """Résout le problème d'ordonnancement des blocs opératoires.

    Paramètres attendus dans `params` :
        - nb_salles (int) : nombre de salles d'opération.
        - horaires_ouverture (tuple) : (heure_debut, heure_fin).
        - duree_creneau (int) : durée d'un créneau en minutes (ex. 30).

    Retour attendu :
        {
            "statut": str,       # "optimal", "faisable", "infaisable"
            "objectif": float,   # fin de journée ou retards pondérés par priorité
            "solution": dict,    # planning par salle/créneau, taux d'occupation, heures sup
            "temps": float,      # temps de calcul en secondes
        }
    """
    raise NotImplementedError("Module M5 à implémenter.")
