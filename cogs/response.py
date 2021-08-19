import discord
import os
from discord.ext import commands


class Response(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ducky(self, ctx, please = ''):
		if please == 'please':
			await ctx.send('quack')
		else:
			await ctx.send('you can\'t just demand things of me...')

	@commands.command()
	async def goose(self, ctx, please = ''):
		if please == 'please':
			await ctx.send('honk')
		else:
			await ctx.send('please be nice :pensive:')

	@commands.command()
	async def doggo(self, ctx, please = ''):
		if please == 'please':
			await ctx.send('bork')
		else:
			await ctx.send('not even a please? damn ok')

	@commands.command()
	async def catto(self, ctx, please = ''):
		if please == 'please':
			await ctx.send('mlem')
		else:
			await ctx.send('your catto can wait')

	@commands.command()
	async def bunny(self, ctx, please = ''):
		if please == 'please':
			await ctx.send('pyon')
		else:
			await ctx.send('bunnies ooh (nope, gotta say please)')

	@commands.command()
	async def wisdom(self, ctx, please = ''):
		if please == 'please':
			await ctx.send('I don\'t think you should be asking a Discord bot for wisdom.')
		else:
			await ctx.send('i dont get paid enough for this')


def setup(client):
	client.add_cog(Response(client))
