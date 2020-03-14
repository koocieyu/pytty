import discord
from discord.ext import commands
from pytty.embeds.errors import ExtensionAlreadyLoaded as err_EAL
from pytty.embeds.errors import ExtensionFailed as err_EF
from pytty.embeds.errors import ExtensionNotFound as err_ENF
from pytty.embeds.errors import NoEntryPointError as err_NEPE
from pytty.embeds.commands.load import embed_response

@commands.command(hidden=True)
@commands.is_owner()
async def load(ctx: commands.Context, to_load):
    Bot: commands.Bot = ctx.bot
    try:
        Bot.load_extension(to_load)
    except commands.ExtensionAlreadyLoaded:
        await ctx.send(embed=err_EAL.embed_response(to_load))
    except commands.ExtensionFailed:
        await ctx.send(embed=err_EF.embed_response(to_load))
    except commands.ExtensionNotFound:
        await ctx.send(embed=err_ENF.embed_response(to_load))
    except commands.NoEntryPointError:
        await ctx.send(embed=err_NEPE.embed_response(to_load))
    else:
        await ctx.send(embed=embed_response(to_load))
    
def setup(client: commands.Bot):
    client.add_command(load)