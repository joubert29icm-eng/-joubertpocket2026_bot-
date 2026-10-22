import os
import threading
from flask import Flask
from telegram.ext import Application, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")

app = Flask(__name__)

@app.route('/')
def home():
    return "HELLO WORLD! Bot Joubert is alive!"

async def start(update, context):
    await update.message.reply_text("Olá Joubert! Deus é fiel! Eu estou vivo e funcionando! 🙏")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    print("INICIANDO O BOT...")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("BOT INICIADO COM SUCESSO!")
    application.run_polling()
