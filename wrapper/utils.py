from PIL import Image, ImageSequence
from io import StringIO, BytesIO
import asyncio
from functools import partial
import discord
import aiohttp
import os
from .file import File

class utils():

    async def get_image(self, image):
        headers = image.headers
        r = await image.read()
        return File(r, headers)
