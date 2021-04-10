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
import asyncio
import typing
from discord.ext import commands

wr = "Warning"
filtered_words = ["Fuck"]

class auto_mod(commands.Cog, name="Moderation"):
    def __init__(self, bot):
        self.bot = bot

    #Anti Server Invite

    @commands.Cog.listener()
    async def on_message(self, message):
        if "discord.gg/" in message.content:
            await message.delete()
            IW = discord.Embed(
                title=wr,
                description=f"{message.author.mention}, Stop posting Invite Links in this server :triumph:",
                color=0xFF0000
            )
            await message.channel.send(embed=IW)
        elif "youtu.be/" in message.content or "youtube.com/" in message.content:
            await message.delete()
            SPW = discord.Embed(
                title=wr,
                description=f"{message.author.mention}, Stop doing self-promotion in this server :triumph:",
                color=0xFF0000
            )
            await message.channel.send(embed=SPW) 
        for word in filtered_words:
            if word in message.content:
                await message.delete()

def setup(bot):
    bot.add_cog(auto_mod(bot))
    print("Auto Moderation file is loaded!")
