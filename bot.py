#!/usr/bin/env python3
"""
Vanish Bot - Auto-delete messages
TOKEN aman di environment variables
"""

import os
import sys
import logging
from telegram.ext import Application

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_token():
    """Ambil token dari environment variable"""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not token:
        logging.error("❌ Token tidak ditemukan!")
        logging.info("💡 Cara set token:")
        logging.info("  1. Di Railway: Set env var TELEGRAM_BOT_TOKEN")
        logging.info("  2. Local: Buat file .env dengan TELEGRAM_BOT_TOKEN=...")
        sys.exit(1)
    
    # Validasi format token
    if ":" not in token or len(token) < 30:
        logging.error("❌ Token format salah!")
        sys.exit(1)
    
    return token

async def start(update, context):
    await update.message.reply_text("Halo! Saya VanishBot 🤖")

def main():
    """Main function"""
    logging.info("🚀 Starting VanishBot...")
    
    # Get token securely
    TOKEN = get_token()
    logging.info("✅ Token loaded securely")
    
    # Build bot
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    # Start bot
    logging.info("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
