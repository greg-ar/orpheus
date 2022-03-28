import discord
from discord.ext import commands

class util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(ctx):
        await ctx.send(f'```Ping: {round(this.client.latency * 1000)} ms```')

    @commands.command()
    async def hello(ctx):
        await ctx.send("Hello There")

def setup(client):
    client.add_cog(util(client))
