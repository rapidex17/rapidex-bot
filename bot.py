from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "COLE_AQUI_SEU_TOKEN_NOVO"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bem-vindo ao Rapidex!\n\n"
        "🛵 Motoristas digitem /sou_motorista\n"
        "👤 Passageiros não precisam se cadastrar."
    )

async def sou_motorista(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛵 Cadastro de Motorista Rapidex\n\n"
        "Digite seu nome completo:",
        parse_mode="Markdown"
    )
    context.user_data["etapa"] = "nome"

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sou_motorista", sou_motorista))

app.run_polling()

