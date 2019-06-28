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

    async def get_image(self, image, format=None):
        type_ = image.headers['Content-Type']
        formats_map = {
            "image/png": "png",
            "image/gif": "gif",
            "image/jpeg": "jpg",
            "image/webp": "webp",
            "video/mp4": "mp4",
            "video/webm": "webm"
        }
        image = BytesIO(await image.read())
        if format is None:
            format = formats_map[type_]
        return discord.File(fp=image, filename=f"nothing.{format}")
