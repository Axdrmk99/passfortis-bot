from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from zxcvbn import zxcvbn
import secrets
import string

BOT_TOKEN = "8254696772:AAFEepz6onei2yLu8hcigR7rZ2T0hoOM010"

def generate_strong_password(base):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+="
    extra_length = max(14 - len(base), 6)
    extra = ''.join(secrets.choice(chars) for _ in range(extra_length))
    return base + extra

async def handle_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pwd = update.message.text.strip()

    result = zxcvbn(pwd)
    score = result["score"]

    crack_slow = result["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
    feedback = result["feedback"]

    levels = ["Very Weak", "Weak", "Okay", "Strong", "Very Strong"]

    message = (
        "🔐 **PassFortis Security Report**\n\n"
        f"**Strength:** {levels[score]} ({score}/4)\n"
        f"**Estimated crack time:** {crack_slow}\n"
        "_(Assuming secure password hashing)_\n\n"
    )

    if feedback["warning"]:
        message += f"⚠️ {feedback['warning']}\n"

    if feedback["suggestions"]:
        for tip in feedback["suggestions"]:
            message += f"• {tip}\n"

    if score < 4:
        stronger = generate_strong_password(pwd)
        message += (
            "\n🔧 **Improved version:**\n"
            f"`{stronger}`\n"
        )

    message += "\n🛡️ _Passwords are analyzed in memory and never stored._"

    await update.message.reply_text(message, parse_mode="Markdown")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_password))
app.run_polling()
