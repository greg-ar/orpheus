import discord
from discord.ext import commands
import music


def main():
    cogs = [music]

    client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

    for i in range(len(cogs)):
        cogs[i].setup(client)

    token_file = open('token/token.txt','r')
    token = token_file.read()

    print("Orpheus Start")
    client.run(token)
    print("Orpheus Shutting Down")

if __name__ == '__main__':
    main()
