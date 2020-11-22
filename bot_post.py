import threading
import telebot
from flask import Flask, request
import requests
import json
import base64
# testbot14112020bot - bot ID
url = "https://maksim:solovjov@staging.gamelix.com/external/telegram/user-subscribed"
headers = {'Content-type': 'application/json'}

bot = telebot.TeleBot('1479132700:AAEv8_x29xWWd_5m0SXnVeL3I0yVmZuEZ3I')



def extractIdAndDecode(text):
	userId = text.split()[1] if len(text.split()) > 1 else None
	userId = userId.encode("UTF-8")
	userId = base64.b64decode(userId)
	userId = userId.decode("UTF-8")
	return userId



app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
	userId = extractIdAndDecode(message.text)
	if userId:
		data = {"userId": userId, "chatId": message.chat.id}
		answer = requests.post(url, data=json.dumps(data), headers=headers)

		




@app.route('/', methods=['POST'])
def result():
	dt = request.args.to_dict(flat=False)
	for i in dt["chatIds"]:
		bot.send_message(i, dt["message"])

	return "0"

t = threading.Thread(target=bot.polling, daemon=True)
t.start()  # start the bot in a thread instead

