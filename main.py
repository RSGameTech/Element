'''
MIT License

Copyright (c) 2021 RSGameTech

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

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
from keep_alive import keep_alive

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

extensions = [
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
        except Exception as e:
            print(f"Error loading {extension}", file=sys.stderr)
            traceback.print_exc()

keep_alive()
bot.load_extension('jishaku')
bot.run(os.getenv('Token'))
