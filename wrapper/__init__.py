from .Badosz import Application
import requests
from .utils import utils

from PIL import Image
from io import StringIO
import asyncio
import discord
import aiohttp

import sys


def my_except_hook(exctype, value, traceback):
    if exctype == ValueError:
        print(traceback)
    else:
        sys.__excepthook__(exctype, value, traceback)

sys.__excepthook__ = my_except_hook

class WrongParameter(Exception):
    pass

class Wrapper(object):
    __slots__ = ("token", "base_api_link", "headers", "bot", "session")
    
    def __init__(self, **kwargs):
        self.token = kwargs.get("token")
        self.base_api_link = "https://api.badosz.com"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }
        self.bot = kwargs.get("bot")
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @property
    async def advice(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/advice",
                              headers=self.headers) as r:
                r = await r.json()
        return r['advice']

    @property
    async def bird(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/bird",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    async def blurple(self, url):
        url_page = await aiohttp.ClientSession().get(url)
        if url_page.status != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/blurple",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def cat(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/cat",
                              headers=self.headers) as r:
                r = await r.json()
        return r['cat']

    async def changemymind(self, text):
        payload = {
            "text": text
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/changemymind",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def chucknorris(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/chucknorris",
                              headers=self.headers) as r:
                r = await r.json()
        return r['joke']

    @property
    async def cuddle(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/cuddle",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def dadjoke(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/dadjoke",
                              headers=self.headers) as r:
                r = await r.json()
        return r['joke']

    @property
    async def dog(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/dog",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    async def execuseme(self, text):
        payload = {
            "text": text
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/execuseme",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def fact(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/fact",
                              headers=self.headers) as r:
                r = await r.json()
        return r['fact']

    @property
    async def fox(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/fox",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def hug(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/hug",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f
    
    async def invert(self, url):
        url_page = await aiohttp.ClientSession().get(url)
        if url_page.status != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/invert",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def kiss(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/kiss",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    async def note(self, text):
        payload = {
            "text": text
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/note",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    async def orangly(self, url):
        url_page = await aiohttp.ClientSession().get(url)
        if url_page.status != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/orangly",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def pat(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/pat",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def shibe(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/shibe",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    async def triggered(self, url):
        url_page = await aiohttp.ClientSession().get(url)
        if url_page.status != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/triggered",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    async def trump(self, text):
        payload = {
            "text": text
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/trump",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    async def tweet(self, url, text, username):
        url_page = await aiohttp.ClientSession().get(url)
        if url_page.status != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url,
            "text": text,
            "username": username
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/tweet",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    async def wanted(self, url):
        url_page = await aiohttp.ClientSession().get(url)
        if url_page.status != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/wanted",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    async def wasted(self, url):
        url_page = await aiohttp.ClientSession().get(url)
        if url_page.status != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/wasted",
                              headers=self.headers, params=payload) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def why(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/why",
                              headers=self.headers) as r:
                r = await r.json()
        return r['why']

    @property
    async def yomomma(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/yomomma",
                              headers=self.headers) as r:
                r = await r.json()
        return r['joke']

    """nsfw section"""

    @property
    async def anal(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/anal",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def ass(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/ass",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def bdsm(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/bdsm",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f
    
    @property
    async def blowjob(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/blowjob",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f
    
    @property
    async def boobs(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/boobs",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def ginger(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/ginger",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def gonewild(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/gonewild",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def hentai(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/hentai",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def lesbian(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/lesbian",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def milf(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/milf",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def nsfw(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/nsfw",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def porngif(self): # for some reasons just this is not working with correct format
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/porngif",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r, "gif")
        return f

    @property
    async def pussy(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/pussy",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def snapchat(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/snapchat",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f

    @property
    async def teen(self):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link+"/teen",
                              headers=self.headers) as r:
                f = await utils.get_image(self, r)
        return f
