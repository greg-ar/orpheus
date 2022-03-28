import discord
from discord.ext import commands
import music
import util

def cogs_setup(client):
    cogs = [music,util]
    for i in range(len(cogs)):
        cogs[i].setup(client)
