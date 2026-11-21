# Plateforme d'aide à la décision — Système de Santé Régional (Projet RO)

Application web **Flask** (HTML / CSS / JS) développée en Python dans le cadre du cours de **Recherche Opérationnelle (RO)**.  
Équipe de **8 personnes** · **8 modules** · **Date finale de validation : 11 décembre 2026**.

---

## Architecture du projet

```text
plateforme_sante/
├── app.py                          # Serveur Flask + page d'accueil `/` (`index.html`)
├── run.py                          # Script de lancement (`python run.py`)
├── requirements.txt                # Dépendances Python communes
├── .gitignore                      # Fichiers ignorés par Git
├── README.md                       # Documentation et règles de travail d'équipe
├── data/
│   ├── generate_data.py            # Génération du jeu de données commun (`random.seed(42)`)
│   ├── loader.py                   # Chargement des CSV communs + calcul des distances
│   └── README.md                   # Schéma détaillé des fichiers CSV communs
├── modules/                        # Modèles mathématiques & solveurs (`solve(data, params)`)
│   ├── __init__.py
│   ├── m1_cliniques.py             # M1 : p-médian (gurobipy)
│   ├── m2_ambulances.py            # M2 : Couverture maximale (gurobipy)
│   ├── m3_tournees_amb.py          # M3 : VRP urgences (gurobipy + OR-Tools)
│   ├── m4_infirmiers.py            # M4 : CVRPTW (OR-Tools + gurobipy)
│   ├── m5_blocs.py                 # M5 : Planning blocs opératoires (gurobipy / CP-SAT)
│   ├── m6_personnel.py             # M6 : Nurse rostering (gurobipy / CP-SAT)
│   ├── m7_lits.py                  # M7 : Affectation lits (gurobipy + SciPy)
│   └── m8_budget.py                # M8 : Achats médicaments PL (gurobipy)
├── routes/                         # Blueprints Flask (1 fichier par module -> 0 conflit Git)
│   ├── __init__.py                 # Enregistrement automatique des 8 blueprints
│   ├── m1_routes.py                # /m1
│   ├── m2_routes.py                # /m2
│   ├── m3_routes.py                # /m3
│   ├── m4_routes.py                # /m4
│   ├── m5_routes.py                # /m5
│   ├── m6_routes.py                # /m6
│   ├── m7_routes.py                # /m7
│   └── m8_routes.py                # /m8
├── templates/                      # Interfaces HTML (Jinja2)
│   ├── base.html                   # Gabarit commun (barre de navigation vers index + M1..M8)
│   ├── index.html                  # Page d'accueil regroupant tous les modules
│   ├── m1_cliniques.html
│   ├── m2_ambulances.html
│   ├── m3_tournees_amb.html
│   ├── m4_infirmiers.html
│   ├── m5_blocs.html
│   ├── m6_personnel.html
│   ├── m7_lits.html
│   └── m8_budget.html
├── static/                         # Ressources statiques web
│   ├── css/
│   │   └── style.css               # Feuille de style commune
│   └── js/
│       └── main.js                 # Scripts JS communs
├── tests/                          # Tests unitaires (1 fichier par module)
└── docs/                           # Rapport final, schémas, captures d'écran
```

---

## Répartition des 8 modules

| # | Module | Type | Route | Fichiers dédiés au membre | Branche Git | Responsable |
|---|---|---|---|---|---|---|
| M1 | Cliniques et centres de vaccination | Localisation (p-médian) | `/m1` | `modules/m1_cliniques.py`, `routes/m1_routes.py`, `templates/m1_cliniques.html`, `tests/test_m1_cliniques.py` | `m1-cliniques` | À assigner |
| M2 | Emplacement des ambulances | Localisation (Couv. max) | `/m2` | `modules/m2_ambulances.py`, `routes/m2_routes.py`, `templates/m2_ambulances.html`, `tests/test_m2_ambulances.py` | `m2-ambulances` | À assigner |
| M3 | Tournées d'ambulances | Routage (VRP urgences) | `/m3` | `modules/m3_tournees_amb.py`, `routes/m3_routes.py`, `templates/m3_tournees_amb.html`, `tests/test_m3_tournees_amb.py` | `m3-tournees-amb` | À assigner |
| M4 | Tournées d'infirmiers à domicile | Routage (CVRPTW) | `/m4` | `modules/m4_infirmiers.py`, `routes/m4_routes.py`, `templates/m4_infirmiers.html`, `tests/test_m4_infirmiers.py` | `m4-infirmiers` | À assigner |
| M5 | Planning des blocs opératoires | Ordonnancement | `/m5` | `modules/m5_blocs.py`, `routes/m5_routes.py`, `templates/m5_blocs.html`, `tests/test_m5_blocs.py` | `m5-blocs` | À assigner |
| M6 | Planning du personnel | Ordonnancement (Rostering) | `/m6` | `modules/m6_personnel.py`, `routes/m6_routes.py`, `templates/m6_personnel.html`, `tests/test_m6_personnel.py` | `m6-personnel` | À assigner |
| M7 | Affectation des patients aux lits | Optimisation (Affectation) | `/m7` | `modules/m7_lits.py`, `routes/m7_routes.py`, `templates/m7_lits.html`, `tests/test_m7_lits.py` | `m7-lits` | À assigner |
| M8 | Budget et achats de médicaments | Optimisation (PL) | `/m8` | `modules/m8_budget.py`, `routes/m8_routes.py`, `templates/m8_budget.html`, `tests/test_m8_budget.py` | `m8-budget` | À assigner |

---

## Installation et lancement

### 1. Prérequis
- **Python 3.10+**
- **Licence académique Gurobi** (gratuite avec l'adresse e-mail universitaire — à demander dès le début du projet)

### 2. Installer l'environnement

```bash
# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement virtuel
# Linux / macOS :
source .venv/bin/activate
# Windows (PowerShell) :
.venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Lancer le serveur web

```bash
python run.py
```

Puis ouvrir dans un navigateur : `http://127.0.0.1:5000` (la page `index.html` regroupe l'ensemble des 8 modules).

### 4. Lancer les tests

```bash
pytest
```

---

## Contrat d'interface commun (`solve`)

Chaque fichier dans `modules/` **doit** exposer exactement la fonction suivante :

```python
def solve(data: dict, params: dict) -> dict:
    return {
        "statut": "optimal",   # "optimal", "faisable", "infaisable"
        "objectif": 1234.5,    # valeur de la fonction objectif (float)
        "solution": {...},     # résultats structurés à afficher
        "temps": 0.42,         # temps de calcul en secondes (float)
    }
```

> **Graphiques dans Flask** :
> - Cartes **Folium** : `carte._repr_html_()` passé au template Jinja2 (`{{ carte_html | safe }}`).
> - Graphiques **Plotly** (Gantt, barres, courbes) : `fig.to_html(full_html=False)` passé au template (`{{ graph_html | safe }}`).

---

## Règles de travail Git

1. **Une branche par module** (ex. `git checkout -b m1-cliniques`). Ne jamais pousser directement sur `main`.
2. **La branche `main` doit toujours fonctionner.**
3. **Pull Request obligatoire** : fusion dans `main` uniquement après relecture par au moins un autre membre.
4. **Ne pas modifier `app.py`, `templates/base.html`, `templates/index.html` ni `data/`** sans prévenir toute l'équipe.
5. **Tout nouveau paquet Python** doit être ajouté dans `requirements.txt`.
6. **Code et commentaires en français** pour l'ensemble du dépôt.
