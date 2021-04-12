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

sn = "Server News"
er = "Error"

class moderation(commands.Cog, name="Moderation"):
    def __init__(self, bot):
        self.bot = bot

    #Kick

    @commands.command(brief="This command is used to kick the members from the current server.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title=sn,
            description=f"{member.name} has successfully kicked for {reason}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            KE1 = discord.Embed(
                title=er,
                description="Please mention the name that you want to `Kick`",
                color=0xFF0000
            )
            await ctx.send(embed=KE1)
        elif isinstance(error, commands.MemberNotFound):
            KE2 = discord.Embed(
                title=er,
                description="Member not found in this server",
                color=0xFF0000
            )
            await ctx.send(embed=KE2)
        elif isinstance(error, commands.MissingPermissions):
            KE3 = discord.Embed(
                title=er,
                description=f"{ctx.author.mention}, you don't have the Kick Member permission!",
                color=0xFF0000
            )
            await ctx.send(embed=KE3)

    #Ban

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title=sn,
            description=f"{member.name} has successfully banned for {reason}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            BE1 = discord.Embed(
                title=er,
                description="Please mention the name that you want to `Ban`",
                color=0xFF0000
            )
            await ctx.send(embed=BE1)
        elif isinstance(error, commands.MemberNotFound):
            BE2 = discord.Embed(
                title=er,
                description=f"Member not found in this server",
                color=0xFF0000
            )
            await ctx.send(embed=BE2)
        elif isinstance(error, commands.MissingPermissions):
            BE3 = discord.Embed(
                title=er,
                description=f"{ctx.author.mention}, you don't have `Ban Member` permission!",
                color=0xFF0000
            )
            await ctx.send(embed=BE3)

    #Clear

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        embed = discord.Embed(
            title=sn,
            description="Message has been succesfully clear",
            color=0x00FF00
        )
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(embed=embed)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            CE1 = discord.Embed(
                title=er,
                description=f"{ctx.author.mention}, you have to  specify the amount of message to delete.",
                color=0xFF0000
            )
            await ctx.send(embed=CE1)
        elif isinstance(error, commands.MissingPermissions):
            CE2 = discord.Embed(
                title=er,
                description=f"{ctx.author.mention}, you don't have the 'Manage Message' permision to use this command.",
                color=0xFF0000
            )
            await ctx.send(embed=CE2)

    #Mute

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        muted_role = ctx.guild.get_role(829564091864842280)
        await member.add_role(muted_role)
        embed = discord.Embed(
            title=sn,
            description=f"{member.author.mention} has been muted for:-\n{reason}",
            color=0x00FF00
        )
        await ctx.send(embed=embed)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            ME1 = discord.Embed(
                title=er,
                description="Please mention the name that you want to `Mute`",
                color=0xFF0000
            )
            await ctx.send(embed=ME1)
        elif isinstance(error, commands.MemberNotFound):
            ME2 = discord.Embed(
                title=er,
                description=f"Member not found in this server",
                color=0xFF0000
            )
            await ctx.send(embed=ME2)


    #Unmute

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def unmute(self, ctx, member: discord.Member):
        muted_role = ctx.guild.get_role(829564091864842280)
        await member.remove_role(muted_role)
        embed = discord.Embed(
            title=sn,
            description=f"{member.author.mention} has been unmuted.",
            color=0x00FF00
        )
        await ctx.send(embed=embed)

    #Embed

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx, title: str = None,*, description: str = None):
        embed = discord.Embed(
            title=f"{title}",
            description=f"{description}",
            color=0x00CCFF
        )
        await ctx.send(embed=embed)

    @embed.error
    async def embed_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            EE1 = discord.Embed(
                title=er,
                description=f"{ctx.author.mention}, you don't have the 'Manage Message' permision to use this command.",
                color=0xFF0000
            )
            await ctx.send(embed=EE1)

def setup(bot):
    bot.add_cog(moderation(bot))
    print("Moderation file is loaded!")
