from PIL import Image
from io import StringIO, BytesIO
import asyncio
from functools import partial
import discord

class utils():

    def get_image(self, image, loop):
        fn = partial(utils.processing, image)
        final_buffer = loop.run_in_executor(None, fn)
        return discord.File(fp=final_buffer)

    def processing(self, image):
        with Image.open(image):
            final_buffer = BytesIO()
            image.save(final_buffer, "png")
        
        final_buffer.seek(0)
        return final_buffer
