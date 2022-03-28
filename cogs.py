import discord
from discord.ext import commands
import music

def cogs_setup(client):
    cogs = [music]
    for i in range(len(cogs)):
        cogs[i].setup(client)
