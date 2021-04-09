import discord
from discord.ext import commands
from discord.utils import get


class event(commands.Cog, name="Events"):
    def __init__(self, bot):
        self.bot = bot

    #member Join

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.role, name="Verified")
        channel = self.bot.get_channel(772856544193675285)
        embed = discord.Embed(title="Good News",
                            description=f"{member.mention} just joined the Server, Welcome him by chatting(Not in DM)",color=discord.Color.blue()
                            )
        await member.add_role(role)
        await channel.send(embed=embed)

    #Member Leave

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel = self.bot.get_channel(772856544193675285)
        embed = discord.Embed(
            title="Sad News",
            description=f"{member.name} just left the Server. Everyone is sad now",
            color=0xFF0000
        )
        await channel.send(embed=embed)

    #Join Voice Channel

    @commands.command()
    @commands.is_owner()
    async def join(self, ctx, *, channel:discord.VoiceChannel):
        await channel.connect()

    #Leave Voice Channel

    @commands.command()
    @commands.is_owner()
    async def leave(self, ctx, *, channel:discord.VoiceChannel):
        await channel.disconnect()

def setup(bot):
    bot.add_cog(event(bot))
    print("Event file is loaded!")
