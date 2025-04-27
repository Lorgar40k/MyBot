from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = 

TEXTS = {
    "skills": "Навыки:\n- Ручное тестирование (Web, Mobile)\n- Тест-дизайн\n- API тестирование\n- SQL, HTML, CSS (базово)\n- DevTools, Jira, Miro\n- Scrum, Kanban",
    "experience": "Опыт:\n- Junior QA Engineer (учебные проекты)\n- Медицинский работник: анализ данных, стандартизация процессов",
    "education": "Образование:\n- Омский Медицинский Колледж\n- Институт международных экономических связей (неоконченное)\n- QA Studio, SkillBox (доп. образование)",
    "contacts": "Контакты:\n📞 +7 (913) 961-8780\n✉ warhale40x@gmail.com\nGitHub: https://github.com/Lorgar40k"
}

keyboard = [
    ["Навыки", "Опыт"],
    ["Образование", "Контакты"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я крутецкий айтишный бот Алексея Григорьевича.\n\nВыберите, что вас интересует:",
        reply_markup=reply_markup
    )

# Функция для обработки текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()

    if "навык" in text:
        await update.message.reply_text(TEXTS["skills"])
    elif "опыт" in text:
        await update.message.reply_text(TEXTS["experience"])
    elif "образование" in text:
        await update.message.reply_text(TEXTS["education"])
    elif "контакт" in text:
        await update.message.reply_text(TEXTS["contacts"])
    else:
        await update.message.reply_text(
            "Извини, я тебя не понял.\nПожалуйста, выбери кнопку или напиши ключевое слово."
        )

# Основная функция для запуска бота
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))  # Обработчик команды /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Обработчик сообщений

    app.run_polling()

if __name__ == '__main__':
    main()
