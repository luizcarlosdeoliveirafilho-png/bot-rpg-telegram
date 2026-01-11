from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv(8095198946:AAEIy8mWjWY3ptlf9Q2Nfn0eaSU9CZJG_7s )

async def start( update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Bem-vindo ao Lendas do Brasil RPG!\nUse /criar para começar."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
