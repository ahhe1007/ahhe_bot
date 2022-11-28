import discord
from discord.ext import commands

bot = commands.bot(command_prefix= '!')

@bot.event
async def on_ready():
    print(">> Bot is online ")

bot.run('MTA0NjYzMTk1OTA2NzExOTc2OA.GhPzTo.lGxXt3d6LyquCe1c2N_XH6Qps9POSR2NGdwIts')