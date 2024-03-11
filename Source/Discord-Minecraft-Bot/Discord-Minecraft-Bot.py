"""
Author     : Ethan Herndon
Date       : 3/10/24
Filename   : Discord-Minecraft-Bot.py
Desc       : Discord bot to allow communication between Discord and Minecraft users.
References :
https://stackoverflow.com/questions/10747974/how-to-check-if-the-current-time-is-in-range-in-python
"""

import discord
import asyncio
import mcrcon
import re
import os
import json
from discord.ext import tasks
import datetime

intents = discord.Intents.all()
client = discord.Client(intents=intents, heartbeat_timeout=120.0, guild_subscriptions=False)


# Check if the current time is within the allowed time range.
def time_in_range(start, end, current_time):
    # Return true if current time is in the range [start, end].
    if start <= end:
        return start <= current_time <= end
    else:
        return start <= current_time or current_time <= end


# Read the latest player chat messages from the Minecraft server log file.
async def read_player_chat_messages():
    time_check = False
    # Read the latest log file and start at the end.
    get_activity = get_info()
    log_directory = get_activity[0]["Log_File_Directory"]

    with open(f"{log_directory}\\latest.log", "r", encoding="utf-8") as log_file:
        log_file.seek(0, 2)
        while True:
            start = datetime.time(23, 35, 0)
            end = datetime.time(0, 35, 0)
            if time_in_range(start, end, datetime.datetime.now().time()) and time_check is False:
                time_check = True
                print(f"THE BOT WILL STOP READING SERVER LOG FILE AND WILL RESUME AT 00:35AM/12:35AM")
                break
            try:
                # Get the current position of the file pointer.
                current_position = log_file.tell()

                # Read the latest lines added to the file.
                latest_lines = log_file.readlines()

                # If there are no new lines, wait for a bit and try again.
                if not latest_lines:
                    await asyncio.sleep(0.1)
                    log_file.seek(current_position)
                else:
                    # Go through the new lines and print out any player chat messages.
                    for line in latest_lines:
                        if "[DISCORD]" in line:
                            continue

                        if any(item in line for item in get_activity[0]["Different_Progressions"]):
                            if "]: <" in line:
                                get_time = line.split()
                                get_player_name = re.search(r"<(.*?)>", line)
                                player_name = get_player_name.group(1)
                                chat_message = line.split("<")[1].split(">")[1]
                                message = discord.Embed(description="", color=0x0000FF)
                                message.set_author(name=f"{get_time[0]} | {player_name}: {chat_message}")
                                channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Chat"])
                                await channel.send(embed=message)
                                break

                            line = line.split()
                            get_time = line[0]
                            del line[0:3]
                            message = discord.Embed(description="", color=0x48066F)
                            message.set_author(name=f"{get_time} | {' '.join(line)}")
                            channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Activity"])
                            await channel.send(embed=message)

                        if any(item in line for item in get_activity[0]["Different_Deaths"]):
                            if "]: <" in line:
                                get_time = line.split()
                                get_player_name = re.search(r"<(.*?)>", line)
                                player_name = get_player_name.group(1)
                                chat_message = line.split("<")[1].split(">")[1]
                                message = discord.Embed(description="", color=0x0000FF)
                                message.set_author(name=f"{get_time[0]} | {player_name}: {chat_message}")
                                channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Chat"])
                                await channel.send(embed=message)
                                break

                            if 'Villager bxz' in line:
                                collect_coordinates, search_coordinates_info = [], [r"x=(.*?),", r"y=(.*?),",
                                                                                    r"z=(.*?)]",
                                                                                    r"message: '(.*?)'"]
                                for i in range(4):
                                    get_position = re.search(search_coordinates_info[i], line)
                                    collect_coordinates.append(get_position.group(1))

                                village_death = line.split()
                                get_time = village_death[0]
                                del village_death[0:3]
                                message = discord.Embed(description="", color=0xFFBF00)
                                message.set_author(
                                    name=f"{get_time} | Villager bxz | {collect_coordinates[3]} at position"
                                         f" {collect_coordinates[0]},{collect_coordinates[1]},{collect_coordinates[2]}")
                                channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Activity"])
                                await channel.send(embed=message)
                            else:
                                line = line.split()
                                get_time = line[0]
                                del line[0:3]
                                message = discord.Embed(description="", color=0xFFBF00)
                                message.set_author(name=f"{get_time} | {' '.join(line)}")
                                channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Activity"])
                                await channel.send(embed=message)

                        if "stop" in line:
                            message = discord.Embed(description="", color=0xFF0000)
                            message.set_author(name=f"Server is stopping! Will be online soon!")
                            channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Activity"])
                            await channel.send(embed=message)
                            await client.close()

                        if "]: <" in line:
                            get_time = line.split()
                            get_player_name = re.search(r"<(.*?)>", line)
                            player_name = get_player_name.group(1)
                            chat_message = line.split("<")[1].split(">")[1]
                            message = discord.Embed(description="", color=0x0000FF)
                            message.set_author(name=f"{get_time[0]} | {player_name}: {chat_message}")
                            channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Chat"])
                            await channel.send(embed=message)

                        if "joined the game" in line:
                            joined_player = line.split()
                            message = discord.Embed(description="", color=0x00ff00)
                            message.set_author(name=f"{joined_player[0]} | {joined_player[3]} joined")
                            channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Activity"])
                            await channel.send(embed=message)

                        if "left the game" in line:
                            left_player = line.split()
                            message = discord.Embed(description="", color=0xFF0000)
                            message.set_author(name=f"{left_player[0]} | {left_player[3]} left")
                            channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Activity"])
                            await channel.send(embed=message)

                await asyncio.sleep(1)
            except mcrcon.MCRconException:
                # Handle any Rcon connection errors here.
                print(f"Rcon connection error")
                # Wait for 5 seconds before trying to reconnect to the server.
                await asyncio.sleep(5)

    if time_check is True:
        await asyncio.sleep(3900)


# Use a task to run the read_chat_log function every 10 seconds.
@tasks.loop(seconds=10)
async def read_chat_log_loop():
    await read_player_chat_messages()


async def send_minecraft_chat(message):
    rcon.command(f"say [DISCORD] {message}")


@client.event
async def on_message(message):
    get_channel = get_info()
    # Check if message is from the designated channel.
    if message.channel.id == get_channel[0]["Channels"]["Discord_Minecraft_Chat"]:
        # Check if message is not from the bot itself.
        if message.author != client.user:
            # Get the member object of the message author.
            member = message.author
            # Check if the member has the specified role.
            role_name = 'Minecraft'
            role = discord.utils.get(member.roles, name=role_name)
            if role is not None:
                # Send message to Minecraft chat.
                await send_minecraft_chat(f"{message.author}: {message.content}")
            else:
                await message.channel.send(f"{member.mention} does not have the {role_name} role.")

    if message.channel.id == get_channel[0]["Channels"]["Discord_Minecraft_Activity"]:
        # Check if message is not from the bot itself.
        if message.author != client.user:
            # Get the member object of the message author.
            member = message.author
            # Check if the member has the specified role.
            role_name = 'Minecraft'
            role = discord.utils.get(member.roles, name=role_name)
            if role is None:
                await message.channel.send(f'{member.mention} does not have the {role_name} role.')


@tasks.loop(seconds=1)
async def check_time_schedule():
    while True:
        current_time = datetime.datetime.now().time()
        time_11_30pm = datetime.time(23, 35)
        time_12_30pm = datetime.time(0, 35)

        if current_time.hour == time_11_30pm.hour and current_time.minute == time_11_30pm.minute:
            get_activity = get_info()

            bot_message = f"BOT {client.user} will stop reading server chat for an hour!\nThe Minecraft Server will " \
                          f"still be online."
            await send_minecraft_chat(f"{bot_message}")

            message = discord.Embed(description="", color=0xFF0000)
            message.set_author(name=bot_message)
            channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Activity"])
            await channel.send(embed=message)
            # Delay to avoid sending multiple messages at the same time.
            await asyncio.sleep(60)

        if current_time.hour == time_12_30pm.hour and current_time.minute == time_12_30pm.minute:
            get_activity = get_info()
            bot_message = f"BOT {client.user} is back online!"
            await send_minecraft_chat(f"{bot_message}")

            message = discord.Embed(description="", color=0xFF0000)
            message.set_author(name=bot_message)
            channel = client.get_channel(get_activity[0]["Channels"]["Discord_Minecraft_Activity"])
            await channel.send(embed=message)
            # Delay to avoid sending multiple messages at the same time
            await asyncio.sleep(60)

        await asyncio.sleep(10)


def get_info():
    config_file = f"{os.path.dirname(os.path.realpath(__file__))}\\Bot Settings\\config.json"
    with open(config_file) as f:
        configuration_information = json.load(f)
    return configuration_information


# Start the Discord bot.
@client.event
async def on_ready():
    print(f"BOT {client.user} IS ONLINE!")
    await client.change_presence(activity=discord.Game(name="Minecraft!"))
    try:
        read_chat_log_loop.start()
        check_time_schedule.start()
    except Exception as f:
        print(f"{f}")
    finally:
        print(f"MINECRAFT DISCORD BOT IS NOW RUNNING")


if __name__ == "__main__":
    print(f"STARTING MINECRAFT DISCORD BOT")
    try:
        getSetup = get_info()
        rcon = mcrcon.MCRcon(getSetup[0]["Rcon_Information"]["IP_Address"], getSetup[0]["Rcon_Information"]["Password"],
                             getSetup[0]["Rcon_Information"]["Port"])
        rcon.connect()
        client.run(getSetup[0]["Discord_API"])
    except Exception as e:
        print(f"{e}")
    finally:
        print(f"MINECRAFT DISCORD BOT STARTED")
