from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/Varshika/Downloads/chatterbot-corpus-1.1.2/chatterbot-corpus-1.1.2/chatterbot_corpus/data/english/'):
	 data = open('C:/Users/Varshika/Downloads/chatterbot-corpus-1.1.2/chatterbot-corpus-1.1.2/chatterbot_corpus/data/english/' + files , 'r').readlines()
	 bot.train(data)

while True:
	message = input('You: ')
	if message.strip() != 'bye':
		reply = bot.get_response(message)
		print('ChatBot: ',reply)
	if message.strip() == 'bye':
		print('ChatBot: Bye')
		break