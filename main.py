# main.py
from zxcvbn import zxcvbn
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

BOT_TOKEN = "8254696772:AAFEepz6onei2yLu8hcigR7rZ2T0hoOM010"

# Futuristic flavor lines
futuristic_lines = [
    "⚡ Cyber AI suggests staying vigilant!",
    "💾 Matrix scan complete. Security enhanced!",
    "🛡️ Hacker intrusion probability minimal.",
    "🔐 Firewall integrity verified."
]

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👾 Welcome to PassFortisBot – your password guardian.\n\n"
        "Commands:\n"
        "/generate - Create a strong password from your words\n"
        "/checkpasswordstrength - Analyze any password\n\n"
        "Send a command to get started!"
    )

# /generate command
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ Please send me some words (like your name or favorite thing) and I'll generate a strong password based on them!"
    )

    async def generate_from_words(update2: Update, context2: ContextTypes.DEFAULT_TYPE):
        words = update2.message.text
        # Strengthen words into a password
        symbols = "!@#$%^&*()_+1234567890"
        pw = "".join(c.upper() if random.random() < 0.3 else c for c in words)
        pw += "".join(random.choice(symbols) for _ in range(2))
        flavor = random.choice(futuristic_lines)
        await update2.message.reply_text(f"⚡ Generated strong password: `{pw}`\n{flavor}", parse_mode="Markdown")
        # Remove this handler after running once
        context.bot.remove_handler(handler)

    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), generate_from_words)
    context.bot.add_handler(handler)

# /checkpasswordstrength command
async def check_password_strength(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ Send me the password you want to analyze, and I will show its strength and crack time."
    )

    async def analyze_password(update2: Update, context2: ContextTypes.DEFAULT_TYPE):
        pw = update2.message.text
        result = zxcvbn(pw)
        score = result['score']
        crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']
        flavor = random.choice(futuristic_lines)

        response = (
            f"⚡ PassFortis Scan Report ⚡\n\n"
            f"💠 Password analyzed: `{pw}`\n"
            f"📊 Strength Score: {score}/4\n"
            f"⏱️ Estimated Crack Time: {crack_time}\n\n"
            f"{flavor}"
        )

        await update2.message.reply_text(response, parse_mode="Markdown")
        # Remove this handler after running once
        context.bot.remove_handler(handler)

    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), analyze_password)
    context.bot.add_handler(handler)

# Main bot setup
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate", generate))
    app.add_handler(CommandHandler("checkpasswordstrength", check_password_strength))
    print("🚀 PassFortisBot is online and guarding passwords!")
    app.run_polling()
