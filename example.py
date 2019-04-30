import wrapper
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
app = wrapper.Wrapper(token="token", bot=bot)

"""docs in future"""

"""discord.py cog example"""
import wrapper
import discord
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.app = wrapper.Wrapper(token="token", bot=bot)

    @commands.command()
    async def my_nice_command(self, ctx, member: discord.Member=None):
        member = ctx.author or member
        f = await app.blurple(member.avatar_url_as("png"))
        return await ctx.send(file=f)

#your setup function

