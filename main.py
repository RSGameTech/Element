import discord
import requests
import sys
import os
import traceback
import json
import discoutils
import jishaku
from discord.ext import commands, tasks
from itertools import cycle
from discoutils import MinimalEmbedHelp

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="--", intents=intents, help_command=MinimalEmbedHelp())
#bot.remove_command('help')
status = cycle([discord.Game(name="Discord"),discord.Activity(type=discord.ActivityType.listening, name="RSGameTech"),discord.Activity(type=discord.ActivityType.watching, name="Youtube")])

@bot.event
async def on_ready():
    change_status.start()
    channel = bot.get_channel(823836100882989108)
    embed = discord.Embed(
        description = f"I am Online :sunglasses:\nPing:- {round(bot.latency * 1000)}ms",
        color = 0x00CCFF
    )
    await channel.send(embed=embed)
    print("Bot is online")

@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=next(status))

bot.owner_ids=[699566190842085439, 730454267533459568]

extentions = [
    'cogs.moderation',
    'cogs.auto_mod',
    'cogs.animation',
    'cogs.fun',
    'cogs.event',
    'cogs.info',
    'cogs.utility',
    'cogs.api',
    'cogs.chat'
]
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Excepton as e:
            print(f"Error loading {extension}", file=sys.stderr)
            traceback.print_exc()

bot.load_extension("jishaku")
bot.run('NzkwODMyMjYzMjYwMDEyNTcz.X-GV8A.vRC6Mw1J3hD6p3ZyaP3bkSULc6g')
