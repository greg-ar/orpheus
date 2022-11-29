from config import TOKEN
from setup import bot_setup


def bot():
    print("Orpheus Starting Up")

    client = bot_setup()

    print("Orpheus is ready, logging in Discord")
    client.run(TOKEN)

    print("\nOrpheus Shuting Down")

if __name__=="__main__":
    bot()