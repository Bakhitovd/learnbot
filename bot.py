from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import setting



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot,update):
    text='Привет! я супер бот. Кто ты?'
    logging.info(text)
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot,update):
    answer_to_user='Привет {}. Ты написал: {}'.format(update.message.chat.first_name,update.message.text)
    user_text=update.message.text
    
    logging.info("User: %s, Chat: %s, message: %s", update.message.chat.first_name,
                update.message.chat.id,update.message.text)

    update.message.reply_text(answer_to_user)
    


def main():
    mybot = Updater(setting.API, request_kwargs=setting.PROXY)
    logging.info("Бот запустился")
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()