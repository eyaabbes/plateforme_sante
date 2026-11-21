"""Chargement centralisé des données communes et calcul des matrices de distances.

Chaque module et chaque route Flask peut importer `load_data()` afin de partager
exactement la même structure de dictionnaire `data`.
"""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent


def load_data(data_dir: Path = DATA_DIR) -> dict:
    """Charge les CSV communs et retourne le dictionnaire `data` attendu par `solve(data, params)`."""
    raise NotImplementedError("TODO : implémenter le chargement des CSV et le calcul des distances.")
