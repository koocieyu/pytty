import discord
from datetime import datetime

def embed_response(
    python_version, guild_amount,
    user_amount, bot_username,
    bot_discrim
):
    embed = discord.Embed()\
        .set_footer(
            text="pretty fun down there if you ask me"
        )\
        .add_field(
            name="Python version",
            value=python_version,
        )\
        .add_field(
            name="discord.py version",
            value=discord.__version__
        )\
        .add_field(
            name="Guilds",
            value=guild_amount,
            inline=False
        )\
        .add_field(
            name="Users",
            value=user_amount,
            inline=True
        )
    embed.description = "Informations about this bot"
    embed.title = f"{bot_username}#{bot_discrim}"
    embed.timestamp = datetime.now()
    return embed