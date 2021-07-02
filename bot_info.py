import discord
import os
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bothelp(self, ctx):
        await ctx.send('''here\'s a list of commands you can currenly use:

//bot info
?bothelp > returns list of commands
?botping > returns bot latency

//server tools
?clear [int] > deletes [int] number of messages in channel. if [int] is not specified, default is 5 | aliases: ?purge, ?delete

//simple response
?duck > quack
?goose > honk
?doggo > bork
?catto > mlem

//randomizers
?ask [query] > responds to a question with yes/maybe/no
?coin > flips a coin | aliases: ?flip, ?cointoss
?card > draws a random card from a standard deck of 52 | aliases: ?shuffle''')

    @commands.command()
    async def botping(self, ctx):
        await ctx.send(f'The bot\'s latency is {round(self.latency * 1000)}ms.')


def setup(client):
    client.add_Cog(Info(client))
