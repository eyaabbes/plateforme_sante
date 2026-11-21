"""Tests unitaires pour le module M4 (tournées d'infirmiers à domicile)."""

import pytest
from modules.m4_infirmiers import solve

EXPECTED_KEYS = {"statut", "objectif", "solution", "temps"}


@pytest.mark.skip(reason="Module M4 non encore implémenté")
def test_m4_solve_contract():
    """Vérifie que `solve` respecte le contrat de retour commun."""
    result = solve(data={}, params={"nb_infirmiers": 4, "duree_travail_max": 480})
    assert EXPECTED_KEYS.issubset(result.keys())
