import discord
import os
import random
from discord.ext import commands


class Randomizer(commands.Cog):

	def __init__(self, commands):
		self.commands = commands

	@commands.command()
	async def ask(self, ctx, *, question : str):
		responses = ['Yes :grin:',
 					 'Of course :grin:',
                     'Maybe :thinking:',
                     'I don\'t know :thinking:',
                     'No :pensive:',
                     'I don\'t think so :pensive:']
		await ctx.send(f'''> {question}
{random.choice(responses)}''')

	@commands.command(aliases=['flip', 'cointoss'])
	async def coin(self, ctx):
		responses = ['heads', 'tails']
		await ctx.send(f'{random.choice(responses)}')

	
	@commands.command(aliases=['rand'])
	async def rng(self, ctx, minval=1, maxval=10):
		if minval >= maxval:
			await ctx.send('Make sure that the lower value is written before the higher value.')
			raise ValueError('minval is larger than maxval')
		else:
			val = random.randint(int(minval), int(maxval))
			await ctx.send(f'{val}')


	@commands.command(aliases=['shuffle'])
	async def card(self, ctx):
		value = ['Ace',
                 '2',
                 '3',
                 '4',
                 '5',
                 '6',
                 '7',
                 '8',
                 '9',
                 '10',
                 'Jack',
                 'Queen',
                 'King']
		suit = ['Clubs',
                'Hearts',
                'Spades',
                'Diamonds']
		await ctx.send(f'I drew the {random.choice(value)} of {random.choice(suit)}.')

	# error msg starts here
	@ask.error
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('What\'s the question?')
		else:
			raise error

def setup(client):
    client.add_cog(Randomizer(client))
