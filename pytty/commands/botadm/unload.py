import discord
from discord.ext import commands
from pytty.embeds.errors import ExtensionNotLoaded as err_ENL
from pytty.embeds.commands.unload import embed_response


@commands.command(hidden=True)
@commands.is_owner()
async def unload(ctx: commands.Context, to_load):
    Bot: commands.Bot = ctx.bot
    try:
        Bot.unload_extension(to_load)
    except commands.ExtensionNotLoaded:
        await ctx.send(embed=err_ENL.embed_response(to_load))
    else:
        await ctx.send(embed=embed_response(to_load))
    
def setup(client: commands.Bot):
    client.add_command(unload)