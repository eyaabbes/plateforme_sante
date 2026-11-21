"""Enregistrement des Blueprints Flask pour les 8 modules (M1 à M8)."""

from flask import Flask

from routes.m1_routes import bp as m1_bp
from routes.m2_routes import bp as m2_bp
from routes.m3_routes import bp as m3_bp
from routes.m4_routes import bp as m4_bp
from routes.m5_routes import bp as m5_bp
from routes.m6_routes import bp as m6_bp
from routes.m7_routes import bp as m7_bp
from routes.m8_routes import bp as m8_bp


def register_blueprints(app: Flask) -> None:
    """Enregistre les 8 blueprints de modules sur l'instance Flask."""
    for bp in (m1_bp, m2_bp, m3_bp, m4_bp, m5_bp, m6_bp, m7_bp, m8_bp):
        app.register_blueprint(bp)
