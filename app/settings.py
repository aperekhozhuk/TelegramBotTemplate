import os


API_TOKEN = os.environ["TELEGRAM_BOT_API_TOKEN"]
DATABASE_URL = os.environ["DATABASE_URL"]
# MODE : "DEVELOPMENT" or "PRODUCTION"
MODE = os.environ.get("TELEGRAM_BOT_MODE", default="DEVELOPMENT")
PORT = int(os.environ.get("PORT", default=5000))
# APP_URL - needed for webhook
APP_URL = os.environ.get("TELEGRAM_BOT_APP_URL", default=None)
