"""Routes Flask — Module M3 : Tournées d'ambulances."""

from flask import Blueprint, render_template

bp = Blueprint("m3", __name__, url_prefix="/m3")


@bp.route("/", methods=["GET", "POST"])
def page_m3():
    """Affiche la page du module M3 et traite la résolution via `modules.m3_tournees_amb.solve`."""
    # TODO (Responsable M3) : récupérer les paramètres VRP, appeler solve(data, params), retourner routes + carte.
    return render_template("m3_tournees_amb.html")
