# Discord Bot for Vanilla Minecraft 

## Server Setup
To have your Discord bot communicate with players in Minecraft, you need to enable the RCON protocol by following these steps:

1. Set up a Minecraft server that supports RCON.

2. Enable RCON on your Minecraft server. This is usually done by adding the following lines to your server.properties file:
```
enable-rcon=true
rcon.password=<your_rcon_password>
rcon.port=<your_rcon_port>
```
Make sure to replace `<your_rcon_password>` and `<your_rcon_port>` with the actual values you want to use.

## Bot Functions and Features

## Bot Installation for Users

## References
1. [RCON](https://wiki.vg/RCON#3:_Login): a TCP/IP-based protocol that allows server administrators to remotely execute Minecraft commands  
2. [mcrcon](https://pypi.org/project/mcrcon/): a client for handling Remote Commands (RCON) to a Minecraft server.
3. ConnectionRefusedError: [Errno 111] Connection refused [error](https://stackoverflow.com/questions/47722559/python-valve-rcon-minecraft-connectionrefusederror-errno-111-connection-refu)
4. Minecraft console and slash commands [here](https://minecraft.fandom.com/wiki/Commands#Command_additions_and_changes)

## Background
Minecraft was a game I did not play until the beginning of 2023. I was fortunate enough to be gifted the game and wanted to see what the hype was all about (some 12 years later).

## Idea
Since I had a spare computer laying around, I wanted to get into server hosting. I thought hosting a Minecraft server would be a great way to learn since there is plenty of documentation. In addition, since this server would be hosted "some what" 24/7, I wanted to create an application that would notify me when players would enter and leave the server. What better way for this application to be is a Discord bot. After some research, this is certainly possible.

## Challenge
Given ChatGPT's popularity, it was a tool that I never use until developing this project. I wanted to challenge ChatGPT to see if it can provide an MVP Discord bot using the RCON protocol. This time, I wanted to use Python rather than Javascript because this is a great opprotunity to learn how to develope a Discord bot in another programming langauge. 