# futuristic_passfortisbot_v2.py
import random
from zxcvbn import zxcvbn
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ⚠ Use environment variable in deployment for security
BOT_TOKEN = "8254696772:AAFEepz6onei2yLu8hcigR7rZ2T0hoOM010"

# Futuristic tips
tips = [
    "⚡ Matrix detected weakness. Fortify immediately!",
    "💾 Security protocols engaged. Hacker likelihood low.",
    "🛡️ Shield optimal. Stability verified.",
    "⚡ Encryption integrity at risk. Upgrade recommended!",
    "🔐 Cyber stability high. Keep passwords strong!"
]

# Generate a strong, futuristic password
def generate_password(length=14):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    return ''.join(random.choice(chars) for _ in range(length))

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👾 Welcome to PassFortisBot v2 – your futuristic password guardian.\n"
        "Send any password, and I’ll scan its strength, show crack time, and suggest a better one if needed! 🔐"
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Commands:\n"
        "/start - Introduction\n"
        "/help - This message\n"
        "/generate - Create a strong password instantly\n\n"
        "Or just send me a password to analyze!"
    )

# /generate command
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pw = generate_password()
    await update.message.reply_text(f"⚡ Generated secure password: `{pw}`", parse_mode="Markdown")

# Main password analysis
async def analyze_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pw = update.message.text
    result = zxcvbn(pw)
    score = result['score']  # 0-4
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']

    # Always suggest a different password if weak or medium
    if score < 3:
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
        comment = "🛡️ Excellent! Hacker scan highly unlikely."

    # Pick a random tip
    tip = random.choice(tips)

    # Build the response with futuristic style
    response = (
        f"⚡ *PassFortis Scan Report* ⚡\n\n"
        f"💠 Password analyzed: `{pw}`\n"
        f"📊 Strength Score: {score}/4\n"
        f"⏱️ Estimated Crack Time: {crack_time}\n"
        f"🔑 Suggested Upgrade: `{suggested_pw}`\n\n"
        f"{comment}\n{tip}"
    )

    await update.message.reply_text(response, parse_mode="Markdown")

# Setup bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("generate", generate))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), analyze_password))
    print("🚀 PassFortisBot v2 is online and guarding passwords!")
    app.run_polling()
