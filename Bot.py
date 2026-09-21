import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Olá! Eu sou o Yaris.\n\n"
        "🧠 Estou sendo preparado para conversar com você usando IA!"
    )


async def mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 Recebi sua mensagem!\n\n"
        "Ainda estou sendo conectado à minha inteligência artificial. 🧠"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensagem))

    print("🤖 Yaris iniciado!")
    app.run_polling()


if __name__ == "__main__":
    main()
