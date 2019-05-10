import wrapper
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
app = wrapper.Wrapper(token="token", bot=bot)

@bot.command()
async def my_command(ctx, member: discord.Member):
    await ctx.send(file=discord.File(await app.blurple(str([member.avatar_url if member else ctx.author.avatar_url])))) # Xd

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
        f = await app.blurple(str(member.avatar_url))
        return await ctx.send(file=f)

#your setup function

