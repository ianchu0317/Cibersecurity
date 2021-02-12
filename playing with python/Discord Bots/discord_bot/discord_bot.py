import discord
from discord.ext import commands
import AI
import search_image
import menu_help
import random_comment

anashex = commands.Bot(command_prefix="!")


@anashex.event
async def on_ready():
	print("ANASHEX is ready")


@anashex.event   #Ready_advice function
async def on_message(message):
	user = str(message.author.mention)
	msg = str(message.content)
	print(f"{user}: {msg}")
	#Hello Function
	if message.content=="!hello":
		await message.channel.send("Hello my friend")

	#Spam Function
	elif msg.startswith("!sp --spam"):
		spam_mode = str(message.content).strip("!sp --spam")
		print(spam_mode)
		if "-i" in spam_mode:
			spam_list = spam_mode.split("-i")
			spam_word = spam_list[0]
			spam_time = spam_list[1]
			if " " in spam_time:
				spam_time = spam_time.replace(" ", "")
				try:
					spam_time = int(spam_time)
					for i in range(spam_time):
						await message.channel.send(str(spam_word))
						if "!stop" in str(message.content):
							await message.channel.send("[+] The spam attack has succefully stopped :) XD ")
							break
				except ValueError:
					await message.channel.send("[+] The passed parameter of itineration is invalid")
		else:
			await message.channel.send("syntax (!sp --spam <word> -i <itineration>) ")

	#AI Function
	elif msg.startswith("!sp --AI"):
		command = msg.strip("!sp --AI ")
		response = discord_AI.check_msg(command)
		await message.channel.send(response)
		pass

	#Pass image Function
	elif msg.startswith("!sp --image "):
		request = str(message.content).strip("!sp --image")
		image = image_search.search_image(request)
		embed.set_image(url=image)
		await message.channel.send(embed=embed)


	#Help menu function
	elif msg.startswith("!sp help"):
		if "image" in msg:
			await message.channel.send(menu_help.image_help)
		elif "spam" in msg:
			await message.channel.send(menu_help.spam_help)
		elif "AI" in msg:
			await message.channel.send(menu_help.ai_help)
		else:
			await message.channel.send(menu_help.help)

	#join voice channel function
	elif msg.startswith("!sp --play"):

		await message.channel.send("This option is not available yet")

		pass
	elif message.author.mention == "<@808120508565553152>":
		m = random_comment.choice_response()
		await message.channel.send(f"{user} {m}")
	#Random comment function
	else:
		if "Gaby gay" in msg and message.author != anashex.user:
			await message.channel.send("Gaby gay")
'''
	else:
		response = random_comment.Random()
		response.check_(str(message.content))
		await message.channel.send(response)
'''



if __name__ == "__main__":
	discord_AI = AI.AI()														#import AI Function
	embed = discord.Embed()														#Embed object from discord module
	image_search = search_image.Search()										#Import the search image module and asign the class
	voice_channels = anashex.get_all_channels()

	anashex.run('Nzg0ODYyOTkxODI4Nzc5MDk5.X8venw.GvRrxZuCkK6KYNXX42IenkR3gPY')
