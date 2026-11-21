"""Routes Flask — Module M4 : Tournées d'infirmiers à domicile."""

from flask import Blueprint, render_template

bp = Blueprint("m4", __name__, url_prefix="/m4")


@bp.route("/", methods=["GET", "POST"])
def page_m4():
    """Affiche la page du module M4 et traite la résolution via `modules.m4_infirmiers.solve`."""
    # TODO (Responsable M4) : récupérer les paramètres CVRPTW, appeler solve(data, params), retourner tournées + horaires.
    return render_template("m4_infirmiers.html")
