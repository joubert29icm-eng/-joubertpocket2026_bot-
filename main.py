from flask import Flask
import threading, os, asyncio, random
from datetime import datetime, timezone
import telegram

app = Flask(__name__)
@app.route('/')
def home(): return "Bot Online - Deus é fiel!"
def run_web(): app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
threading.Thread(target=run_web).start()

PARES_FOREX_REAL = [
    "EUR/USD","GBP/USD","USD/JPY","AUD/USD","USD/CAD",
    "EUR/GBP","EUR/JPY","GBP/JPY","AUD/JPY","EUR/AUD",
    "NZD/USD","USD/CHF","EUR/CHF","GBP/CHF","EUR/CAD"
]

FICHA = os.getenv("TELEGRAM_BOT_TOKEN")
ID_DO_CHAT = os.getenv("ID_DO_CHAT_DO_TELEGRAM")

async def enviar():
    if not FICHA or not ID_DO_CHAT:
        print("Aguardando TOKEN...")
        return
    bot = telegram.Bot(token=FICHA)
    while True:
        par = random.choice(PARES_FOREX_REAL)
        agora = datetime.now(timezone.utc)
        msg = f"🔥 SINAL POCKET 2026 🔥\n\nPar: {par}\nHorário: {agora.strftime('%H:%M')} UTC\n\nDeus é fiel! 🙏"
        try:
            await bot.send_message(chat_id=ID_DO_CHAT, text=msg)
        except Exception as e:
            print(e)
        await asyncio.sleep(300)

if __name__ == "__main__":
    asyncio.run(enviar())
