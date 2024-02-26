# Discord Bot for Vanilla Minecraft (Java Edition) <img src='https://cdn3.emoji.gg/emojis/1491-minecraft.png' width='25'>
![image](https://github.com/HerndonE/Vanilla-Minecraft-Discord-Bot/blob/main/Images/banner.png?raw=true)

## Abstract
Minecraft was a game I did not play until the beginning of 2023. I was fortunate enough to be gifted the game and got to see what the hype was all about (some 12 years later). Having a spare computer, I wanted to get into server hosting. I thought hosting a Minecraft server would be a great way to learn since there is plenty of documentation. In addition, since this server would be hosted "_some what_" 24/7, I wanted to create an application that would notify me when players would enter and leave the server. What better way for this application to be is a Discord bot.

## Inspiration
Given ChatGPT's popularity in early 2023, it was a tool that I never use until developing this project. I wanted to challenge ChatGPT to see if it can provide an MVP Discord bot using the RCON protocol. In addition, I wanted to use Python rather than Javascript because this is a great opprotunity to learn how to develope a Discord bot in another programming langauge. 

## Discord Bot Setup <img src='https://cdn3.emoji.gg/emojis/9255-discord.png' width='20'>
Before you use this Discord bot for Minecraft, you must set up a Discord bot first.   
1. Log on to the [Discord website](https://discord.com/).  
2. Naviagte to the [application page](https://discord.com/developers/applications).
3. Click the “_New Application_” button.
4. Give the your Discord bot a name i.e. "_MyMinecraftBot_" and click “_Create_”.
5. Navigate to the “_Bot_” tab for configuration.
6. Make sure that your Discord bot is ticked for **PUBLIC BOT** so you can invite the bot to your server.
7. Copy the Discord bot token using the “_Copy_” button. _**Note:** Keep this token in a safe location_

## Invite Discord Bot to Discord Server <img src='https://cdn3.emoji.gg/emojis/6174-w98-computer.png' width='20'>
1. If you are not on your Discord bots page, navigate to the bots page.  
2. Go to the “OAuth2 -> URL Generator” tab.
3. Click the "_bot_" checkbox under "scopes". _**Note:** This may change over time as new features get implemented_
4. Navigate to the bottom of the page and copy your Discord bot url under **GENERATED URL**.
5. Paste the URL into browser URL field and select which server to invite your bot.

## Server Setup <img src='https://cdn3.emoji.gg/emojis/1491-minecraft.png' width='15'>
To have your Discord bot communicate with people in Discord and players in Minecraft, you need to enable the RCON protocol by following these steps:

1. Set up a Minecraft server that supports RCON.

2. Enable RCON on your Minecraft server. This is usually done by adding the following lines to your server.properties file:
```
enable-rcon=true
rcon.password=<your_rcon_password>
rcon.port=<your_rcon_port>
```
Make sure to replace `<your_rcon_password>` and `<your_rcon_port>` with the actual values you want to use.

## Bot Installation for Users
1. Download the Minecraft Discord Bot Setup Wizard executable [here](https://github.com/HerndonE/Vanilla-Minecraft-Discord-Bot/blob/main/Minecraft%20Discord%20Bot%20Seutp%20Wizard.exe?raw=true).
2. The Setup Wizard will download and install the latest Minecraft Discord Bot release.
3. Follow the configuration instructions to get your Minecraft Discord Bot started.

## Bot Functions and Features
The Minecraft Discord Bot provides:

<div style='padding:0.7em; margin-left:0.7em; display: inline-block;'>
  <img src="https://raw.githubusercontent.com/HerndonE/Vanilla-Minecraft-Discord-Bot/main/Images/features.jpg" width="350" align="right" style='padding:0.27em;' />
  <ol>
    <li>Users and Players the ability to chat between the Minecraft and Discord Server</li>
    <li>Notifications to Discord users when a player joins and leaves a game.</li>
    <li>Notifications to Discord users when a player dies or earns an achievement.</li>
    <li>Notifications to Discord users when the bot stops reading the Minecraft server logs (<i>this allows the Minecraft server to create new logs</i>).</li>
    <li>Notifications to Discord users when the Minecraft server host stops the server.</li>
  </ol>
</div>

## References
1. [RCON](https://wiki.vg/RCON#3:_Login): a TCP/IP-based protocol that allows server administrators to remotely execute Minecraft commands  
2. [MRCON](https://pypi.org/project/mcrcon/): a client for handling Remote Commands (RCON) to a Minecraft server.
3. ConnectionRefusedError: [Errno 111] Connection refused [error](https://stackoverflow.com/questions/47722559/python-valve-rcon-minecraft-connectionrefusederror-errno-111-connection-refu)
4. Minecraft console and slash commands [here](https://minecraft.fandom.com/wiki/Commands#Command_additions_and_changes)
