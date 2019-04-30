from PIL import Image
from io import StringIO, BytesIO
import asyncio
from functools import partial
import discord
import aiohttp

class utils():
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=bot.loop)

    async def get_img_bytes(self, image) -> bytes:
        async with self.session.get(image) as response:
            img_bytes = await response.read()

        return img_bytes

    def processing(self, image):
        with Image.open(image) as im:
            final_buffer = BytesIO()
            im.save(final_buffer, "png")

        final_buffer.seek(0)
        return final_buffer

    async def get_image(self, image):
        im = await utils.get_img_bytes(self, image)
        fn = partial(utils.processing, self, im)
        final_buffer = await self.bot.loop.run_in_executor(None, fn)
        return discord.File(fp=final_buffer)
