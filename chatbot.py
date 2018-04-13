from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

while True:
	message = input('You: ')
	if message.strip() != 'bye':
		reply = bot.get_response(message)
		print('ChatBot: ',reply)
	if message.strip() == 'bye':
		print('ChatBot: Bye')
		break