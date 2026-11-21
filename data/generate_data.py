"""Script de génération du jeu de données commun (Section 3.1).

À implémenter collectivement en début de projet avec une graine fixe :
    SEED = 42

Fichiers CSV à générer dans `data/` :
- communes.csv
- sites_candidats.csv
- hopitaux.csv
- patients.csv
- personnel.csv
- operations.csv
- medicaments.csv
- fournisseurs.csv
"""

from pathlib import Path

SEED = 42
DATA_DIR = Path(__file__).resolve().parent


def generate_all(seed: int = SEED) -> None:
    """Génère l'ensemble des fichiers CSV communs de manière déterministe."""
    raise NotImplementedError("TODO : implémenter la génération cohérente des CSV communs.")


if __name__ == "__main__":
    generate_all()
