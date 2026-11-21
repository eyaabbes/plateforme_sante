"""Tests unitaires pour le module M6 (planning du personnel / nurse rostering)."""

import pytest
from modules.m6_personnel import solve

EXPECTED_KEYS = {"statut", "objectif", "solution", "temps"}


@pytest.mark.skip(reason="Module M6 non encore implémenté")
def test_m6_solve_contract():
    """Vérifie que `solve` respecte le contrat de retour commun."""
    result = solve(data={}, params={"nb_infirmiers": 12, "nb_jours": 7})
    assert EXPECTED_KEYS.issubset(result.keys())
