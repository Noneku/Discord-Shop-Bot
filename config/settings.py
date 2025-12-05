import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    _DISCORD_BOT_TOKEN: str = os.getenv("DISCORD_BOT_TOKEN")
    _API_URL: str = os.getenv("API_URL")
    _UPDATE_INTERVAL: int = int(os.getenv("UPDATE_INTERVAL", 0))

    # ------------------------
    # GETTERS (lecture seule)
    # ------------------------

    @classmethod
    def discord_bot_token(cls) -> str:
        return cls._DISCORD_BOT_TOKEN

    @classmethod
    def api_url(cls) -> str:
        return cls._API_URL

    @classmethod
    def update_interval(cls) -> int:
        return cls._UPDATE_INTERVAL

    # ------------------------
    # VALIDATION
    # ------------------------

    @classmethod
    def validate(cls):
        if not cls._DISCORD_BOT_TOKEN:
            raise ValueError("❌ DISCORD_BOT_TOKEN est manquant dans .env")

        if not cls._API_URL:
            raise ValueError("❌ API_URL est manquant dans .env")

        if cls._UPDATE_INTERVAL <= 0:
            raise ValueError("❌ UPDATE_INTERVAL doit être > 0")
