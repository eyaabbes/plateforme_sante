# Données communes (`data/`)

Un seul jeu de données commun est généré par `generate_data.py` avec une graine fixe (`random.seed(42)`).
**Règle d'équipe** : ne pas modifier les schémas ou les fichiers CSV communs sans prévenir toute l'équipe.

## Fichiers attendus

| Fichier | Colonnes attendues | Modules utilisateurs |
|---|---|---|
| `communes.csv` | `id`, `nom`, `x`, `y`, `population` | M1, M2, M3, M4 |
| `sites_candidats.csv` | `id`, `x`, `y`, `cout_fixe`, `type` (`clinique`, `base_ambulance`) | M1, M2 |
| `hopitaux.csv` | `id`, `nom`, `x`, `y`, `nb_lits`, `nb_salles_operation` | M3, M5, M7 |
| `patients.csv` | `id`, `commune`, `service_requis`, `urgence`, `duree_soin`, `fenetre_debut`, `fenetre_fin`, `sexe`, `isolement` | M3, M4, M7 |
| `personnel.csv` | `id`, `role`, `contrat`, `indisponibilites` | M5, M6 |
| `operations.csv` | `id`, `duree`, `chirurgien`, `priorite` | M5 |
| `medicaments.csv` | `id`, `nom`, `demande` | M8 |
| `fournisseurs.csv` | `id`, `nom`, `medicament_id`, `prix`, `capacite` | M8 |

> **Distances** : non stockées aléatoirement — calculées à partir des coordonnées `(x, y)` dans `loader.py` (`temps_trajet = distance / vitesse_moyenne`).

## Règles de cohérence (Section 3.1 de la fiche projet)
- Distances calculées à partir des coordonnées ; temps de trajet dérivé d'une vitesse moyenne réaliste.
- Populations réalistes (communes de quelques milliers d'habitants, villes de dizaines de milliers).
- Durées réalistes (opération : 30 min à 4 h ; soin à domicile : 15 à 45 min ; journée : 7 à 8 h).
- Capacité totale suffisante pour garantir l'existence d'une solution réalisable sur le jeu par défaut.
