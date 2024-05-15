import os, logging
from functools import wraps
from telegram import Update
from telegram.ext import CommandHandler, Application, ContextTypes


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def restricted(func):
    @wraps(func)
    def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs) -> None:
        if update.message.chat.type != "private" and update.effective_chat.username != "BernardAbaidoo":
            return context.bot.send_message(chat_id=update.effective_chat.id, text="you are not allowed to send this message")
        return func(update, context, *args, **kwargs)
    return wrapped

@restricted
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello i am the AFK Data Manager, how can i held you!")

@restricted
async def get_message_files(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    print("\n\n", update, "\n\n")
    command, messages = update.message.text.split(maxsplit=1)
    
    groups = []
    # user_groups = await context.bot.get_chat_member(user_id=user_id)
    # print("\n\n", user_groups, "\n\n")
    
    
    if "payment" in messages and "issue" in messages:
        # TODO: get all documents with 'payment' and 'issue' in document name
        pass
    if "payment" in messages and "report" in messages:
        # TODO: get all documents with 'payment' and 'report' in document name
        pass
    
    if len(groups) > 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{groups[0]}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No groups found")
    

def main() -> None:
    application = Application.builder().token(os.environ.get('TELEGRAM_BOT_TOKEN')).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("compile", get_message_files))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
