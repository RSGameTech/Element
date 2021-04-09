import discord
import asyncio
from discord.ext import commands
import random

er = "Error"
nt = "Note:-"
nd = "[ ] -> Required\n( ) -> Optional"

class animation(commands.Cog, name="animation"):
    def __init__(self, bot):
        self.bot = bot

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

    #Virus

    @commands.command()
    async def virus(self, ctx, user: discord.Member = None, *, virus: str = "trojan"):
        m = await ctx.send("starting")
        await asyncio.sleep(0.5)
        user = user or ctx.author
        virus = (
        f"`[▓▓▓                    ] / {virus}-virus.exe Packing files.`",
        f"`[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..`",
        f"`[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..`",
        f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..`",
        f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..`",
        f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..`",
        f"`[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..`",
        f"`Successfully downloaded {virus}-virus.exe`",
        "`Injecting virus.   |`",
        "`Injecting virus..  /`",
        "`Injecting virus... -`",
        f"`Successfully Injected {virus}-virus.exe into {user.name}`",
        )
        for i in virus:
            await asyncio.sleep(1.5)
            await m.edit(content=i)

def setup(bot):
    bot.add_cog(animation(bot))
    print("Animation file is loaded!")
