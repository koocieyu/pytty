import discord
from discord.ext import commands
from platform import python_version
from pytty.embeds.commands.info import embed_response

class Misc(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def info(self, ctx):
        await ctx.send(
            embed=embed_response(
                python_version(),
                sum(1 for _ in self.client.guilds),
                sum(1 for _ in self.client.get_all_members()),
                self.client.user.name,
                self.client.user.discriminator
            )
        )


def setup(client: commands.Bot):
    client.add_cog(Misc(client))