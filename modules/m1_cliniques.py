"""Module M1 — Emplacement de cliniques et centres de vaccination.

Type    : Localisation (p-médian, PLNE)
Outils  : gurobipy, Folium
Données : communes.csv, sites_candidats.csv, distances
Branche : m1-cliniques
"""


def solve(data: dict, params: dict) -> dict:
    """Résout le problème p-médian d'emplacement de cliniques.

    Paramètres attendus dans `params` :
        - nb_centres (int) : nombre P de sites à ouvrir.

    Retour attendu :
        {
            "statut": str,       # "optimal", "faisable", "infaisable"
            "objectif": float,   # distance totale / moyenne pondérée
            "solution": dict,    # sites ouverts, affectations commune -> centre
            "temps": float,      # temps de calcul en secondes
        }
    """
    raise NotImplementedError("Module M1 à implémenter.")
