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
from discord.ext import commands
from discord.utils import get


class event(commands.Cog, name="Events"):
    def __init__(self, bot):
        self.bot = bot

    #member Join

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.role, name="Verified")
        channel = self.bot.get_channel(772856544193675285)
        embed = discord.Embed(title="Good News",
                            description=f"{member.mention} just joined the Server, Welcome him by chatting(Not in DM)",color=discord.Color.blue()
                            )
        await member.add_role(role)
        await channel.send(embed=embed)

    #Member Leave

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel = self.bot.get_channel(772856544193675285)
        embed = discord.Embed(
            title="Sad News",
            description=f"{member.name} just left the Server. Everyone is sad now",
            color=0xFF0000
        )
        await channel.send(embed=embed)

    #Join Voice Channel

    @commands.command()
    @commands.is_owner()
    async def join(self, ctx, *, channel:discord.VoiceChannel):
        await channel.connect()

    #Leave Voice Channel

    @commands.command()
    @commands.is_owner()
    async def leave(self, ctx, *, channel:discord.VoiceChannel):
        await channel.disconnect()

def setup(bot):
    bot.add_cog(event(bot))
    print("Event file is loaded!")
