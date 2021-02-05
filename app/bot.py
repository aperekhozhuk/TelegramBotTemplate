from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from app import settings, views


class Bot:

    commands = ("start",)

    def __init__(self) -> None:
        self.updater = Updater(token=settings.API_TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.set_handlers()

    def set_handlers(self):
        # Setting command handlers by their names
        for command_name in self.commands:
            self.dispatcher.add_handler(
                CommandHandler(command_name, getattr(views, command_name))
            )

        # Handling unrecognized commands
        unknown_handler = MessageHandler(Filters.text, views.unknown)
        self.dispatcher.add_handler(unknown_handler)

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
