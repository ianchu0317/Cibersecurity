import discord
from discord.ext import commands
import AI
import search_image
import random_comment

anashex = commands.Bot(command_prefix="!sp ")
help = """
___COMMANDS___

--spam 		(--spam <message> <Time>)
--AI   		(--AI <message>)
--image 	(--image <message>)
--help (print out this help command manual) 

___EXAMPLE SYNTAX___
!sp <mode> <option>

___SPECIFIC HELP___
!sp help <mode>
Ex: !sp help spam

 """
image_help = """
___SYNTAX___
!sp --image <command>

___AVAILABLE COMMANDS OPTIONS___
- Naruto
- Dog
- Cat 
- Random 
"""

spam_help = """
___SYNTAX___
!sp --spam <message> -i <number>
"""

ai_help = '''
___SYNTAX___
!sp --AI <message>
'''

@anashex.event
async def on_ready():
	print("Bot is ready")

@anashex.event
async def on_message(message):
	print(message.content)
	msg = str(message.content)
	if message.content=="!hello":
		await message.channel.send("Hello my friend")
	
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

	elif msg.startswith("!sp --AI"):
		command = msg.strip("!sp --AI ")
		response = discord_AI.check_msg(command)
		await message.channel.send(response)
		pass

	elif msg.startswith("!sp --image "):
		request = str(message.content).strip("!sp --image")
		print(f'Request is: {request}')
		image = image_search.search_image(request)
		embed.set_image(url=image)
		await message.channel.send(embed=embed)

	elif msg.startswith("!sp help"):
		if "image" in msg:
			await message.channel.send(image_help)
		elif "spam" in msg:
			await message.channel.send(spam_help)
		elif "AI" in msg:
			await message.channel.send(ai_help)
		else:
			await message.channel.send(help)
'''
	else:
		response = random_comment.Random()
		response.check_(str(message.content))
		await message.channel.send(response)
'''


if __name__ == "__main__":
	discord_AI = AI.AI()														#import AI Function
	embed = discord.Embed()														#Embed object from discord module
	image_search = search_image.Search()										#Import the search image module
	anashex.run('Nzg0ODYyOTkxODI4Nzc5MDk5.X8venw.0NCy2ayWKGJhsoVVOvx4HTEbGOc')