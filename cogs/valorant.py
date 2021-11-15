import discord
import os
import random
from discord.ext import commands


class Valorant(commands.Cog):

	def __init__(self, commands):
		self.commands = commands

	@commands.command()
	async def rndgun(self, ctx, guntype = 'all'):
		if guntype == 'light':
			gun = ['Classic',
				   'Shorty',
				   'Frenzy',
				   'Ghost',
				   'Sheriff']
			await ctx.send(f'The gun you have selected is the {random.choice(gun)}.')
		elif guntype == 'mid':
			gun = ['Stinger',
				   'Spectre',
				   'Bucky',
				   'Judge',
				   'Bulldog',
				   'Guardian',
				   'Marshal',
				   'Ares']
			await ctx.send(f'The gun you have selected is the {random.choice(gun)}.')
		elif guntype == 'heavy':
			gun = ['Phantom',
				   'Vandal',
				   'Operator',
				   'Odin']
			await ctx.send(f'The gun you have selected is the {random.choice(gun)}.')
		else:
			gun = ['Classic',
				   'Shorty',
				   'Frenzy',
				   'Ghost',
				   'Sheriff',
				   'Stinger',
				   'Spectre',
				   'Bucky',
				   'Judge',
				   'Bulldog',
				   'Guardian',
				   'Marshal',
				   'Ares',
				   'Phantom',
				   'Vandal',
				   'Operator',
				   'Odin']
			await ctx.send(f'The gun you have selected is the {random.choice(gun)}.')


def setup(client):
    client.add_cog(Valorant(client))
