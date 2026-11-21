"""Serveur web Flask — Plateforme d'aide à la décision pour un système de santé régional.

Point d'entrée de l'application web :
- Route `/` : page d'accueil (`templates/index.html`) regroupant les 8 modules.
- Blueprints `/m1` à `/m8` : un fichier par module dans `routes/` pour éviter les conflits Git.
"""

from flask import Flask, render_template

from routes import register_blueprints

MODULES_INFO = [
    {"id": "M1", "titre": "Cliniques et centres de vaccination", "type": "Localisation · p-médian", "url": "/m1"},
    {"id": "M2", "titre": "Emplacement des ambulances", "type": "Localisation · Couverture max", "url": "/m2"},
    {"id": "M3", "titre": "Tournées d'ambulances", "type": "Routage · VRP urgences", "url": "/m3"},
    {"id": "M4", "titre": "Tournées d'infirmiers à domicile", "type": "Routage · CVRPTW", "url": "/m4"},
    {"id": "M5", "titre": "Planning des blocs opératoires", "type": "Ordonnancement · Salle × créneau", "url": "/m5"},
    {"id": "M6", "titre": "Planning du personnel", "type": "Ordonnancement · Nurse rostering", "url": "/m6"},
    {"id": "M7", "titre": "Affectation des patients aux lits", "type": "Optimisation · Affectation", "url": "/m7"},
    {"id": "M8", "titre": "Budget et achats de médicaments", "type": "Optimisation · Programmation linéaire", "url": "/m8"},
]


def create_app() -> Flask:
    """Crée et configure l'application Flask avec tous les modules."""
    app = Flask(__name__)

    @app.route("/")
    def index():
        """Page d'accueil regroupant l'accès à l'ensemble des 8 modules."""
        return render_template("index.html", modules=MODULES_INFO)

    register_blueprints(app)
    return app


app = create_app()
