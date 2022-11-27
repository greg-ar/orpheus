import nextcord
from nextcord.ext import commands

from managers.youtube_api_manager import yt_load

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("I don't like playing music alone...")
        else: 
            await ctx.send("Joining VC")
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()
            else: 
                await ctx.voice_client.move_to(voice_channel)
            
            await ctx.guild.change_voice_state(channel=voice_channel, self_mute=False, self_deaf=True)

    @commands.command()
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()
        
    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        ctx.voice_client.play(await yt_load(url))

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
