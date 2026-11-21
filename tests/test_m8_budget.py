"""Tests unitaires pour le module M8 (budget et achats de médicaments)."""

import pytest
from modules.m8_budget import solve

EXPECTED_KEYS = {"statut", "objectif", "solution", "temps"}


@pytest.mark.skip(reason="Module M8 non encore implémenté")
def test_m8_solve_contract():
    """Vérifie que `solve` respecte le contrat de retour commun."""
    result = solve(data={}, params={"budget_max": 50000.0})
    assert EXPECTED_KEYS.issubset(result.keys())
