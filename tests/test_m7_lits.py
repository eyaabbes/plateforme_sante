"""Tests unitaires pour le module M7 (affectation des patients aux lits)."""

import pytest
from modules.m7_lits import solve

EXPECTED_KEYS = {"statut", "objectif", "solution", "temps"}


@pytest.mark.skip(reason="Module M7 non encore implémenté")
def test_m7_solve_contract():
    """Vérifie que `solve` respecte le contrat de retour commun."""
    result = solve(data={}, params={})
    assert EXPECTED_KEYS.issubset(result.keys())
