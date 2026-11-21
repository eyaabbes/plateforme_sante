"""Routes Flask — Module M1 : Emplacement de cliniques et centres de vaccination."""

from flask import Blueprint, render_template

bp = Blueprint("m1", __name__, url_prefix="/m1")


@bp.route("/", methods=["GET", "POST"])
def page_m1():
    """Affiche la page du module M1 et traite la résolution via `modules.m1_cliniques.solve`."""
    # TODO (Responsable M1) : récupérer les entrées/CSV, appeler solve(data, params), retourner résultats + carte Folium.
    return render_template("m1_cliniques.html")
