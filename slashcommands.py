from discord_slash.utils.manage_commands import create_option
from discord_slash import SlashCommand
from discord_slash.model import SlashCommandOptionType

import random

# This is an example of a dice roll slash command which imports random 
# When you run the bot, the slash commands should be updated in Discord, but it might take a while to propegate

def roll():
    description = "Dice roll command, up to 999,999,999"
    options = [create_option(
                    name="d",
                    description="Roll a d-sided die",
                    option_type=SlashCommandOptionType.INTEGER,
                    required=True)]
    
    @slash.slash(name="roll", description=description, options=options)
    async def roll(ctx, d):
        if 0 < d <= 999999999:  # dice roll command (up to 999,999,999)
            await ctx.send(content=f"Roll d{d}: `[{str(random.randint(1, d))}]`")
        else:
            await ctx.send(content="Please enter a number between one and one billion")

# define as many slash commands as you want, and add them to the commands list to be initialized

commands = {roll}

def init_slashcommands(client):
    global slash
    slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.
    for i in commands:
        i()
    print("slash commands initialized!")