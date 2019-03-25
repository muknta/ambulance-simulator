import telebot



class Bot:
    bot = telebot.TeleBot('709037271:AAFPMYU-Jxbc4DOMDBkdl6PR5V_G8GbNFcQ')
    updates = bot.get_updates()
    def __call__(self, bot=bot):
        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            bot.reply_to(message, '''Виртуальная служба скорой помощи города Зеон. Обращайтесь только в случае крайней необходимоси.
              \nНаш бот запишет Ваше обращение и пошлет к Вам скорую помощь.
              \n       Для продолжения нажмите /continue''')

        @bot.message_handler(commands=['continue'])
        def sypthoms(message):
            bot.send_message(message.chat.id, 'Опишите симпотмы:')
        bot.polling()


bot = Bot().__call__()

