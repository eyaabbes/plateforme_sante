"""Routes Flask — Module M8 : Budget et achats de médicaments."""

from flask import Blueprint, render_template

bp = Blueprint("m8", __name__, url_prefix="/m8")


@bp.route("/", methods=["GET", "POST"])
def page_m8():
    """Affiche la page du module M8 et traite la résolution via `modules.m8_budget.solve`."""
    # TODO (Responsable M8) : récupérer prix/capacités/demande/budget, appeler solve(data, params), retourner quantités + graphiques.
    return render_template("m8_budget.html")
