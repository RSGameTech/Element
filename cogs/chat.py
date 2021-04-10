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
import random
from discord.ext import commands


class Chat(commands.Cog, name="Extras"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Chat file is loaded")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "dead chat":
            await message.channel.send(f"{message.author.name}, if it is dead chat then why are you chatting here!")
        if "<@699566190842085439>" in message.content:
            r = [":expressionless:",":rolling_eyes:",":weary:",":scream:",":triumph:",":dizzy_face:"]
            await message.channel.send(random.choice(r))

def setup(bot):
    bot.add_cog(Chat(bot))

#        if message.content == "??":
#            await message.channel.send(f"{message.author.name} didn't understand what you told!")
#        elif message.content == "idk":
#            await message.channel.send(f"{message.author.name} don't know what you asked!'")
#        elif message.content == "hi":
#            await message.channel.send(f"Hi {message.author.name}, welcome to the chat!")
