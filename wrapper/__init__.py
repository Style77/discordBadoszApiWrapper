from .Badosz import Application
import requests
from .utils import utils
from .file import File

from PIL import Image
from io import StringIO
import asyncio
import discord
import aiohttp

class BaseException(Exception):
    pass

class WrongParameter(BaseException):
    pass

class NotFound(BaseException):
    pass

image_endpoints = ['bird', 'cuddle', 'dog', 'fox', 'hug',
                    'kiss', 'pat', 'shibe', 'anal', 'ass',
                    'bdsm', 'blowjob', 'boobs', 'ginger',
                    'gonewild', 'hentai', 'lesbian', 'milf',
                    'nsfwimg', 'porngif', 'pussy', 'snapchat',
                    'teen', 'tickle', 'poke', 'feed', 'catgirl',
                    'lewd', 'spreadeagle', 'legs', 'pajamas']

all_endpoints = ['bird', 'cuddle', 'dog', 'fox', 'hug',
                    'kiss', 'pat', 'shibe', 'anal', 'ass',
                    'bdsm', 'blowjob', 'boobs', 'ginger',
                    'gonewild', 'hentai', 'lesbian', 'milf',
                    'nsfw', 'porngif', 'pussy', 'snapchat',
                    'teen', 'tickle', 'poke', 'feed', 'catgirl',
                    'advice', 'cat', 'chucknorris', 'dadjoke',
                    'fact', 'why', 'yomomma']

endpoints_map = {
            'advice': 'advice',
            'cat': 'cat',
            'chucknorris': 'joke',
            'dadjoke': 'joke',
            'fact': 'fact',
            'why': 'why',
            'yomomma': 'joke'
            }

class Wrapper:
    __slots__ = ("token", "base_api_link", "headers")

    def __init__(self, **kwargs):
        self.token = kwargs.get("token")
        self.base_api_link = "https://api.badosz.com"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }

    async def __getattr__(self, attr):
        if not attr in all_endpoints:
            raise NotFound("This endpoint does not exist.")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.base_api_link + '/' + attr,
                        headers=self.headers) as r:
                if attr in image_endpoints:
                    return File(await r.read(), r.headers)
                r = await r.json()
                return r[endpoints_map[attr]]

    async def blurple(self, url):
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
