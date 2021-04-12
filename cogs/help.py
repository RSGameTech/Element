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
