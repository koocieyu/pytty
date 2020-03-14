import discord
from datetime import datetime

def embed_response(extension):
    embed = discord.Embed()
    embed.description = f"The extension `{extension}` has been successfully loaded!"
    embed.set_footer(
        text="Success!"
    )
    embed.timestamp = datetime.now()
    return embed