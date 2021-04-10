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

class info(commands.Cog, name="Info"):
    def __init__(self, bot):
        self.bot = bot

    #BOT Info

    @commands.command(description="Shows you the information about a bot.")
    async def bi(self, ctx):
        embed = discord.Embed(
            title="<:ElementLogo:802919295755223060> Element BOT Info",
            description="Prefix is --",
            color=0x134F5C
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        fields = [("Bot Latency",f"{round(self.bot.latency* 1000)}ms",True),
        ("Created By","RSGameTech#9977",True),
        ("Bot Version","V0.4 (Beta)",True),
        ("Language Using","Python",True),
        ("Total Server Joined","....",True),
        ("Total User Useing","....",True)]
        for name, value, inline in fields:
            embed.add_field(name=name,value=value,inline=inline)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Server Info

    @commands.command(description="Shows you the information about the current server.")
    async def si(self, ctx):
        embed = discord.Embed(title="Server Info",color=ctx.guild.owner.colour)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        fields = [("Owner",ctx.guild.owner,True),
        ("Total Member",ctx.guild.member_count,True),
        ("Region",str(ctx.guild.region).capitalize(),True),
        ("Created At",ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"),True)]
        for name, value, inline in fields:
            embed.add_field(name=name,value=value,inline=inline)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #User Info

    @commands.command(description="Shows you the information of a user in current server")
    async def ui(self, ctx , *,user: discord.Member = None):
        if user is None:
            user = ctx.author
        embed = discord.Embed(
            title="User Information",
            color=0x134F5C
        )
        embed.set_thumbnail(url=user.avatar_url)
        fields = [("Name",str(user.name),True),
        ("ID",user.id,True),
        ("Status",str(user.status).capitalize(),True),
        ("Created At",user.created_at.strftime("%d/%m/%Y %H:%M:%S"),True),
        ("Joined At",user.joined_at.strftime("%d/%m/%Y %H:%M:%S"),True)]
        for name, value, inline in fields:
            embed.add_field(name=name,value=value,inline=inline)
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(info(bot))
    print("Info file is loaded!")
