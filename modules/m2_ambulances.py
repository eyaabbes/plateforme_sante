"""Module M2 — Emplacement des ambulances.

Type    : Localisation (Couverture maximale, PLNE)
Outils  : gurobipy, Folium
Données : communes.csv, sites_candidats.csv, temps de trajet
Branche : m2-ambulances
"""


def solve(data: dict, params: dict) -> dict:
    """Résout le problème de couverture maximale pour les bases d'ambulances.

    Paramètres attendus dans `params` :
        - nb_ambulances (int) : nombre K de bases à activer.
        - rayon_minutes (float) : rayon de couverture R en minutes.

    Retour attendu :
        {
            "statut": str,       # "optimal", "faisable", "infaisable"
            "objectif": float,   # population couverte
            "solution": dict,    # bases choisies, taux de couverture, zones non couvertes
            "temps": float,      # temps de calcul en secondes
        }
    """
    raise NotImplementedError("Module M2 à implémenter.")
