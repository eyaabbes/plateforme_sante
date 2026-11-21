# Règles obligatoires pour tous les agents IA

Ce fichier est la source canonique des règles de travail du projet. Tous les agents IA, outils automatisés et assistants de code doivent le lire au démarrage de chaque session et respecter ces instructions.

Ces règles sont également résumées dans `.github/copilot-instructions.md`, `CLAUDE.md` et `GEMINI.md`. En cas de différence, appliquer ce fichier `AGENTS.md`.

## Règle initiale obligatoire

Avant toute modification ou proposition de modification :

1. Exécuter `git status --short --branch`.
2. Identifier la branche active.
3. Identifier les fichiers que la demande concerne.
4. Vérifier que la branche et les fichiers appartiennent au même module.
5. Si une règle n'est pas respectée, s'arrêter avant toute modification et demander à l'utilisateur l'action nécessaire.

## Git et branches

- Ne jamais modifier, committer, merger, rebaser, supprimer ou pousser directement sur `main`.
- Ne jamais utiliser `push --force` ou contourner une protection GitHub.
- Ne jamais committer ou pousser automatiquement sans demande explicite.
- Travailler uniquement sur la branche du module demandé :
  - M1 : `m1_cliniques`
  - M2 : `m2_ambulances`
  - M3 : `m3_tournees_amb`
  - M4 : `m4_infirmiers`
  - M5 : `m5_blocs`
  - M6 : `m6_personnel`
  - M7 : `m7_lits`
  - M8 : `m8_budget`
- Si la branche active ne correspond pas au module demandé, ne rien modifier. Demander à l'utilisateur de basculer vers la bonne branche ou proposer uniquement la commande appropriée.
- Une tâche touchant plusieurs modules nécessite une branche dédiée ou une validation explicite.
- Toute intégration dans `main` doit être faite par Pull Request avec revue et validations réussies.

## Affectation obligatoire des fichiers

| Module | Branche | Fichiers autorisés pour le module |
|---|---|---|
| M1 | `m1_cliniques` | `modules/m1_cliniques.py`, `routes/m1_routes.py`, `templates/m1_cliniques.html`, `tests/test_m1_cliniques.py` |
| M2 | `m2_ambulances` | `modules/m2_ambulances.py`, `routes/m2_routes.py`, `templates/m2_ambulances.html`, `tests/test_m2_ambulances.py` |
| M3 | `m3_tournees_amb` | `modules/m3_tournees_amb.py`, `routes/m3_routes.py`, `templates/m3_tournees_amb.html`, `tests/test_m3_tournees_amb.py` |
| M4 | `m4_infirmiers` | `modules/m4_infirmiers.py`, `routes/m4_routes.py`, `templates/m4_infirmiers.html`, `tests/test_m4_infirmiers.py` |
| M5 | `m5_blocs` | `modules/m5_blocs.py`, `routes/m5_routes.py`, `templates/m5_blocs.html`, `tests/test_m5_blocs.py` |
| M6 | `m6_personnel` | `modules/m6_personnel.py`, `routes/m6_routes.py`, `templates/m6_personnel.html`, `tests/test_m6_personnel.py` |
| M7 | `m7_lits` | `modules/m7_lits.py`, `routes/m7_routes.py`, `templates/m7_lits.html`, `tests/test_m7_lits.py` |
| M8 | `m8_budget` | `modules/m8_budget.py`, `routes/m8_routes.py`, `templates/m8_budget.html`, `tests/test_m8_budget.py` |

## Fichiers protégés

Ne pas modifier les éléments suivants sans demande explicite de l'utilisateur et validation indépendante :

- `app.py`
- `routes/__init__.py`
- `templates/base.html`
- `templates/index.html`
- `static/css/style.css`
- `static/js/main.js`
- `data/`
- `requirements.txt`
- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `.github/`
- `.gitignore`
- `.env`, licences locales, identifiants, jetons et autres secrets

Toute modification protégée doit être expliquée, isolée, testée et envoyée par Pull Request.

## Portée des modifications

- Modifier uniquement les fichiers nécessaires au module demandé.
- Ne pas réécrire les autres modules ou fichiers communs pour corriger un problème local.
- Préserver les routes, noms de fichiers, contrats d'interface et architecture Flask existants.
- Ne pas supprimer plusieurs fichiers ou un fichier protégé sans confirmation explicite.
- Ne pas changer les dépendances sans justification et mise à jour de `requirements.txt`.

## Contrat Python commun

- Le code, les noms descriptifs et les commentaires doivent être en français.
- Chaque module doit exposer exactement `solve(data: dict, params: dict) -> dict`.
- Le résultat doit conserver les clés `statut`, `objectif`, `solution` et `temps`.
- Utiliser les dépendances existantes avant d'en ajouter de nouvelles.
- Ne jamais ajouter de clés API, licences Gurobi, mots de passe, jetons ou secrets au dépôt.

## Tests et validation

- Ajouter ou mettre à jour le test du module concerné dans `tests/`.
- Pour un module, exécuter `pytest tests/test_<module>.py` lorsque le test existe.
- Pour une modification commune, exécuter `pytest`.
- Vérifier les diagnostics et erreurs de syntaxe.
- Ne pas masquer les erreurs ni laisser de fichiers temporaires, caches, journaux locaux ou sorties générées dans le dépôt.

## Bonnes pratiques GitHub

- Utiliser des commits atomiques avec des messages clairs en français.
- Rester sur une branche correspondant à une seule responsabilité.
- Créer une Pull Request vers `main` avec les fichiers modifiés, les tests réalisés et les impacts.
- Respecter `CODEOWNERS` et les protections de branche.
- Ne jamais demander à l'utilisateur de contourner une validation ou une protection GitHub.

## Comportement obligatoire de l'agent

- Commencer chaque tâche en vérifiant la branche active et la portée des fichiers.
- Refuser toute modification directe de `main` et proposer la branche du module concerné.
- Si un fichier protégé est demandé, s'arrêter avant la modification et demander une validation explicite.
- Ne pas supposer qu'une modification commune est approuvée.
- Résumer les fichiers modifiés, les validations effectuées et les prochaines actions.

## Compatibilité entre assistants

- Codex, Claude Code et les assistants compatibles OpenAI/Anthropic doivent lire ce fichier `AGENTS.md`.
- Claude Code doit aussi lire `CLAUDE.md` et appliquer les règles importées depuis `AGENTS.md`.
- Gemini et Antigravity doivent lire `GEMINI.md` et appliquer les règles importées depuis `AGENTS.md`.
- Copilot doit lire `.github/copilot-instructions.md`, qui renvoie vers ce fichier.

Une convention Markdown d'instructions ne remplace pas les protections GitHub ou les restrictions locales du dépôt. Elles doivent être complétées par les règles de branche sur GitHub.
