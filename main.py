from flask import Flask
import os
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

@app.route('/')
def home():
    return "Bot Joubert ON! - Ta funcionando, so!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("E ai Joubert! Bot ON! Siga fiel!")

def run_bot():
    if not TOKEN:
        print("FALTA TOKEN!")
        return
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

# Inicia o bot em segundo plano
threading.Thread(target=run_bot, daemon=True).start()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
