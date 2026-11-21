"""Routes Flask — Module M2 : Emplacement des ambulances."""

from flask import Blueprint, render_template

bp = Blueprint("m2", __name__, url_prefix="/m2")


@bp.route("/", methods=["GET", "POST"])
def page_m2():
    """Affiche la page du module M2 et traite la résolution via `modules.m2_ambulances.solve`."""
    # TODO (Responsable M2) : récupérer K, R, données modifiées, appeler solve(data, params), retourner résultats + carte Folium.
    return render_template("m2_ambulances.html")
