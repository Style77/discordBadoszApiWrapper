import wrapper

app = wrapper.Wrapper(token="token")
print(type(app.blurple("https://i.imgur.com/BGH4OoZ.png")))
print(app.advice)
print(app.bird)
print(app.blurple("https://i.imgur.com/BGH4OoZ.png"))
print(app.cat)
print(app.changemymind("jesteś gejem"))
print(app.chucknorris)
print(app.cuddle)
print(app.dadjoke)
print(app.dog)
print(app.execuseme("co kurczak"))
print(app.invert("https://i.imgur.com/BGH4OoZ.png"))
print(app.kiss)
print(app.note("Marcin"))
print(app.orangly("https://i.imgur.com/BGH4OoZ.png"))
print(app.pat)
print(app.shibe)
print(app.triggered("https://i.imgur.com/BGH4OoZ.png"))
print(app.execuseme("trumpson"))
print(app.tweet(url="https://i.imgur.com/BGH4OoZ.png", text="siema to ja", username="Marek"))
print(app.wanted("https://i.imgur.com/BGH4OoZ.png"))
print(app.wasted("https://i.imgur.com/BGH4OoZ.png"))
print(app.why)
print(app.yomomma)

"""discord.py cog example"""
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
        return await ctx.send(file=app.blurple(member.avatar_url_as("png")))

#your setup function

