"""Routes Flask — Module M5 : Planning des blocs opératoires."""

from flask import Blueprint, render_template

bp = Blueprint("m5", __name__, url_prefix="/m5")


@bp.route("/", methods=["GET", "POST"])
def page_m5():
    """Affiche la page du module M5 et traite la résolution via `modules.m5_blocs.solve`."""
    # TODO (Responsable M5) : récupérer opérations/salles, appeler solve(data, params), retourner Gantt Plotly.
    return render_template("m5_blocs.html")
