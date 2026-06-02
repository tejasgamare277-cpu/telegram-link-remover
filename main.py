import re
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8886489009:AAEJYkjsgRYovRb42wJ1e2SlV2UHDCcBz7s"

seen_links = set()

async def check_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    links = re.findall(r'https?://\S+|t\.me/\S+', update.message.text)

    for link in links:
        if link in seen_links:
            try:
                await update.message.delete()
            except Exception as e:
                print(e)
            return

        seen_links.add(link)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_links))

if __name__ == "__main__":
    print("Bot starting...")
    app.run_polling()
