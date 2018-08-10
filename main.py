import discord

if discord.__author__ is not "Rapptz":
    print("Please use the rewrite version of Discord.py.")
    print("See details in README.")
    exit()

import requests, asyncio, platform
from discord.ext.commands import Bot