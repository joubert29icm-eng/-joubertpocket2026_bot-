import os
import asyncio
import random
from datetime import datetime, timezone
import telegram

PARES_FOREX_REAL = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD",
    "EUR/GBP", "EUR/JPY", "GBP/JPY", "AUD/JPY", "EUR/AUD",
    "NZD/USD", "USD/CHF", "EUR/CHF", "GBP/CHF", "EUR/CAD"
]

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def enviar():
    if not TOKEN or not CHAT_ID:
        print("Aguardando TOKEN...")
        return
    bot = telegram.Bot(token=TOKEN)
    par = random.choice(PARES_FOREX_REAL)
    direcao = random.choice(["COMPRA", "VENDA"])
    agora = datetime.now(timezone.utc).strftime("%H:%M")
    msg = f"🚀 SINAL FOREX REAL\n\nPar: {par} (REAL SEM OTC)\nDirecao: {direcao}\nHorario: {agora} UTC\n\n✅ So FOREX REAL"
    await bot.send_message(chat_id=CHAT_ID, text=msg)

async def main():
    print("joubertpocket2026_bot INICIADO - SO FOREX REAL")
    while True:
        try:
            await enviar()
        except Exception as e:
            print(e)
        await asyncio.sleep(300)

if __name__ == "__main__":
    asyncio.run(main())
