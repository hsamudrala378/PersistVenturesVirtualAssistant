import schedule
import time
from telegram.ext import Updater, CommandHandler

# Function that sends a scheduled message
def send_reminder(context):
    context.bot.send_message(chat_id="876472713", text="This is your daily reminder!")

# Function to start the bot
def start(update, context):
    update.message.reply_text("Welcome to Persist Ventures Bot!")

def help_command(update, context):
    update.message.reply_text("""
    Available commands:
    /start - Welcome message
    /help - List of available commands
    """)

def main():
    # Initialize the Updater object
    updater = Updater("7916163960:AAGgD83ecNoGoBVqwsKuTdKtMpDRUeBL2wM", use_context=True)
    dispatcher = updater.dispatcher

    # Register the commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Schedule the daily reminder at 10:00 AM
    schedule.every().day.at("10:00").do(send_reminder, context=updater)

    # Polling for updates and running the scheduler
    updater.start_polling()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
