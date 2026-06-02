import re
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8886489009:AAEM2bb51y__PE6Taxp3doK2dFb_ZkSvp3A"

seen_links = set()

async def check_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    links = re.findall(r'https?://\S+|t\.me/\S+', update.message.text)

    for link in links:
        if link in seen_links:
            try:
                await update.message.delete()
            except:
                pass
            return

        seen_links.add(link)

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, check_links)
)

app.run_polling()
