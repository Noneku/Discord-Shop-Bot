import logging

# Configuration du format d'affichage
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Configuration du logger principal
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt=DATE_FORMAT
)

def get_logger(name: str):
    """
    Retourne un logger avec un nom spécifique.
    Exemple : logger = get_logger("bot")
    """
    return logging.getLogger(name)
