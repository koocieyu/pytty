import discord
import json
import os

from discord.ext import commands

json_secret = {}

with open(".json") as file_in:
    json_secret = json.load(file_in)

client = commands.Bot(
    command_prefix="y."
)

@client.event
async def on_ready():
    print("logged in")

for category in os.listdir("pytty/commands"):
    if category.find(".") == -1:
        for command in os.listdir(f"pytty/commands/{category}"):
            if command.endswith(".py"):
                client.load_extension(f"pytty.commands.{category}.{command[:-3]}")

# for error_file in os.listdir("pytty/errors"):
#     if error_file.endswith(".py"):
#         client.load_extension(f"pytty.errors.{error_file[:-3]}")

for event_file in os.listdir("pytty/events"):
    if event_file.endswith(".py"):
        client.load_extension(f"pytty.events.{event_file[:-3]}")

client.run(json_secret["token"])
json_secret = ""