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
import requests
import random
import json
from discord.ext import commands

er = "Error"
nt = "Note:-"
nd = "[ ] -> Required\n( ) -> Optional"

class api(commands.Cog, name="API"):
    def __init__(self, bot):
        self.bot = bot
    


    #Wasted

    @commands.command()
    async def wasted(self, ctx, *, user: discord.Member = None):
        if user is None:
            E1 = discord.Embed(
                title=er,
                description="Please mention the name that you want to `Wasted`",
                colour=0xFF0000
            )
            E1.add_field(name="Usage", value="--wasted [member]")
            E1.add_field(name=nt, value=nd)
            await ctx.send(embed=E1)
            return
        elif user is ctx.message.author:
            E2 = discord.Embed(
                description="Why would you waste yourself?",
                color=0x00CCFF
            )
            await ctx.send(embed=E2)
            return
        w = f"https://some-random-api.ml/canvas/wasted?avatar={user.avatar_url}"
        embed = discord.Embed(
            color=0x00CCFF
        )
        embed.set_image(url=w)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Say

    @commands.command()
    async def say(self, ctx, *, text):
        s = requests.get(f"https://gdcolon.com/tools/gdtextbox/img/{text}?color=blue&name={ctx.author.name}&char=scratch")
        await ctx.send(s)

    #Comment

    @commands.command()
    async def comment(self, ctx, *, text):
        e = text.replace(' ','%20')
        m = ctx.author.name.replace(' ','%20')
        c = f"https://gdcolon.com/tools/gdcomment/img/{e}?name={m}&likes={ctx.guild.member_count}&%=100&days=2-second&customIcon=https%3A%2F%2Fgdbrowser.com%2Ficon%2Ficon%3Ficon%3D30%26form%3Dcube%26col1%3D4%26col2%3D16"
        await ctx.send(c)

    #Kill

    @commands.command()
    async def kill(self, ctx, user: discord.Member = None):
        if user is None:
            E1 = discord.Embed(
                title=er,
                description="Please mention a user that you want to `Kill`",
                color=0xFF0000
            )
            E1.add_field(name="Usage", value="--kill [member]")
            E1.add_field(name=nt, value=nd)
            await ctx.send(embed=E1)
            return
        elif user is ctx.message.author:
            E2 = discord.Embed(
                description="Why would you kill yourself?",
                color=0x00CCFF
            )
            await ctx.send(embed=E2)
            return
        r = requests.get("https://api.rishiraj0100.repl.co/api/kill")
        r = (r.json())["args"]
        if "$mention" in r:
            r = r.replace("$mention", user.name)
        if "$author" in r:
            r = r.replace("$author", ctx.author.name)
        embed = discord.Embed(
            description=r,
            color=0x00CCFF
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(api(bot))
    print("API file is loaded!")
