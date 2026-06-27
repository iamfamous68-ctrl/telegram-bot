from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8822418395:AAFGJ8cU5B2YlfUEhYPjULS-j-wNAohLk28"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men Abrorning birinchi botiman! 😊")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "salom":
        javob = "Salom! 😊"
    elif text == "seni kim yaratdi":
        javob = "Meni Abror yaratdi! 😎"
    else:
        javob = "Siz yozdingiz: " + update.message.text

    await update.message.reply_text(javob)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot ishga tushdi...")
app.run_polling()
