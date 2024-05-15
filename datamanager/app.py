import os, logging
from functools import wraps
from telegram import Update
from telegram.ext import CommandHandler, Application, ContextTypes


logging.basicConfig(filename="./datamanager/logs/info.log", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def restricted(func):
    @wraps(func)
    def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs) -> None:
        if update.message.chat.type != "private" and update.effective_chat.username != "BernardAbaidoo":
            username = update.message.from_user.name
            return context.bot.send_message(chat_id=update.effective_chat.id, text=f"{username} you are not allowed to send this message \U0001F595")
        return func(update, context, *args, **kwargs)
    return wrapped


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="\U0001F44B Hello\nAFK Data Manager here\nhow can i help you!\nyou can use /commands")


# @restricted
async def get_message_files(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    command, messages = update.message.text.split(maxsplit=1)
    group_id = messages.split("-")[-1]
    group_data = await context.bot.get_chat(chat_id=f"-{group_id}")
    
    print("\n\n", dir(group_data), "\n\n")
    
    if "payment" in messages and "issue" in messages:
        # TODO: get all documents with 'payment' and 'issue' in document name
        pass
    if "payment" in messages and "report" in messages:
        # TODO: get all documents with 'payment' and 'report' in document name
        pass
    
    # if len(groups) > 0:
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{groups[0]}")
    # else:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="No groups found")


async def get_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="/start\n/compile\n/commands\n/fetch")


async def get_group_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    user_id = os.environ.get("ADMIN_USER_ID")
    group_name = update.message.chat.title
    await context.bot.send_message(chat_id=user_id, text=f"{group_name}'s generated identification is {chat_id}")


def main() -> None:
    application = Application.builder().token(os.environ.get('TELEGRAM_BOT_TOKEN')).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("compile", get_message_files))
    application.add_handler(CommandHandler("fetch", get_group_id))
    application.add_handler(CommandHandler("commands",get_commands))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
