import discord
from datetime import datetime

def embed_response(extension):
    embed = discord.Embed()
    embed.description = f"The extension `{extension}` does not have a setup function!"
    embed.set_footer(
        text="NoEntryPointError"
    )
    embed.timestamp = datetime.now()
    return embed