# futuristic_passfortisbot_ready.py

import random
from zxcvbn import zxcvbn
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# -----------------------------
# ⚠ WARNING: For safe deployment, use environment variable instead of hardcoding
# Example: BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------------------
BOT_TOKEN = "8254696772:AAFEepz6onei2yLu8hcigR7rZ2T0hoOM010"

# Futuristic tips and encouragements
futuristic_tips = [
    "⚡ Encryption integrity at risk. Upgrade recommended!",
    "🛡️ Shield optimal. Cyber defenses strong.",
    "💾 Hacker scan unlikely. Safety verified.",
    "⚡ Matrix detected weakness. Fortify immediately.",
    "🛡️ Cyber stability high. Keep up the good work."
]

# Function to generate a strong password
def generate_strong_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    return ''.join(random.choice(chars) for _ in range(length))

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👾 Welcome to PassFortisBot, your futuristic password guardian.\n"
        "Send me any password and I'll analyze its strength, calculate crack time, and suggest stronger alternatives if needed. 🔐"
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Commands available:\n"
        "/start - Introduction\n"
        "/help - Show this message\n"
        "/generate - Generate a strong random password\n\n"
        "Or just send any password and I'll evaluate it!"
    )

# /generate command
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = generate_strong_password()
    await update.message.reply_text(f"⚡ Generated secure password: `{password}`", parse_mode="Markdown")

# Analyze user passwords
async def analyze_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_password = update.message.text
    result = zxcvbn(user_password)
    score = result['score']  # 0-4
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']

    # Suggested stronger password if weak
    suggested_password = generate_strong_password() if score < 3 else user_password

    # Pick a futuristic tip
    tip = random.choice(futuristic_tips)

    # Build response
    response = (
        f"⚡ Password Analysis Report ⚡\n\n"
        f"Password: `{user_password}`\n"
        f"Strength Score: {score}/4\n"
        f"Estimated crack time: {crack_time}\n"
        f"Suggested upgrade: `{suggested_password}`\n\n"
        f"{tip}"
    )

    await update.message.reply_text(response, parse_mode="Markdown")

# Main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("generate", generate))

    # Password messages
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), analyze_password))

    print("🚀 PassFortisBot is online and guarding passwords!")
    app.run_polling()
# futuristic_passfortisbot_ready.py

import random
from zxcvbn import zxcvbn
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# -----------------------------
# ⚠ WARNING: For safe deployment, use environment variable instead of hardcoding
# Example: BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------------------
BOT_TOKEN = "8254696772:AAFEepz6onei2yLu8hcigR7rZ2T0hoOM010"

# Futuristic tips and encouragements
futuristic_tips = [
    "⚡ Encryption integrity at risk. Upgrade recommended!",
    "🛡️ Shield optimal. Cyber defenses strong.",
    "💾 Hacker scan unlikely. Safety verified.",
    "⚡ Matrix detected weakness. Fortify immediately.",
    "🛡️ Cyber stability high. Keep up the good work."
]

# Function to generate a strong password
def generate_strong_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    return ''.join(random.choice(chars) for _ in range(length))

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👾 Welcome to PassFortisBot, your futuristic password guardian.\n"
        "Send me any password and I'll analyze its strength, calculate crack time, and suggest stronger alternatives if needed. 🔐"
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Commands available:\n"
        "/start - Introduction\n"
        "/help - Show this message\n"
        "/generate - Generate a strong random password\n\n"
        "Or just send any password and I'll evaluate it!"
    )

# /generate command
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = generate_strong_password()
    await update.message.reply_text(f"⚡ Generated secure password: `{password}`", parse_mode="Markdown")

# Analyze user passwords
async def analyze_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_password = update.message.text
    result = zxcvbn(user_password)
    score = result['score']  # 0-4
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']

    # Suggested stronger password if weak
    suggested_password = generate_strong_password() if score < 3 else user_password

    # Pick a futuristic tip
    tip = random.choice(futuristic_tips)

    # Build response
    response = (
        f"⚡ Password Analysis Report ⚡\n\n"
        f"Password: `{user_password}`\n"
        f"Strength Score: {score}/4\n"
        f"Estimated crack time: {crack_time}\n"
        f"Suggested upgrade: `{suggested_password}`\n\n"
        f"{tip}"
    )

    await update.message.reply_text(response, parse_mode="Markdown")

# Main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("generate", generate))

    # Password messages
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), analyze_password))

    print("🚀 PassFortisBot is online and guarding passwords!")
    app.run_polling()
# futuristic_passfortisbot_ready.py

import random
from zxcvbn import zxcvbn
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# -----------------------------
# ⚠ WARNING: For safe deployment, use environment variable instead of hardcoding
# Example: BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------------------
BOT_TOKEN = "8254696772:AAFEepz6onei2yLu8hcigR7rZ2T0hoOM010"

# Futuristic tips and encouragements
futuristic_tips = [
    "⚡ Encryption integrity at risk. Upgrade recommended!",
    "🛡️ Shield optimal. Cyber defenses strong.",
    "💾 Hacker scan unlikely. Safety verified.",
    "⚡ Matrix detected weakness. Fortify immediately.",
    "🛡️ Cyber stability high. Keep up the good work."
]

# Function to generate a strong password
def generate_strong_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    return ''.join(random.choice(chars) for _ in range(length))

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👾 Welcome to PassFortisBot, your futuristic password guardian.\n"
        "Send me any password and I'll analyze its strength, calculate crack time, and suggest stronger alternatives if needed. 🔐"
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Commands available:\n"
        "/start - Introduction\n"
        "/help - Show this message\n"
        "/generate - Generate a strong random password\n\n"
        "Or just send any password and I'll evaluate it!"
    )

# /generate command
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = generate_strong_password()
    await update.message.reply_text(f"⚡ Generated secure password: `{password}`", parse_mode="Markdown")

# Analyze user passwords
async def analyze_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_password = update.message.text
    result = zxcvbn(user_password)
    score = result['score']  # 0-4
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']

    # Suggested stronger password if weak
    suggested_password = generate_strong_password() if score < 3 else user_password

    # Pick a futuristic tip
    tip = random.choice(futuristic_tips)

    # Build response
    response = (
        f"⚡ Password Analysis Report ⚡\n\n"
        f"Password: `{user_password}`\n"
        f"Strength Score: {score}/4\n"
        f"Estimated crack time: {crack_time}\n"
        f"Suggested upgrade: `{suggested_password}`\n\n"
        f"{tip}"
    )

    await update.message.reply_text(response, parse_mode="Markdown")

# Main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("generate", generate))

    # Password messages
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), analyze_password))

    print("🚀 PassFortisBot is online and guarding passwords!")
    app.run_polling()
