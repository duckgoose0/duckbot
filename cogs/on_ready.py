import discord
import os
from discord.ext import commands


class Startup(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('duckbot is running...')


def setup(client):
    client.add_cog(Startup(client))
