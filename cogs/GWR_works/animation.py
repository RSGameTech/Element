import discord
import asyncio
from discord.ext import commands
import random

class anim(commands.Cog, name="animation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cathi(self, ctx, *, text: str = "Hi..."):
        m = await ctx.send("0.1 sec only to start")
        await asyncio.sleep(0.1)
        list = (
            """ຸ 　　　＿＿_＿＿
　　／　／　  ／|"
　　|￣￣￣￣|　|
　　|　　　　|／
　　￣￣￣￣""",
            f"""ຸ 　　　{text}
 　   　 ∧＿∧＿_
　　／(´･ω･`)  ／＼
　／|￣￣￣￣|＼／
　　|　　　　|／
　　￣￣￣￣""",
        )
        for i in range(3):
            for cat in list:
                await asyncio.sleep(1.5)
                await m.edit(content=cat)

    @commands.command()
    async def flop(self, ctx):
        m = await ctx.send("1 sec pls")
        await asyncio.sleep(0.5)
        flop = (
            "(   ° - °) (' - '   )",
            "(\\\° - °)\ (' - '   )",
            "(—°□°)— (' - '   )",
            "(╯°□°)╯(' - '   )",
            "(╯°□°)╯︵(\\\ .o.)\\",
        )
        for i in flop:
            await asyncio.sleep(1.5)
            await m.edit(content=i)

    @commands.command()
    async def poof(self, ctx):
        m = await ctx.send("1 sec pls")
        await asyncio.sleep(0.5)
        """poofness"""
        poof = ("(   ' - ')", "' - ')", "- ')", "')", ")", "*poofness*")
        for i in poof:
            await asyncio.sleep(1.5)
            await m.edit(content=i)

    @commands.command()
    async def boom(self, ctx):
        m = await ctx.send("```THIS MESSAGE WILL SELFDESTRUCT IN 5```")
        await asyncio.sleep(1.5)
        boom = (
            "```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
            "💣",
            "💥",
        )
        for i in boom:
            await asyncio.sleep(1.5)
            await m.edit(content=i)

    @commands.command()
    async def table(self, ctx):
        m = await ctx.send("`(\°-°)\  ┬─┬`")
        table = (
            "`(\°□°)\  ┬─┬`",
            "`(-°□°)-  ┬─┬`",
            "`(╯°□°)╯    ]`",
            "`(╯°□°)╯     ┻━┻`",
            "`(╯°□°)╯       [`",
            "`(╯°□°)╯          ┬─┬`",
            "`(╯°□°)╯                 ]`",
            "`(╯°□°)╯                  ┻━┻`",
            "`(╯°□°)╯                         [`",
            "`(\°-°)\                               ┬─┬`",
        )
        for i in table:
            await asyncio.sleep(1.5)
            await m.edit(content=i)

    @commands.command()
    async def warning(self, ctx):
        m = await ctx.send("0")
        warn = (
            "`LOAD !! WARNING !! SYSTEM OVER`",
            "`OAD !! WARNING !! SYSTEM OVERL`",
            "`AD !! WARNING !! SYSTEM OVERLO`",
            "`D !! WARNING !! SYSTEM OVERLOA`",
            "`! WARNING !! SYSTEM OVERLOAD !`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`ARNING !! SYSTEM OVERLOAD !! W`",
            "`RNING !! SYSTEM OVERLOAD !! WA`",
            "`NING !! SYSTEM OVERLOAD !! WAR`",
            "`ING !! SYSTEM OVERLOAD !! WARN`",
            "`NG !! SYSTEM OVERLOAD !! WARNI`",
            "`G !! SYSTEM OVERLOAD !! WARNIN`",
            "`!! SYSTEM OVERLOAD !! WARNING`",
            "`! SYSTEM OVERLOAD !! WARNING !`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.01 SEC!`",
            "`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`",
            "`CTRL + R FOR MANUAL OVERRIDE..`",
        )
        for i in warn:
            await asyncio.sleep(0.5)
            await m.edit(content=i)


def setup(bot):
    bot.add_cog(anim(bot))
