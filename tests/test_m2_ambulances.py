"""Tests unitaires pour le module M2 (emplacement des ambulances)."""

import pytest
from modules.m2_ambulances import solve

EXPECTED_KEYS = {"statut", "objectif", "solution", "temps"}


@pytest.mark.skip(reason="Module M2 non encore implémenté")
def test_m2_solve_contract():
    """Vérifie que `solve` respecte le contrat de retour commun."""
    result = solve(data={}, params={"nb_ambulances": 3, "rayon_minutes": 10})
    assert EXPECTED_KEYS.issubset(result.keys())
