# Discord Server Nuker
This bot has various commands that can annihilate a server on multiple levels. A good service if you want to start your server all fresh! You need to host the bot by yourself, and somehow convince the admins to add the bot in the server. There are some disguised commands like normal `kick` and `ban` which work like like normal, so you can make the argument that you created a custom bot for the server or whatever, that's up to you.
## Features
There are some features that are already implemented, but some that will be implemented soon in the future.
- [x] Delete all Emojis
- [x] Delete all Roles
- [x] Delete all Channels
- [ ] Ban all Users(Except other admins with their role above the bot's)
- [ ] Kick all Users(Except other admins with their role above the bot's)
- [ ] Do all of these things at once
- [ ] Change server settings, like name, profile picture, etc
- [ ] Gives the user administrator permissions
## Prerequisites
You need the following installed: [Python](https://www.python.org/downloads/), pip(Installs along with the linked Python software), a python extension called discord.py(type `pip install discord` in command prompt
## How to use
1. First, you need to make a [bot application](https://discord.com/developers/applications) and invite it to your server. Discord has provided very good [documentation](https://discordpy.readthedocs.io/en/latest/discord.html) to do that. **Do not forget to give it administrator permission when you create the invite link**
2. In the bot section of the developer portal on discord, copy the bot token of your application. 
3. Download and open the file `bot.py` in a text editor, like Notepad or Notepad++.
4. Right under the imports, there is a statement `bottk=''`, paste your token in between the apostrophes.
5. Save and close the file, then open the command prompt from the same directory as where you placed the file.
6. Type `py bot.py` in the command window. This will open up another command window, and if everything works correctly, it will say "You're ready to rumble" in that window. And indeed, now you're ready to get started.

## Commands
* !omegalulgone : Deletes all of the emojis in the server
* !allwhite : Deletes all of the roles.(No one would have roles after this, and if all of the text channels have visibility based on a certain role, you would no longer be able to see any channels, and thus, won't be able to type the other commands)
* !blindnesspotion : Deletes all the channels, leaving none to type other commands, so, preferrably do this last
