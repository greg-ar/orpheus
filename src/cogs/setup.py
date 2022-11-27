from cogs.util_cogs import util
from cogs.music_cogs import music

def cog_setup(client):

    client.add_cog(util(client))
    client.add_cog(music(client))