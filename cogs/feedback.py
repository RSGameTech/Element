import discord
from discord.ext import commands

er = "Error"
nt = "[ ] -> Required\n( ) -> Optional"

class feedback(commands.Cog, name="Feedback"):
    def __init__(self, bot):
        self.bot = bot

    #Suggestion

    @commands.command()
    async def suggest(self, ctx, mode = None, *, args):
        if mode == "bot":
            bot_suggest = self.bot.get_channel(830830456915623946)
            bs = discord.Embed(
                title="BOT Suggestion",
                description=args,
                color=0x00CCFF
            )
            bs.set_footer(text=f"Suggestion sended by {ctx.author.name}",icon_url=ctx.author.avatar_url)
            await bot_suggest.send(embed=bs)
            await ctx.reply("Your BOT Suggestion has been sended successfully")
        elif mode == "server":
            server_suggest = self.bot.get_channel(830840766737678346)
            ss = discord.Embed(
                title="Server Suggestion",
                description=args,
                color=0x00CCFF
            )
            ss.set_footer(text=f"Suggestion sended by {ctx.author.name}",icon_url=ctx.author.avatar_url)
            await server_suggest.send(embed=ss)
            await ctx.reply("Your Server Suggestion has been sended succussfully")
        else:
            me = discord.Embed(
                title=er,
                color=0xFF0000
            )
            fields=[("Ussage","l!suggest [mode] [Your suggestion]",True),
            ("Note:-",nt,True),
            ("Mode:-","`bot` -> For BOT Suggestion\n`server` -> For Server Suggestion",True)]
            for name, value, inline in fields:
                me.add_field(name=name,value=value,inline=inline)
            await ctx.send(embed=me)

def setup(bot):
    bot.add_cog(feedback(bot))
    print("Feedback file is loaded!")
