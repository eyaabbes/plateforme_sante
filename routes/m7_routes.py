"""Routes Flask — Module M7 : Affectation des patients aux lits."""

from flask import Blueprint, render_template

bp = Blueprint("m7", __name__, url_prefix="/m7")


@bp.route("/", methods=["GET", "POST"])
def page_m7():
    """Affiche la page du module M7 et traite la résolution via `modules.m7_lits.solve`."""
    # TODO (Responsable M7) : récupérer patients/lits, appeler solve(data, params), retourner affectations et taux d'occupation.
    return render_template("m7_lits.html")
