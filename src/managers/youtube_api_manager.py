import youtube_dl

import nextcord
import asyncio

from config import FFMPEG_OPTIONS, YDL_OPTIONS

async def yt_load(url):
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            return await nextcord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
             