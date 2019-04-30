from .Badosz import Application
import requests
from .utils import utils

from PIL import Image
from io import StringIO
import asyncio
import discord

class WrongParameter(Exception):
    pass

class Wrapper(object):
    __slots__ = ("token", "base_api_link", "headers", "loop")
    
    def __init__(self, **kwargs):
        self.token = kwargs.get("token")
        self.base_api_link = "https://api.badosz.com"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }
        self.loop = asyncio.new_event_loop()

    @property
    def advice(self):
        r = requests.get(self.base_api_link+"/advice", 
                                 headers=self.headers)
        r = r.json()
        return r['advice']

    @property
    async def bird(self):
        r = requests.get(self.base_api_link+"/bird",
                                 headers=self.headers)
        f = await utils.get_image(self, r)
        return f

    async def blurple(self, url):
        url_page = requests.get(url)
        if url_page.status_code != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        r = requests.get(self.base_api_link+"/blurple",
                                 headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    @property
    def cat(self):
        r = requests.get(self.base_api_link+"/cat",
                         headers=self.headers)
        r = r.json()
        return r['cat']

    async def changemymind(self, text):
        payload = {
            "text": text
        }
        r = requests.get(self.base_api_link+"/changemymind",
                         headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    @property
    def chucknorris(self):
        r = requests.get(self.base_api_link+"/chucknorris",
                         headers=self.headers)
        r = r.json()
        return r['joke']

    @property
    async def cuddle(self):
        r = requests.get(self.base_api_link+"/cuddle",
                         headers=self.headers)
        f = await utils.get_image(self, r)
        return f

    @property
    def dadjoke(self):
        r = requests.get(self.base_api_link+"/dadjoke",
                         headers=self.headers)
        r = r.json()
        return r['joke']

    @property
    async def dog(self):
        r = requests.get(self.base_api_link+"/dog",
                         headers=self.headers)
        f = await utils.get_image(self, r)
        return f

    async def execuseme(self, text):
        payload = {
            "text": text
        }
        r = requests.get(self.base_api_link+"/execuseme",
                         headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    @property
    def fact(self):
        r = requests.get(self.base_api_link+"/fact",
                         headers=self.headers)
        r = r.json()
        return r['fact']

    @property
    async def fox(self):
        r = requests.get(self.base_api_link+"/fox",
                         headers=self.headers)
        f = await utils.get_image(self, r)
        return f

    @property
    async def hug(self):
        r = requests.get(self.base_api_link+"/hug",
                         headers=self.headers)
        f = await utils.get_image(self, r)
        return f
    
    async def invert(self, url):
        url_page = requests.get(url)
        if url_page.status_code != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        r = requests.get(self.base_api_link+"/invert",
                         headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    @property
    async def kiss(self):
        r = requests.get(self.base_api_link+"/kiss",
                         headers=self.headers)
        f = await utils.get_image(self, r)
        return f

    async def note(self, text):
        payload = {
            "text": text
        }
        r = requests.get(self.base_api_link+"/note",
                         headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    async def orangly(self, url):
        url_page = requests.get(url)
        if url_page.status_code != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        r = requests.get(self.base_api_link+"/orangly",
                         headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    @property
    async def pat(self):
        r = requests.get(self.base_api_link+"/pat",
                         headers=self.headers)
        f = await utils.get_image(self, r)
        return f

    @property
    async def shibe(self):
        r = requests.get(self.base_api_link+"/shibe",
                         headers=self.headers)
        f = await utils.get_image(self, r)
        return f

    async def triggered(self, url):
        url_page = requests.get(url)
        if url_page.status_code != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        r = requests.get(self.base_api_link+"/triggered",
                         headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    async def trump(self, text):
        payload = {
            "text": text
        }
        r = requests.get(self.base_api_link+"/trump",
                         headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    async def tweet(self, url, text, username):
        url_page = requests.get(url)
        if url_page.status_code != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url,
            "text": text,
            "username": username
        }
        r = requests.get(self.base_api_link+"/tweet",
                         headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    async def wanted(self, url):
        url_page = requests.get(url)
        if url_page.status_code != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        r = requests.get(self.base_api_link+"/wanted",
                         headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    async def wasted(self, url):
        url_page = requests.get(url)
        if url_page.status_code != 200:
            raise WrongParameter("Error appeared while trying to get image.")
        payload = {
            "url": url
        }
        r = requests.get(self.base_api_link+"/wasted",
                         headers=self.headers, params=payload)
        f = await utils.get_image(self, r)
        return f

    @property
    def why(self):
        r = requests.get(self.base_api_link+"/why",
                         headers=self.headers)
        r = r.json()
        return r['why']

    @property
    def yomomma(self):
        r = requests.get(self.base_api_link+"/yomomma",
                         headers=self.headers)
        r = r.json()
        return r['joke']
