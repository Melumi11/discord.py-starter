# -------------------------------import----------------------------------#
import logging
from client import *
import slashcommands
# -----------------------------------------------------------------------#


# Logging errors
logging.basicConfig(level=logging.ERROR)


# -------------------------------variables-------------------------------#
client = Client() # from client.py (this contains everything needed for the bot to function)

# -----------------------------------------------------------------------#


# -----------------------------slash commands----------------------------#
slashcommands.init_slashcommands(client) # defines all your slash command functions

# -----------------------------------------------------------------------#


# -------------------------------launch bot------------------------------#
with open('token.txt') as f:
    TOKEN = f.readline() # put bot token in git ignored file token.txt
client.run(TOKEN)
# -----------------------------------------------------------------------#
