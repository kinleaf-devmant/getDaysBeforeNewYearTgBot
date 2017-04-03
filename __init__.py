import os
from telegram.ext import Updater, CommandHandler
from time_before_ny import time_before_ny

# environment variable is as unique as possible
TELEGRAM_BOT_API_KEY = os.getenv("GET_DAYS_BEFORE_NEW_YEAR_TG_BOT_API_KEY", "WRONG KEY")

assert(TELEGRAM_BOT_API_KEY != "WRONG_KEY")
updater = Updater(TELEGRAM_BOT_API_KEY)


# on start command
def start(bot, update):
    timediff = time_before_ny().days
    text = "It's {} days before New Year, use /start command to check again"\
        .format(timediff)
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

# create handlers
start_handler = CommandHandler('start', start)

# add handlers to dispatcher
updater.dispatcher.add_handler(start_handler)

if __name__ == "__main__":
    # listen
    updater.start_polling()