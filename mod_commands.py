import discord
import os
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['purge', 'delete'])
    @commands.has_role("Developer")
    async def clear(self, ctx, num=6):
        try:
            await ctx.channel.purge(limit=num)
        except commands.MissingRole:
            await ctx.send('You don\'t have permission to use that command!')


def setup(client):
    client.add_Cog(Info(client))
