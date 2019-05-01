from PIL import Image
from io import StringIO, BytesIO
import asyncio
from functools import partial
import discord
import aiohttp

class utils():
    def __init__(self, bot):
        self.bot = bot

    def processing(self, image) -> BytesIO:
        im = Image.open(BytesIO(image.read()))
        final_buffer = BytesIO()
        im.save(final_buffer, "png")
        final_buffer.seek(0)
        return final_buffer

    async def get_image(self, image):
        fn = partial(utils.processing, self, image)
        final_buffer = await self.bot.loop.run_in_executor(None, fn)
        return discord.File(fp=final_buffer)
