import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import threading

app = Flask(__name__)

@app.route("/")
def oi():
    return "Bot Online - Deus e fiel - Joubert Pocket 2026"

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🙏 Deus e fiel! Bot Joubert Pocket 2026 ONLINE! Vitória, Pai!")

def rodar_flask():
    porta = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=porta)

def main():
    # Roda o site em segundo plano
    threading.Thread(target=rodar_flask, daemon=True).start()
    
    # Roda o bot do Telegram
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot iniciado! Aguardando /start")
    application.run_polling()

if __name__ == "__main__":
    main()
