from setuptools import setup, find_packages

with open("README.md", "r") as ld:
    long_description = ld.read()

setup(
    name="DiscordBadoszApiWrapper.py",
    version="1.0",
    author="Style",
    author_email="stylek777@gmail.com",
    description="Badosz api wrapper focused on discord.py",
    long_description=long_description,
    url="xd",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
