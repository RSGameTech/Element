import discord
from discord.ext import commands

class help(commands.Cog, name="Help"):
	def __init__(self,bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		user = ctx.message.author
		embed = discord.Embed(color=0x00FF00)
		embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
		embed.add_field(name="Full BOT Guide", value=f"[Help](https://rsgametech.gitbook.io/element/)", inline=False)
		embed.add_field(name="BOT Info", value=f"[Invite](https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot)", inline=False)
		try:
			await user.send(embed=embed)
			await ctx.send(f"{user}, you recieved a Mail :mailbox_with_mail: in your DM")
		except:
			await ctx.send("Please unlock your DM to recieve the help message")

def setup(bot):
	bot.add_cog(help(bot))
	print("help file is loaded!")
