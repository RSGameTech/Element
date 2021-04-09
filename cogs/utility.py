import discord
import asyncio
from discord.ext import commands

class util(commands.Cog, name="Utility"):
    def __init__(self,bot):
        self.bot = bot

    #User Avatar

    @commands.command()
    async def user_av(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.message.author
        embed = discord.Embed()
        embed.add_field(name=user.name,value=f"[Download]({user.avatar_url})")
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Server Avatar

    @commands.command()
    async def server_av(self, ctx):
        embed = discord.Embed()
        embed.add_field(name=ctx.guild.name,value=f"[Download]({ctx.guild.icon_url})")
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Reverse

    @commands.command()
    async def reverse(self, ctx, *, args):
        r = args[::-1]
        embed = discord.Embed(description=f"The message is\n`{r}`")
        await ctx.send(embed=embed)

    #Ping

    @commands.command()
    async def ping(self, ctx):
        msg = await ctx.send("Pinging <a:WindowsDotLoading:809471466311516211>")
        await asyncio.sleep(5)
        embed = discord.Embed(
            title="Pong!",
            description=f"Your latency is {round(self.bot.latency * 1000)}ms",
            color=0x00CCFF
        )
        await msg.edit(content = "",embed=embed)

def setup(bot):
    bot.add_cog(util(bot))
    print("Utility file is loaded!")
