from utils.logger import get_logger
from config.settings import Settings
import requests

logger = get_logger("startup")


# --------------------------------------------------
# Vérification des variables d'environnement
# --------------------------------------------------
def check_env_variables():
    logger.info("Vérification des variables d'environnement...")

    if not Settings.discord_bot_token:
        logger.error("❌ DISCORD_BOT_TOKEN est manquant dans le fichier .env.")
        return False
    
    logger.info("✔ Variables d'environnement OK.")
    return True


# --------------------------------------------------
# Vérification de l'accès API
# --------------------------------------------------
def check_api_access():
    logger.info(f"Test de connexion à l'API : {Settings.api_url()}")

    try:
        response = requests.get(Settings.api_url(), timeout=5)
        if response.status_code == 200:
            logger.info("✔ Accès à l'API réussi.")
            return True

        logger.error(f"❌ Code inattendu retourné par l'API : {response.status_code}")
        return False

    except requests.RequestException as e:
        logger.error(f"❌ Impossible de contacter l'API : {e}")
        return False


# --------------------------------------------------
# Fonction principale — renvoie True si tout est OK
# --------------------------------------------------
def run_startup_checks():
    logger.info("----- DÉMARRAGE DES CHECKS -----")

    checks = [
        check_env_variables(),
        check_api_access()
    ]

    all_ok = all(checks)

    if all_ok:
        logger.info("✔ Tous les checks sont validés. Démarrage du bot...")
    else:
        logger.error("❌ Certains checks ont échoué. Le bot NE sera PAS lancé.")

    logger.info("----- CHECKS TERMINÉS -----")

    return all_ok