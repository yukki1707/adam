import telebot
import config

bot = telebot.TeleBot()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'That a test')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print (message.sticker.file_id)

@bot.message_handler(content_types=['text'])
def chatting(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello, Creator!')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Good bye, Creator!')
    elif message.text.lower() == 'send a sticker':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAIBS17ZX1x3eg-Y0Lb66F1nYJGy3O43AAKdAQAC3kD4Bw2V1XgkjhzgGgQ')


bot.polling()