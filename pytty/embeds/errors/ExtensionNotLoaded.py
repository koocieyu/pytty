import discord
from datetime import datetime

def embed_response(extension):
    embed = discord.Embed()
    embed.description = f"The extension `{extension}` was not loaded!"
    embed.set_footer(
        text="ExtensionNotLoaded"
    )
    embed.timestamp = datetime.now()
    return embed