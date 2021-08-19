import discord
import os
import random
from discord.ext import commands


class Randomizer(commands.Cog):

	def __init__(self, commands):
		self.commands = commands

	@commands.command()
	async def ask(self, ctx, please = '', *, question : str):
		if please == 'please':
			responses = ['Yes :grin:',
 					 'Of course :grin:',
                     'Maybe :thinking:',
                     'I don\'t know :thinking:',
                     'No :pensive:',
                     'I don\'t think so :pensive:']
			await ctx.send(f'''> {question}
{random.choice(responses)}''')
		else:
			await ctx.send('im not answering that lmao')

	@commands.command(aliases=['flip', 'cointoss'])
	async def coin(self, ctx, please = ''):
		if please == 'please':
			responses = ['heads', 'tails']
			await ctx.send(f'{random.choice(responses)}')
		else:
			await ctx.send('don\'t you have spare change lying aroud somewhere? just use that lmao')

	
	@commands.command(aliases=['rand'])
	async def rng(self, ctx, minval=1, maxval=10, please = ''):
		if please == 'please':
			if minval >= maxval:
				await ctx.send('Make sure that the lower value is written before the higher value.')
				raise ValueError('minval is larger than maxval')
			else:
				val = random.randint(int(minval), int(maxval))
				await ctx.send(f'{val}')
		else:
			await ctx.send('just think of a number lmao')


	@commands.command(aliases=['shuffle'])
	async def card(self, ctx, please = ''):
		if please == 'please':
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
		else:
			await ctx.send('bugger off m8 just think of a card')

	# error msg starts here
	@ask.error
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('What\'s the question?')
		else:
			raise error

def setup(client):
    client.add_cog(Randomizer(client))
