import discord
from discord.ext import commands
from utils.startup_checks import run_startup_checks
from config.settings import Settings
from utils.logger import get_logger

logger = get_logger("bot")


# 1. Config Intents
intents = discord.Intents.default()
intents.message_content = True

# 2. Bot
bot = commands.Bot(command_prefix="!", intents=intents)


# 3. Startup checks AVANT lancement
if not run_startup_checks():
    logger.error("Impossible de lancer le bot. Arrêt.")
    exit(1)


# 4. Event bot prêt
@bot.event
async def on_ready():
    logger.info(f"Bot connecté en tant que {bot.user}")


# 5. Charger les cogs automatiquement
@bot.event
async def setup_hook():
    await bot.load_extension("cogs.shop")
    await bot.load_extension("cogs.general")
    await bot.load_extension("cogs.admin")
    logger.info("Cogs chargés avec succès")


# 6. Run bot
bot.run(Settings.discord_bot_token())
