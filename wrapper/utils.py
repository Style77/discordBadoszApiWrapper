from PIL import Image, ImageSequence
from io import StringIO, BytesIO
import asyncio
from functools import partial
import discord
import aiohttp
import os

class utils():
    def __init__(self, bot):
        self.bot = bot

    def processing(self, image, type_of_img) -> BytesIO:
        im = Image.open(BytesIO(image.content))
        if type_of_img in ["gif", "webm", "gifv"]:
            final_buffer = BytesIO()
            final_buffer.write(image.content)
            final_buffer.seek(0)
            return final_buffer
        final_buffer = BytesIO()
        im.save(final_buffer, type_of_img)
        final_buffer.seek(0)
        return final_buffer

    async def get_image(self, image, type_: str="png"):
        final_buffer = await self.bot.loop.run_in_executor(None, utils.processing, self, image, type_)
        return discord.File(fp=final_buffer, filename=f"nothing.{type_}")
