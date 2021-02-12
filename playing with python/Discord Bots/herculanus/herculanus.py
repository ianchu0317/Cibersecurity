#!/usr/bin/env python3

#Import discord module
import discord
from discord.ext import commands    #Import extensions
from time import sleep              #Import sleep module to stay organized
import bot_finght

bot = commands.Bot(command_prefix="$")      #Create the bot


@bot.event
async def on_ready():
    print("HERCULANUS is ready")

@bot.event
async def on_message(message):
    user = str(message.author.mention)
    h = str(bot.user)
    if message.author == bot.user:
        pass
    else:
        msg = bot_finght.choice_response()
        await message.channel.send(f"{user} {msg}")
'''
@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

@bot.command()
async def pong(ctx):
    await ctx.channel.send("ping you bitch")

@bot.command()
async def conversation(ctx):
    await ctx.channel.send()
'''

if __name__ == "__main__":
    bot.run("ODA3MjQ3ODMyMTkyMjUzOTg1.YB1OIQ.JbRW1McZ9aiuG48w0WfvjC5ulFQ")