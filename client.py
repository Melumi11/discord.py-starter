import discord

# DO NOT RUN THIS FILE
# Run main.py instead, this file will do nothing. This is where you put your text commands/responses to messages

class Client(discord.Client):
    # -------------------------------"Global" Variables:-------------------------------#
    # for example:
    # MELUMI = 640714673045504020  # my discord id
    # ----------------------------------------------------------------------------------#

    async def on_ready(self):
        # this runs when you first start the bot
        # for example: this sets the bot's status to "Playing *To the Moon*" and prints "bot online" in the terminal
        activity = discord.Activity(type=discord.ActivityType.playing,
                                    name="To the Moon")  # Playing, Listening to, Watching, also streaming, competing
        await self.change_presence(activity=activity)
        print('bot online')
    
    # This runs every time someone sends a message
    async def on_message(self, message):
        if message.author == self.user:  
            # so that the bot doesn't respond to itself
            return
        
        message_lower = message.content.lower()
        """
        here you can define bot commands, message_lower.startswith can help
        if message_lower.startswith('!'):
            if message_lower == '!hello':
                await message.channel.send("hello")
        """



# Some possibly helpful reference

# wait:
# await asyncio.sleep(10)
# reply:
# await message.channel.reply('Hello!', mention_author=False)

# Very cool debug command that stops the script and shows all variables, can resume after
# import code
# code.interact(local=locals())