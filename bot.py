import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/AnimatedSticker.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keybord
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🐍 Get random number !")
	item2 = types.KeyboardButton("😀 How are you?")

	markup.add(item1,item2)

	bot.send_message(message.chat.id, "welcome, {0.first_name}!\nI'm - <b>{1.first_name}</b>,a bot created to help you.".format(message.from_user, bot.get_me()),
	parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def lalala(message):
	#bot.send_message(message.chat.id,message.text)
	if message.chat.type == 'private':
		if message.text == '🐍 Get random number !':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
			
		elif message.text == '😀 How are you?':
			markup=types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Good", callback_data ='good')
			item2 = types.InlineKeyboardButton("Not good", callback_data ='bad')
			markup.add(item1, item2)
			bot.send_message(message.chat.id, '🥳 I am good,what about you',reply_markup=markup)	
		else:
			bot.send_message(message.chat.id, '🤬 I dont know what the fuck to do')	


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	try:
		if call.message:
			if call.data =='good':
				bot.send_message(call.message.chat.id, '🤗 its okay')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, '😱sometimes happens')

			#remove inline buttons
			bot.edit_message_text(chat_id =call.message.chat.id, message_id=call.message.message_id, text="🥳 I am good,what about you?",
             	reply_markup=None)


            
            #show alert
			bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text="Test note!!!")
	

	except Exception as e:
		print(repr(e))				

bot.polling(none_stop=True)

	