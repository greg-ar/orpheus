from nextcord.ext import commands

class util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'```Ping: {round(self.client.latency * 1000)} ms```')

    @commands.command()
    async def hello(self,ctx):
        await ctx.send("Hello There")