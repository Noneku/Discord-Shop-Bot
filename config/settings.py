import os
from dotenv import load_dotenv

load_dotenv()

# Discord Bot Token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# API Configuration
API_URL= os.getenv('API_URL')

# Update interval
UPDATE_INTERVAL= int(os.getenv('UPDATE_INTERVAL', 0))


