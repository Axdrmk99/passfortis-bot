# main.py
import random
from zxcvbn import zxcvbn
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ⚠ Replace with env variable in production
BOT_TOKEN = "8254696772:AAFEepz6onei2yLu8hcigR7rZ2T0hoOM010"

# Small futuristic flavor line
futuristic_lines = [
    "⚡ Cyber AI suggests staying vigilant!",
    "💾 Matrix scan complete. Security enhanced!",
    "🛡️ Hacker intrusion probability minimal.",
    "🔐 Firewall integrity verified."
]

# Strengthen user password (keep recognizable)
def strengthen_password(pw):
    substitutions = {"a":"@","A":"@","i":"1","I":"1","s":"$","S":"$","o":"0","O":"0","e":"3","E":"3"}
    pw_strong = "".join(substitutions.get(c, c) for c in pw)
    pw_strong = "".join(c.upper() if random.random() < 0.3 else c for c in pw_strong)
    # Add 1-2 symbols at the end
    symbols = "!@#$%^&*()_+1234567890"
    pw_strong += "".join(random.choice(symbols) for _ in range(2))
    return pw_strong

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👾 Welcome to PassFortisBot – your password guardian.\n"
        "Send any password and I'll analyze it, show crack time, and suggest a stronger version keeping it recognizable.\n"
        "Type /help to see commands."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Commands:\n"
        "/start - Introduction\n"
        "/help - Show this message\n"
        "/generate - Generate a strong password from your words\n\n"
        "Or send a password and I'll analyze it!"
    )

# /generate command
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ Please send me some words (like your name or favorite thing) and I'll generate a strong password based on them!"
    )

    # Wait for the next message as the user input
    def check(msg):
        return True

    # Handler to catch next message for generating password
    async def generate_from_words(update2: Update, context2: ContextTypes.DEFAULT_TYPE):
        words = update2.message.text
        # Strengthen the words into a password
        password = strengthen_password(words)
        flavor = random.choice(futuristic_lines)
        await update2.message.reply_text(f"⚡ Generated strong password: `{password}`\n{flavor}", parse_mode="Markdown")
        # Remove this handler after running once
        context.bot.remove_handler(handler)

    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), generate_from_words)
    context.bot.add_handler(handler)

# Analyze user passwords
async def analyze_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pw = update.message.text
    result = zxcvbn(pw)
    score = result['score']
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']

    suggested_pw = strengthen_password(pw) if score < 4 else pw
    flavor = random.choice(futuristic_lines)

    response = (
        f"⚡ PassFortis Scan Report ⚡\n\n"
        f"💠 Password analyzed: `{pw}`\n"
        f"📊 Strength Score: {score}/4\n"
        f"⏱️ Estimated Crack Time: {crack_time}\n"
        f"🔑 Suggested Upgrade: `{suggested_pw}`\n\n"
        f"{flavor}"
    )

    await update.message.reply_text(response, parse_mode="Markdown")

# Main bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("generate", generate))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), analyze_password))
    print("🚀 PassFortisBot is online and guarding passwords!")
    app.run_polling()
