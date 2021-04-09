import discord
from discord.ext import commands

class source(commands.Cog, name="Utility"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def source(self, ctx):
        embed = discord.Embed(
            title="This BOT is open source",
            description=f"[Click here](https://ritam0604.github.io/Element/)"
        )
        embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(source(bot))
    print("Source file is loaded!")