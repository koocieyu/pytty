import discord
from datetime import datetime

def embed_response(extension):
    embed = discord.Embed()
    embed.description = f"The extension `{extension}` could not be found!"
    embed.set_footer(
        text="ExtensionNotFound"
    )
    embed.timestamp = datetime.now()
    return embed