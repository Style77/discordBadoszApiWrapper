import wrapper
from discord.ext import commands
import asyncio

app = wrapper.Wrapper(token=)

async def test():
    z = await app.fox
    print(await z.get_discord_file())

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

"""
# discord.py cog example

import wrapper
import discord
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.app = wrapper.Wrapper(token="token")

    @commands.command()
    async def my_nice_command(self, ctx, member: discord.Member=None):
        member = ctx.author or member
        f = await app.blurple(str(member.avatar_url))
        return await ctx.send(file=f)

#your setup function

"""
