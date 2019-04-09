from telebot import TeleBot, types
from app.op.сonfig import *


class Request(object):
    def __init__(self, phone_number:str, adress: str):
        self.phone_number = phone_number
        self.adress = adress


class Process(Request):
    def __init__(self, status:bool, danger:float, phone_number, adress):
        super().__init__(phone_number=phone_number, adress=adress)
        #Request.__init__(self, phone_number=Request.phone_number, adress=Request.adress)
        self.status = status
        self.danger = danger


class Ambulance_db(object):
    pass


class Bot:
    __bot__ = TeleBot(Config.TOKEN)
    __updates__ = __bot__.get_updates()

    def __call__(self, bot = __bot__):
        @bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            bot.reply_to(message, '''Virtual emergency service of the city of Zeon. Handle only when absolutely necessary.
               \nOur bot will record your message and send you an ambulance.
               \nTo continue, click  /continue''')

        @bot.message_handler(commands=['continue'])
        def __data__(message):

            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            button_phone = types.KeyboardButton(text='Send phone number', request_contact=True)
            keyboard.row(button_phone)
            bot.send_message(message.chat.id, "Please, enter all data about you and follow the next instructions.", reply_markup=keyboard)

            @bot.message_handler(content_types=["contact"])
            def __read_contact_data__(message):
                bot.send_message(message.chat.id, "Got it! Your number is "+ str(message.contact.phone_number + ' Please, follow the next instructions.'), reply_markup=types.ReplyKeyboardRemove())
                phone_number = message.contact.phone_number
                '''
                Other buttons to get sympthoms after this
                One inline button to get adress
                GetRequest().__call__() ------- get request and save request to db including class DB in future 
                '''
                return phone_number

        bot.polling(none_stop=True)

    class GetRequest:
        pass



