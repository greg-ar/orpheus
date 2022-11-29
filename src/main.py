import asyncio

from config import TOKEN
from setup import bot_setup
'''
try:
    loop = asyncio.get_running_loop()
except RuntimeError:  # 'RuntimeError: There is no current event loop...'
    loop = None
'''
def bot():
    print("Orpheus Starting Up")

    client = bot_setup()

    print("Orpheus is ready, logging in Discord")
    client.run(TOKEN)

    print("\nOrpheus Shuting Down")

if __name__=="__main__":
    asyncio.run(bot())