import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot


class Info(commands.Cog):

	def __init__(self, client):
		self.client = client


	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong! The bot\'s latency is {round(self.client.latency * 1000)}ms.')

	@commands.command()
	async def about(self, ctx):
		await ctx.send(
			'''I\'m duckbot! I was created as a summer project to get familiar with Python. You can reach my creator at https://twitter.com/_duckgoose_.
		
			Current Version: 2.3.0 beta''')

def setup(client):
    client.add_cog(Info(client))