from telegram.ext import Updater, CommandHandler
from app import settings, views


class Bot:
    def __init__(self) -> None:
        self.updater = Updater(token=settings.API_TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher

        # Adding handlers to dispatcher
        self.start_handler = CommandHandler("start", views.start)
        self.dispatcher.add_handler(self.start_handler)

    def run(self):
        if settings.MODE == "PRODUCTION":
            self.updater.start_webhook(
                listen="0.0.0.0",
                port=settings.PORT,
                url_path=settings.API_TOKEN,
            )
            self.updater.bot.setWebhook(settings.APP_URL + settings.API_TOKEN)
        else:
            print("Running ...")
            self.updater.start_polling()
            self.updater.idle()
