
import os
import threading
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = (os.getenv("BOT_TOKEN") or os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("TELEGRAM_TOKEN") or "").strip()

async def start(update, context):
    await update.message.reply_text("🔥 BOT BLINDADO ON! Fala Joubert! Deu certo! To VIVO! Deus é fiel!")

def run_bot():
    if not TOKEN:
        print("ERRO: SEM TOKEN!")
        return
    print("BOT INICIADO!")
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.run_polling()

app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "BOT DO JOUBERT ONLINE - Deus é fiel!"

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host='0.0.0.0', port=port)
