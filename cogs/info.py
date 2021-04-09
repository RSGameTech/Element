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
