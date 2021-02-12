#!/usr/bin/env python3

#Import modules to use
import discord
from time import sleep
import random_comment

pancracius = discord.Client()		#Create the bot

'''
def comments_counter(comment):
	if comments in already_done_comments:
		return True
	else:
		already_done_comments.append(comment)
'''

@pancracius.event
async def on_ready():
	print("PANCRACIUS is ready")

@pancracius.event
async def on_message(message):
	if message.author == pancracius.user:
		pass					#If the bot send a message, it will skip
	else:
		user = str(message.author.mention)	#Get user id to tag into the next message
		m = random_comment.choice_response()
		await message.channel.send(f"{user} {m}")



if __name__ == "__main__":
	already_done_comment = []
	pancracius.run("ODA4MTIwNTA4NTY1NTUzMTUy.YCB63w.SahAjnEB7gQhjlMofwLhiKwDaHg")
	
