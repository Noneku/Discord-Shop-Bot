from utils.logger import get_logger

logger = get_logger("startup")


# --------------------------------------------------
# Exemple : chaque check renvoie True (OK) ou False (échec)
# --------------------------------------------------

def check_env_variables():
    logger.info("Vérification des variables d'environnement...")
    # 👉 À compléter
    return True  # Remplace par False si échec


def check_internet():
    logger.info("Vérification de la connexion Internet...")
    # 👉 À compléter
    return True


def check_api_access(api_url: str):
    logger.info(f"Test de connexion à l'API : {api_url}")
    # 👉 À compléter
    return True


def check_required_files():
    logger.info("Vérification des fichiers nécessaires...")
    # 👉 À compléter
    return True


def check_python_version(min_version=(3, 10)):
    logger.info("Vérification de la version de Python...")
    # 👉 À compléter
    return True


def check_intents(intents):
    logger.info("Vérification des intents Discord...")
    # 👉 À compléter
    return True


def show_summary():
    logger.info("Résumé final de la configuration du bot :")
    # 👉 À compléter


# --------------------------------------------------
# Fonction principale — renvoie True si tout est OK
# --------------------------------------------------

def run_startup_checks(api_url=None, intents=None):
    logger.info("----- DÉMARRAGE DES CHECKS -----")

    checks = [
        check_python_version(),
        check_env_variables(),
        check_required_files(),
        check_internet()
    ]

    if api_url:
        checks.append(check_api_access(api_url))

    if intents:
        checks.append(check_intents(intents))

    show_summary()

    all_ok = all(checks)

    if all_ok:
        logger.info("✔ Tous les checks sont validés. Démarrage du bot...")
    else:
        logger.error("❌ Certains checks ont échoué. Le bot NE sera PAS lancé.")

    logger.info("----- CHECKS TERMINÉS -----")

    return all_ok
