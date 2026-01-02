# main.py
import random
from zxcvbn import zxcvbn
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

# ⚠ For safe deployment, replace this with environment variable
# BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_TOKEN = "8254696772:AAFEepz6onei2yLu8hcigR7rZ2T0hoOM010"

# Futuristic tips
tips = [
    "⚡ Matrix detected weakness. Fortify immediately!",
    "💾 Security protocols engaged. Hacker likelihood low.",
    "🛡️ Shield optimal. Stability verified.",
    "⚡ Encryption integrity at risk. Upgrade recommended!",
    "🔐 Cyber stability high. Keep passwords strong!"
]

# Futuristic extra commentary
futuristic_comments = [
    "⚡ Cyber AI scanning… protocols updated.",
    "💾 Encryption matrix analyzed. Security enhanced.",
    "🛡️ Hacker intrusion probability minimal.",
    "🔐 Firewall integrity confirmed.",
    "⚡ Quantum matrix simulation complete."
]

# Generate a strong password
def generate_password(length=14):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    return ''.join(random.choice(chars) for _ in range(length))

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👾 Welcome to PassFortisBot v3 – your futuristic password guardian.\n"
        "Send me any password, and I'll analyze its strength, show crack time, and suggest a stronger one if needed! 🔐\n\n"
        "Type /help to see all commands."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Commands:\n"
        "/start - Introduction\n"
        "/help - Show this message\n"
        "/generate - Generate a strong password instantly\n\n"
        "Or just send me a password and I'll analyze it for you!"
    )

# /generate command
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pw = generate_password()
    tip = random.choice(futuristic_comments)
    await update.message.reply_text(
        f"⚡ Generated secure password: `{pw}`\n{tip}",
        parse_mode="Markdown"
    )

# Analyze user passwords
async def analyze_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pw = update.message.text
    result = zxcvbn(pw)
    score = result['score']  # 0-4
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']

    # Always suggest a different password if less than perfect
    if score < 4:
        suggested_pw = generate_password()
    else:
        suggested_pw = pw

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

# Main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("generate", generate))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), analyze_password))
    print("🚀 PassFortisBot v3 is online and guarding passwords!")
    app.run_polling()
