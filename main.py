import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Online - Deus e fiel! Joubert Pocket 2026 ONLINE! Vitoria, Pai!")

def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot Online - Deus e fiel")
    app.run_polling()

if __name__ == "__main__":
    main()
