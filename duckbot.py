import discord
import os
from discord.ext import commands, tasks
from keep_alive import keep_alive
from itertools import cycle


client = commands.Bot(command_prefix='?')
keep_alive()
token = os.environ['DISCORD_BOT_TOKEN']
status = cycle(['need help with the bot?', 'send ?bothelp'])


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
async def bothelp(ctx):
    await ctx.send('''here\'s a list of commands you can currenly use:

**Bot Info**
?bothelp > returns list of commands
?botping > returns bot latency

**Simple Response**
?ducky > quack
?goose > honk
?doggo > bork
?catto > mlem
?bunny > pyon
?viper > viper mommy mmmmmmmmm (returns image)

**Randomizers**
?ask [query] > responds to a question with yes/maybe/no
?rng [min] [max] > picks a random integer between the two parameters (default 1-10) | aliases: ?rand
?coin > flips a coin | aliases: ?flip, ?cointoss
?card > draws a random card from a standard deck of 52 | aliases: ?shuffle''')


@client.command()
async def botping(ctx):
    await ctx.send(f'The bot\'s latency is {round(client.latency * 1000)}ms.')


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
