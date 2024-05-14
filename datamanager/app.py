import logging

from telegram import Update
from telegram.ext import CommandHandler, Application, ContextTypes


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context:
        pass
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello i am the AFK Data Manager, how can i held you!")

async def get_message_files(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    bot_data = await context.bot.get_updates()
    print(bot_data)
    command, messages = update.message.text.split(maxsplit=1)
    
    
    if "payment" in messages and "issue" in messages:
        # TODO: get all documents with 'payment' and 'issue' in document name
        pass
    if "payment" in messages and "report" in messages:
        # TODO: get all documents with 'payment' and 'report' in document name
        pass
    

def main() -> None:
    application = Application.builder().token("6735004489:AAFOV9Bq0LaGmIgKtU6Aoaji2MxIjZmHME0").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("compile", get_message_files))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
