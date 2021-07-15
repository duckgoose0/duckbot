import discord
import os
from discord.ext import commands


class Response(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ducky(self, ctx):
		await ctx.send('quack')

	@commands.command()
	async def goose(self, ctx):
		await ctx.send('honk')

	@commands.command()
	async def doggo(self, ctx):
		await ctx.send('bork')

	@commands.command()
	async def catto(self, ctx):
		await ctx.send('mlem')

	@commands.command()
	async def bunny(self, ctx):
		await ctx.send('pyon')


def setup(client):
	client.add_cog(Response(client))
