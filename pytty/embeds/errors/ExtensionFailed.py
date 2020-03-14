import discord
from datetime import datetime

def embed_response(extension):
    embed = discord.Embed()
    embed.description = f"The extension `{extension}` had an execution error!"
    embed.set_footer(
        text="ExtensionFailed"
    )
    embed.timestamp = datetime.now()
    return embed