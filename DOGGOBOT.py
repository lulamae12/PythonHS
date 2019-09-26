api = '856255486:AAGMiHjLXDRrVjEYqdiy4KoSSC2mqoDeTzA'
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater(api)

updater.dispatcher.add_handler(CommandHandler('hello', hello))


while True:
    updater.start_polling()
    updater.idle()
