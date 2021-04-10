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
        if "youtu.be/" in message.content or "youtube.com/" in message.content:
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
