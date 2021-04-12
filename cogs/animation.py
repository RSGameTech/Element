import discord
import asyncio
import random
from discord.ext import commands

er = "Error"
nt = "Note:-"
nd = "[ ] -> Required\n( ) -> Optional"

class animation(commands.Cog, name="animation"):
    def __init__(self, bot):
        self.bot = bot

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
