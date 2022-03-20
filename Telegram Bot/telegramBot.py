import config
import telebot as tb

bot=tb.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])

def lalalal(message):
	bot.send_message(message.chat.id,message.text)

bot.polling(none_stop=True)