"""Tests unitaires pour le module M5 (planning des blocs opératoires)."""

import pytest
from modules.m5_blocs import solve

EXPECTED_KEYS = {"statut", "objectif", "solution", "temps"}


@pytest.mark.skip(reason="Module M5 non encore implémenté")
def test_m5_solve_contract():
    """Vérifie que `solve` respecte le contrat de retour commun."""
    result = solve(data={}, params={"nb_salles": 4, "duree_creneau": 30})
    assert EXPECTED_KEYS.issubset(result.keys())
