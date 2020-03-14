import discord
from datetime import datetime

def embed_response(extension):
    embed = discord.Embed()
    embed.description = f"The extension `{extension}` is already loaded!"
    embed.set_footer(
        text="ExtensionAlreadyLoaded"
    )
    embed.timestamp = datetime.now()
    return embed