import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Token del bot (se leerá desde las variables de entorno en Railway)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Función que responde al comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Soy tu bot de Telegram.")

# Función que repite cualquier mensaje que envíen
async def responder(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)

# Configurar el bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Agregar comandos y respuestas
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    # Iniciar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
