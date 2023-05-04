import os
import telegram
import openai
import logging
from dotenv import load_dotenv
# import wandb
from telegram.ext import ApplicationBuilder, CallbackContext, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import date

load_dotenv()
# CONSTANTS
BOT_NAME = os.getenv('BOT_NAME')
GPT_API_KEY = os.getenv('GPT_API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_AUTHAURIZE_CHANNEL = os.getenv('TELEGRAM_AUTHAURIZE_CHANNEL')
GPT_MODEL = os.getenv('GPT_MODEL')
FIRST_PROMPT = {"role": "system", "content": f'{os.getenv("DEFAULT_PROMPT")} Current date ${date.today()}'}

# SYSLOG
logger = logging.getLogger()

# Global variables
conversation_history = [FIRST_PROMPT]

# Init functions
def initLogging(level: int = logging.INFO):
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=level
    )

def initOpenAI():
    openai.api_key = GPT_API_KEY


# Telegram commands
async def reset(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id == int(TELEGRAM_AUTHAURIZE_CHANNEL):
        conversation_history.clear()
        conversation_history.append(FIRST_PROMPT)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{BOT_NAME} was reset')

async def setagent(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id == int(TELEGRAM_AUTHAURIZE_CHANNEL):
        text = update.message.text.removeprefix('/setagent')
        if (text == None or len(text) == 0):
            await context.bot.send_message(chat_id=update.effective_chat.id, text="please set the agent that way :\n/setagent [Prompt]")
            return
        conversation_history.clear()
        conversation_history.append({"role": "system", "content": text})
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{BOT_NAME} will have as pre-prompt : {text.removeprefix("/setagent")}')

async def kill():
    exit()

async def echo(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(''.join([str(elem) for elem in conversation_history]))
    logger.info(f'receive {update.message.text}')
    conversation_history.append(
        {"role": "user", "content": f"{update.message.text}"})
    if update.message.chat_id == int(TELEGRAM_AUTHAURIZE_CHANNEL):
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=conversation_history
        )['choices'][0]['message']
        conversation_history.append(response)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response['content'])

# Telegram bot
def runTelegramBot():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    # register commands
    application.add_handler(CommandHandler(setagent.__name__, setagent))
    application.add_handler(CommandHandler(reset.__name__, reset))
    application.add_handler(CommandHandler(kill.__name__, kill))
    # other commands
    application.add_handler(MessageHandler(
        filters.TEXT & (~filters.COMMAND), echo))
    # run the bot
    application.run_polling()


def main():
    initLogging()
    initOpenAI()
    runTelegramBot()


if __name__ == "__main__":
    main()
