import nextcord
from nextcord.ext import commands

from cogs.setup import cog_setup

def bot_setup():
    intents = nextcord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix="!", intents=intents)

    @client.event
    async def on_ready():
        print(f"Orpheus logged in as {client.user}") 

    @client.event 
    async def on_message(ctx):
        if ctx.author == client.user:
            return 
        
        await client.process_commands(ctx)

    cog_setup(client)


    return client 