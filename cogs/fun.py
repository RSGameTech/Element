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
import random
import requests
import asyncio
from discord.ext import commands

er = "Error"
nt = "Note:-"
nd = "[ ] -> Required\n( ) -> Optional"

class fun(commands.Cog, name="Fun"):
    def __init__(self, bot):
        self.bot = bot

    #Simple

    #Q&A
    @commands.command()
    async def qna(self, ctx, *, question):
        response = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."
                    ]
        embed = discord.Embed(
                title="Q&A",
                description=f"Question: {question}\nAnswer: {random.choice(response)}"
                )
        await ctx.send(embed=embed)

    #F
    @commands.command()
    async def f(self, ctx, *, user: discord.Member = None):
        if user is None:
            await ctx.send(f"{ctx.author.mention} has paid the respect")
        else:
            embed = discord.Embed(
                title="F",
                description=f"{ctx.author.mention} has paid the respect for {user.mention}",
                color=0x00CCFF
            )
            await ctx.send(embed=embed)

    #Animation

    #Hack
    @commands.command()
    async def hack(self, ctx, user: discord.Member = None):
        if user is ctx.message.author:
            E1 = discord.Embed(
                description="Why would you hack yourself?",
                color=0x00CCFF
            )
            await ctx.send(embed=E1)
            return
        elif user is None:
            E2 = discord.Embed(
                title=er,
                description="Please mention the name that you want to `Hack`",
                color=0xFF0000
            )
            E2.add_field(name="Usage", value="--hack [member]")
            E2.add_field(name=nt, value=nd)
            await ctx.send(embed=E2)
            return
        m = await ctx.send("Loading")
        await asyncio.sleep(0.5)
        hack = ("Loading.",
        "Loading..",
        "Loading...",
        f"```\nHaking {user.name}\nStatus:- 0%\n[                    ]\n```",
        "```\nAquiring Data\nStatus:- 5%\n[█                   ]\n```",
        "```\nData Aquired\nStatus:- 10%\n[██                  ]\n```",
        "```\nTracing IP Address\nStatus:- 15%\n[███                 ]\n```",
        "```\nIP Address traced:- 1.234.567.89\nStatus:- 20%\n[████                ]\n```",
        "```\nAccesing Last Channel he/she went\nStatus:- 25%\n[█████               ]\n```",
        "```\nHacking Failed\n```",
        "```\nHacking Failed\nDeleting hack traces\n```",
        "```\nHacking Failed\nFailed to delete traces\n```",
        "```\nHac***g Fa**ed\nFailed ** d****e tra*es\n```",
        "```\nH***********ed\n*****d ********e***a*es\n```",
        "```\n****     *****\n**********   ***    ***\n```",
        "```\n:(\nYour Terminal Ran into a problem\n```"
        )
        for i in hack:
            await asyncio.sleep(1.5)
            await m.edit(content=i)
        await asyncio.sleep(5)
        await ctx.send(f"{ctx.author.mention}, Discord Found you that you were Hacking others, so Discord decided that they will disable your account. Goodbye! :wave:")

    #API

    #Meme
    @commands.command()
    async def meme(self, ctx):
        r = requests.get("https://memes.blademaker.tv/api/memes")
        res = r.json()
        title = res["title"]
        ups = res["ups"]
        downs = res["downs"]
        sub = res["subreddit"]
        author = res["author"]
        embed = discord.Embed(
            title=f"{title}\nAuthor: {author}\nSubreddit: {sub}",
            description=f":+1: : {ups}, :-1: : {downs}",
            color=0x00CCFF
        )
        embed.set_image(url=res["image"])
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Font
    @commands.command()
    async def font(self, ctx, *, text):
        font = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        f = requests.get(f"https://gdcolon.com/tools/gdfont/img/{text}?font={random.choice(font)}")
        embed = discord.Embed(
            colour=0x00CCFF
        )
        embed.set_image(url=f)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #Change My Mind
    @commands.command(aliases=['cmm'])
    async def changemymind(self, ctx, *, text):
        c = requests.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}").json()
        url = c["message"]
        await ctx.send(url)

    #Threats
    @commands.command(aliases=['t'])
    async def threats(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        t = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={user.avatar_url}").json()
        url = t["message"]
        embed = discord.Embed(
            title="Threats",
            colour=0x00CCFF
        )
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    #iPhone
    @commands.command()
    async def iphone(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        i = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={user.avatar_url}").json()
        url = i["message"]
        embed = discord.Embed(
            title="iPhone",
            colour=0x00CCFF
        )
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(fun(bot))
    print("Fun file is loaded!")
