"""Tests unitaires pour le module M3 (tournées d'ambulances)."""

import pytest
from modules.m3_tournees_amb import solve

EXPECTED_KEYS = {"statut", "objectif", "solution", "temps"}


@pytest.mark.skip(reason="Module M3 non encore implémenté")
def test_m3_solve_contract():
    """Vérifie que `solve` respecte le contrat de retour commun."""
    result = solve(data={}, params={"nb_ambulances": 3, "duree_max": 120})
    assert EXPECTED_KEYS.issubset(result.keys())
