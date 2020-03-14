import discord
from discord.ext import commands

class on_ready_event(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("""
        _   _
       (.)_(.)
    _ (   _   ) _
   / \/`-----'\/ \      - Meow, he said
 __\ ( (     ) ) /__      enthusiastically.
 )   /\ \._./ /\   (
  )_/ /|\   /|\ \_(
        """)
        print(f"""
Started successfully!
Currently on {sum(1 for _ in self.client.guilds)} servers.
Currently serving {sum(1 for _ in self.client.get_all_members())} humans. 
        """)

def setup(client: commands.Bot):
    client.add_cog(on_ready_event(client))