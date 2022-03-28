import discord
from discord.ext import commands
from cogs import cogs_setup


def main():

    client = commands.Bot(command_prefix='!', intents = discord.Intents.all())
    cogs_setup(client)

    token_file = open('token/token.txt','r')
    token = token_file.read()

    print("Orpheus Start")
    client.run(token)
    print("Orpheus Shutting Down")

if __name__ == '__main__':
    main()
