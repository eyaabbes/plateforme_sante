"""Script de lancement du serveur web Flask.

Utilisation :
    python run.py
"""

import os
from app import create_app


def main() -> None:
    """Démarre le serveur de développement Flask."""
    app = create_app()
    host = os.environ.get("FLASK_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_PORT", "5000"))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    main()
