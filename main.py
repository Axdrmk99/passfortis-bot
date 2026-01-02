# main.py
import random
from zxcvbn import zxcvbn
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

# ⚠ Replace with environment variable for safe deployment
BOT_TOKEN = "8254696772:AAFEepz6onei2yLu8hcigR7rZ2T0hoOM010"

# Futuristic tips and commentary
tips = [
    "⚡ Matrix detected weakness. Fortify immediately!",
    "💾 Security protocols engaged. Hacker likelihood low.",
    "🛡️ Shield optimal. Stability verified.",
    "⚡ Encryption integrity at risk. Upgrade recommended!",
    "🔐 Cyber stability high. Keep passwords strong!"
]

futuristic_comments = [
    "⚡ Cyber AI scanning… protocols updated.",
    "💾 Encryption matrix analyzed. Security enhanced.",
    "🛡️ Hacker intrusion probability minimal.",
    "🔐 Firewall integrity confirmed.",
    "⚡ Quantum matrix simulation complete."
]

# Function to make the password stronger but keep it recognizable
def strengthen_password(pw):
    # Replace letters with symbols
    substitutions = {
        "a": "@", "A": "@",
        "i": "1", "I": "1",
        "s": "$", "S": "$",
        "o": "0", "O": "0",
        "e": "3", "E": "3"
    }
    pw_strong = "".join(substitutions.get(c, c) for c in pw)

    # Randomly capitalize some letters
    pw_strong = "".join(c.upper() if random.random() < 0.3 else c for c in pw_strong)

    # Add 2 random symbols/numbers at the end
    chars = "!@#$%^&*()_+1234567890"
    pw_strong += "".join(random.choice(chars) for _ in range(2))

    return pw_strong

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👾 Welcome to PassFortisBot v4 – your futuristic password guardian.\n"
        "Send me any password, and I'll analyze its strength, show crack time, and suggest a stronger version keeping it recognizable! 🔐\n\n"
        "Type /help to see all commands."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Commands:\n"
        "/start - Introduction\n"
        "/help - Show this message\n"
        "/generate - Generate a strong random password instantly\n\n"
        "Or just send me a password and I'll analyze it for you!"
    )

# /generate command (full random)
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pw = strengthen_password("PassFortisBot123")  # example strong password
    tip = random.choice(futuristic_comments)
    await update.message.reply_text(
        f"⚡ Generated strong password: `{pw}`\n{tip}",
        parse_mode="Markdown"
    )

# Analyze and strengthen user password
async def analyze_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pw = update.message.text
    result = zxcvbn(pw)
    score = result['score']  # 0-4
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']

    # Strengthen the same password (even if strong, optionally)
    suggested_pw = strengthen_password(pw) if score < 4 else pw

    # Customize futuristic commentary
    if score <= 1:
        comment = "⚡ Alert! Encryption integrity compromised!"
    elif score == 2:
        comment = "🔐 Caution! Stability moderate."
    elif score == 3:
        comment = "🛡️ Good! Integrity strong."
    else:
        comment = "💎 Excellent! Hacker scan highly unlikely."

    comment += "\n" + random.choice(futuristic_comments)
    tip = random.choice(tips)

    # Build response
    response = (
        f"⚡ *PassFortis Scan Report* ⚡\n\n"
        f"💠 Password analyzed: `{pw}`\n"
        f"📊 Strength Score: {score}/4\n"
        f"⏱️ Estimated Crack Time: {crack_time}\n"
        f"🔑 Suggested Upgrade: `{suggested_pw}`\n\n"
        f"{comment}\n{tip}"
    )

    await update.message.reply_text(response, parse_mode="Markdown")

# Main bot setup
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("generate", generate))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), analyze_password))
    print("🚀 PassFortisBot v4 is online and guarding passwords!")
    app.run_polling()
