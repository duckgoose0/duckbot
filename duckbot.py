import discord
import os
from discord.ext import commands, tasks
from keep_alive import keep_alive
from itertools import cycle


client = commands.Bot(command_prefix='duck ')
keep_alive()
token = os.environ['DISCORD_BOT_TOKEN']
status = cycle(['need help with the bot?', 'send duck bot help'])


@client.event  # bot birthday is july 1
async def on_ready():
    change_status.start()
    print('duckbot is running...')

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('The command you are trying to use does not exist.')
	else:
		raise error


@client.command()
async def bot(ctx, param1 = '', param2 = ''):
	if param1 == 'help':
		await ctx.send('''Here\'s a list of commands you can currenly use. Remember to say please when you need the bot to do something :)

**Bot Info**
bot | gateway command for bot information and settings 

**Simple Response**
ducky | quack
goose | honk
doggo | bork
catto | mlem
bunny | pyon

**Randomizers**
ask <query> | responds to a question with yes/maybe/no
rng <min> <max> | picks a random integer between the two parameters (default 1-10) | aliases: duck:rand
coin | flips a coin | aliases: duck:flip, duck:cointoss
card | draws a random card from a standard deck of 52 | aliases: duck:shuffle
wisdom | asks the bot for wisdom!''')
	elif param1 == 'ping':
		await ctx.send(f'Pong! The bot\'s latency is {round(client.latency * 1000)}ms.')
	#elif param1 == 'prefix':
		#if param2 == '':
			#await ctx.send('Set the prefix the bot uses for this server by typing "duck:bot prefix <prefix>')'"
		#elif len(param2) >= 5:
			#command to set prefix here
		#else:
			#error message for invalid command here
	elif param1 == 'about':
		await ctx.send('''I\'m duckbot! I was created by duckgoose#6969 as a summer project to get familiar with Python. You can reach my creator at https://twitter.com/_duckgoose_.
		
Current Version: 2.1.0 beta''')
	elif param1 == '':
		await ctx.send('''These are the commands under duck:bot (format: duck:bot <command> <optional parameter>):
		
help | sends a full list of commands (planned to be obsolete in next update)
ping | pong! returns the bot's latency
about | gives you information about the bot and its very sexy creator
prefix | allows you to set the bot's server prefix (not functional yet) | required parameter: prefix (string, < 6 characters)''')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
