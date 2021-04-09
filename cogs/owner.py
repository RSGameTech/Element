import discord
from discord.ext import commands

class owner(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

    #Reload

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self,ctx,name:str):
        try:
            self.bot.reload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(ethrow.traceback_throw(e))
        await ctx.send(f"✅ | Reloaded extension `{name}`")

def setup(bot):
    bot.add_cog(owner(bot))
    print("owner file is loaded!")
