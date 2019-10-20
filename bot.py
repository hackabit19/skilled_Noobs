import json, os, subsystem
import httplib2,pprint
import sys, re
import zulip

from lyrics import Lyrics
from cricket import Cricket
from currency import Currency
from translate import Translate
from movie import Movie

from holiday import Holiday


p = pprint.PrettyPrinter()
BOT_MAIL = "noob-bot@zulipchat.com"

class ZulipBot(object):
	def __init__(self):
		self.client = zulip.Client(site="https://noobbot.zulipchat.com/api/")
		self.subscribe_all()
		self.lyrics = Lyrics()
		self.cricket = Cricket()
		self.currency = Currency()
		self.trans = Translate()
		self.movie= Movie()
		self.holiday = Holiday()
						
		print("done init")
		self.subkeys = ["askme", "lyrics", "cricnews", "currency","translate", "movie", "holiday"]

	def subscribe_all(self):
		json = self.client.get_streams()["streams"]
		streams = [{"name": stream["name"]} for stream in json]
		self.client.add_subscriptions(streams)

	def process(self, msg):
		content = msg["content"].split()
		sender_email = msg["sender_email"]
		ttype = msg["type"]
		stream_name = msg['display_recipient']
		stream_topic = msg['subject']

		print(content)

		if sender_email == BOT_MAIL:
			return 

		print("Sucessfully heard.")

		if content[0].lower() == "noob" or content[0] == "@**noob**":
			if content[1].lower() == "translate":
				ip = content[2:]
				ip = " ".join(ip)
				message = self.trans.translate(ip)
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})

			if content[1] not in self.subkeys:
				ip = content[1:]
				ip = " ".join(ip)
				message = self.chatbot.get_response(ip).text
				self.client.send_message({
					"type": "stream",
					"subject": msg["subject"],
					"to": msg["display_recipient"],
					"content": message
					})

		
		elif "noob" in content and content[0] != "noob":
			self.client.send_message({
				"type": "stream",
				"subject": msg["subject"],
				"to": msg["display_recipient"],
				"content": "Hey there! :blush:"
				})
		else:
			return

def main():
	bot = ZulipBot()
	bot.client.call_on_each_message(bot.process)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Thanks for using noob Bot. Bye!")
		sys.exit(0)
