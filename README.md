# discord.py-starter
Starter code for a python discord bot

# Setup:
If running yourself, install discord.py and discord-py-slash-command (pip install)
Add a text file called token.txt with your discord bot token

If running with Github action runners, fork this, go to your repo -> settings -> secrets -> actions
Create a new repo secret called TOKEN and set the value to your github bot token
To run the bot, you can start it manually from Actions -> your workflow (discord.py-starter) -> run workflow
These have a limit of like 3 days but if you uncomment some lines in the /.github/workflows/python-app.yml file, you can make the bot restart every day and/or whenever you push a change to the repo.
If not using Github actions, this folder can be ignored.

If you want to use Docker, I added a Dockerfile which can be used to create a docker image. Add your install requirements to requirements.txt; everything there will be run with pip install.
If not using Docker, these files can be ignored.