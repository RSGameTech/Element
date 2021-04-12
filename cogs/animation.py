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
