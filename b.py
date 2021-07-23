import abc
import asyncio
import os
from discord import channel, guild, message
import discord
from discord.channel import TextChannel 

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Le bot est prêt")

@bot.command(name='DelCup')
async def on_message(ctx):
     await ctx.message.delete()
     await asyncio.sleep(10)
     await ctx.channel.delete()


@bot.command(name='del')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_messages in messages:
        await each_messages.delete()



bot.run(os.getenv("TOKEN"))