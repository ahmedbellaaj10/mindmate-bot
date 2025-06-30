from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"Received message: {user_message}")
    await update.message.reply_text("👋 Hello!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()