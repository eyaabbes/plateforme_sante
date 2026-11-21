"""Tests unitaires pour le module M1 (cliniques et centres de vaccination)."""

import pytest
from modules.m1_cliniques import solve

EXPECTED_KEYS = {"statut", "objectif", "solution", "temps"}


@pytest.mark.skip(reason="Module M1 non encore implémenté")
def test_m1_solve_contract():
    """Vérifie que `solve` respecte le contrat de retour commun."""
    result = solve(data={}, params={"nb_centres": 3})
    assert EXPECTED_KEYS.issubset(result.keys())
