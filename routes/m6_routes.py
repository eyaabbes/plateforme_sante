"""Routes Flask — Module M6 : Planning du personnel (Nurse Rostering)."""

from flask import Blueprint, render_template

bp = Blueprint("m6", __name__, url_prefix="/m6")


@bp.route("/", methods=["GET", "POST"])
def page_m6():
    """Affiche la page du module M6 et traite la résolution via `modules.m6_personnel.solve`."""
    # TODO (Responsable M6) : récupérer effectifs/indisponibilités, appeler solve(data, params), retourner planning.
    return render_template("m6_personnel.html")
